"""
Quantum Job Manager

Track, monitor, and retrieve quantum job results.
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from qiskit_ibm_runtime import QiskitRuntimeService


class JobManager:
    """Manages quantum jobs on IBM Quantum Platform."""

    def __init__(self, service: QiskitRuntimeService = None):
        """
        Initialize JobManager.

        Args:
            service: QiskitRuntimeService instance (creates new if None)
        """
        self.service = service or QiskitRuntimeService()
        self._job_cache: Dict[str, Any] = {}

    def get_job(self, job_id: str):
        """
        Retrieve a job by ID.

        Args:
            job_id: The job ID

        Returns:
            Job object
        """
        if job_id not in self._job_cache:
            self._job_cache[job_id] = self.service.job(job_id)
        return self._job_cache[job_id]

    def list_jobs(
        self,
        limit: int = 10,
        status: Optional[str] = None,
        backend: Optional[str] = None
    ) -> List:
        """
        List recent jobs.

        Args:
            limit: Maximum number of jobs to return
            status: Filter by status ("Queued", "Running", "Done", "Error")
            backend: Filter by backend name

        Returns:
            List of job objects
        """
        return self.service.jobs(limit=limit, backend_name=backend)

    def get_status(self, job_id: str) -> str:
        """
        Get job status.

        Args:
            job_id: The job ID

        Returns:
            Status string
        """
        job = self.get_job(job_id)
        return job.status()

    def wait_for_result(self, job_id: str, timeout: int = 3600):
        """
        Wait for job to complete and return result.

        Args:
            job_id: The job ID
            timeout: Maximum wait time in seconds

        Returns:
            Job result
        """
        job = self.get_job(job_id)
        return job.result()

    def cancel_job(self, job_id: str) -> bool:
        """
        Cancel a running job.

        Args:
            job_id: The job ID

        Returns:
            True if cancelled successfully
        """
        job = self.get_job(job_id)
        try:
            job.cancel()
            return True
        except Exception as e:
            print(f"Failed to cancel job: {e}")
            return False

    def get_job_info(self, job_id: str) -> Dict:
        """
        Get detailed job information.

        Args:
            job_id: The job ID

        Returns:
            Dictionary with job details
        """
        job = self.get_job(job_id)

        return {
            "job_id": job.job_id(),
            "status": str(job.status()),
            "backend": job.backend().name if job.backend() else "N/A",
            "creation_date": job.creation_date.isoformat() if job.creation_date else "N/A",
        }

    def print_jobs(self, limit: int = 10) -> None:
        """Print formatted job list."""
        jobs = self.list_jobs(limit=limit)

        print(f"{'Job ID':<40} {'Status':<12} {'Backend':<20} {'Date'}")
        print("-" * 90)

        for job in jobs:
            info = self.get_job_info(job.job_id())
            date_str = info["creation_date"][:19] if info["creation_date"] != "N/A" else "N/A"
            print(
                f"{info['job_id']:<40} "
                f"{info['status']:<12} "
                f"{info['backend']:<20} "
                f"{date_str}"
            )

    def get_results_summary(self, job_id: str) -> Dict:
        """
        Get a summary of job results.

        Args:
            job_id: The job ID

        Returns:
            Summary dictionary
        """
        job = self.get_job(job_id)
        result = job.result()

        summary = {
            "job_id": job_id,
            "status": str(job.status()),
            "num_results": len(result),
        }

        # Add result-specific info
        if len(result) > 0:
            pub_result = result[0]
            if hasattr(pub_result.data, "evs"):
                summary["type"] = "estimator"
                summary["expectation_values"] = list(pub_result.data.evs)
            elif hasattr(pub_result.data, "meas"):
                summary["type"] = "sampler"
                summary["counts"] = pub_result.data.meas.get_counts()

        return summary
