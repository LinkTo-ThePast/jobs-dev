import requests;
from bs4 import BeautifulSoup;
from typing import List;
from app.SK.models.job import Job;
from app.SK.config.settings import settings

class JobService:
    @staticmethod
    def get_jobs() -> List[Job]:
        """
        Fetches current job listings from Sukarne careers page.
        
        Returns:
            List[Job]: List of available jobs
            
        Raises:
            requests.RequestException: For network-related errors
            ValueError: If page structure is unexpected
        """
        ## TRY - EXCEP: network request
        try:
            response = requests.get(settings.JOB_LISTINGS_URL, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to fetch jobs: {str(e)}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        job_containers = soup.select('div.awsm-job-listing-item')
        
        if not job_containers:
            raise ValueError("No job listings found - page structure may have changed")
        
        jobs = []
        
        for container in job_containers:
            try:
                ## retrieve ID
                job_id = container.get('id', '').replace('awsm-grid-item-', '')
                ## retrieve title 
                title_element = container.select_one('h2.awsm-job-post-title')
                title = title_element.get_text(strip=True) if title_element else 'N/A'
                ## URL
                link_element = container.select_one('a.awsm-job-item')
                url = link_element.get('href', '') if link_element else ''
                
                ## 0 --> city, 2 ---> state, 3 ----> type of job
                spec_terms = container.select('span.awsm-job-specification-term')
                state = spec_terms[0].get_text(strip=True) if len(spec_terms) > 0 else 'N/A'
                city = spec_terms[1].get_text(strip=True) if len(spec_terms) > 1 else 'N/A'
                job_type = spec_terms[2].get_text(strip=True) if len(spec_terms) > 2 else 'N/A'
                
                jobs.append(Job(
                    job_id=job_id,
                    title=title,
                    state=state,
                    city=city,
                    job_type=job_type,
                    url=url
                ))
            except Exception as e:
                continue
        
        return jobs

    @staticmethod
    def find_job_by_id(job_id: str) -> Job:
        """id searching only, but NEEDS REFACTOR:"""
        jobs = JobService.get_jobs()
        for job in jobs:
            if job.job_id == job_id:
                return job
        raise ValueError(f"Job with ID {job_id} not found")