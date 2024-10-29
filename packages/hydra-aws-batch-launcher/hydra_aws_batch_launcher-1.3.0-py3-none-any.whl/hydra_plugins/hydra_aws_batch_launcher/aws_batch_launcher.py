import hashlib
import logging
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from typing import Any, Optional, Sequence

import boto3
from hydra.core.utils import JobReturn, JobStatus
from hydra.plugins.launcher import Launcher
from hydra.types import HydraContext, TaskFunction
import multiprocessing
from hydra import compose
from tqdm import tqdm
from botocore.config import Config
from omegaconf import DictConfig, OmegaConf

from hydra_plugins.hydra_aws_batch_launcher.config import AWSBatchLauncherConf
from tqdm import tqdm

logger = logging.getLogger(__name__)


def validation_callback(future):
    try:
        batch_results = future.result()
        logger.info(f"Batch processed successfully with {len(batch_results)} results.")
    except Exception as e:
        logger.error(f"Error processing batch: {str(e)}")

def validate_batch(batch, test_config_name):
    results = []
    for override in batch:
        cfg = compose(config_name=test_config_name, overrides=override)

    return results

def batch_iterator(iterable, batch_size):
    """Yield successive batches from the iterable."""
    for i in range(0, len(iterable), batch_size):
        yield iterable[i:i + batch_size]

class AWSBatchLauncher(Launcher):
    def __init__(self, **kwargs: Any) -> None:
        self.config: Optional[DictConfig] = None
        self.task_function: Optional[TaskFunction] = None
        self.hydra_context: Optional[HydraContext] = None

        self.launcher_config: AWSBatchLauncherConf = AWSBatchLauncherConf(**kwargs)

    def setup(
            self,
            *,
            hydra_context: HydraContext,
            task_function: TaskFunction,
            config: DictConfig,
    ) -> None:
        self.config = config
        self.task_function = task_function
        self.hydra_context = hydra_context

    def launch(
            self, job_overrides: Sequence[Sequence[str]], initial_job_idx: int
    ) -> Sequence[JobReturn]:
        logger.info(f"Starting {len(job_overrides)} jobs")

        hashes = self.preprocess_configs(self.config.hydra.job.name, job_overrides)

        if self.launcher_config.test_config_before_submit:
            if not self.launcher_config.test_config_name:
                raise ValueError("test_config_name cannot be empty")

            self.validate_config_in_parallel(job_overrides)

        return self.submit_jobs_in_parallel(hashes, job_overrides)

    def preprocess_configs(self, job_name, job_overrides):
        logger.info("Adding sweep dir and job number to all overrides")

        hashes = []
        for override in tqdm(job_overrides, desc="Preprocess Config", unit="config"):
            # Process each override
            for standard_override in self.launcher_config.standard_overrides:
                override.append(standard_override)

            if self.launcher_config.override_job_name:
                override.append(f"hydra.job.name={job_name}")

            current_hash = compute_hash(override)
            if self.launcher_config.add_config_hash:
                override.append(f"{self.launcher_config.hash_key}={current_hash}")

            hashes.append(current_hash)
        return hashes

    def validate_config_in_parallel(self, job_overrides):
        with ProcessPoolExecutor(max_workers=self.launcher_config.test_n_processes) as executor:
            futures = []

            for batch in tqdm(batch_iterator(job_overrides, self.launcher_config.test_batch_size),
                              desc="Scheduling Job Overrides", unit="batch"):
                future = executor.submit(validate_batch, batch, self.launcher_config.test_config_name)
                future.add_done_callback(validation_callback)  # Attach the callback to each future
                futures.append(future)

            logger.info("All configs scheduled for testing")

            # Use tqdm to monitor completion of all futures
            for _ in tqdm(as_completed(futures), total=len(futures), desc="Processing Batches", unit="batch"):
                pass  # The callback handles the result collection and logging

            logger.info("All configs successfully tested")

    def submit_jobs_in_parallel(self, hashes, job_overrides):
        logger.info("Submit AWS Batch jobs")

        with ThreadPoolExecutor(max_workers=self.launcher_config.n_jobs) as executor:
            # Submit all jobs and collect the Future objects
            futures = [
                executor.submit(
                    self.submit_job,
                    current_hash,
                    self.launcher_config.aws_job_queue,
                    self.launcher_config.aws_job_definition,
                    override
                )
                for current_hash, override in zip(hashes, job_overrides)
            ]

            # Use tqdm to display a progress bar as jobs complete
            for future in tqdm(as_completed(futures), total=len(futures)):
                try:
                    # Optionally retrieve the result of each job
                    result = future.result()
                    # You can process the result here if needed
                except Exception as e:
                    # Handle exceptions if any of the jobs fail
                    logger.error(f"Job failed with exception: {e}")

        job_returns = []
        for override in job_overrides:
            job_returns.append(JobReturn(status=JobStatus.COMPLETED))
        return job_returns

    def submit_job(self, job_name, job_queue, job_definition, command):
        retry_config = Config(
            retries={
                'max_attempts': self.launcher_config.aws_retry_max_attempts,  # Total number of retry attempts
                'mode': self.launcher_config.aws_retry_mode  # Retry mode ('legacy', 'standard', or 'adaptive')
            }
        )
        session = boto3.Session(profile_name=self.launcher_config.aws_profile)
        client = session.client('batch', region_name=self.launcher_config.aws_region, config=retry_config)

        job_parameters = {
            'jobName': job_name,
            'jobQueue': job_queue,
            'jobDefinition': job_definition,
            'containerOverrides': {
                'command': command
            }
        }

        if self.launcher_config.aws_tags:
            tags = OmegaConf.to_container(self.launcher_config.aws_tags, resolve=True)
            job_parameters["tags"] = tags

        response = client.submit_job(**job_parameters)
        return response['jobId']


def compute_hash(parameters_list: Sequence[str]):
    concatenated_params = " ".join(parameters_list)
    hash_object = hashlib.sha256()
    hash_object.update(concatenated_params.encode('utf-8'))
    return hash_object.hexdigest()
