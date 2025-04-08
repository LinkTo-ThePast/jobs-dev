import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent));


import logging
from app.SK.services.get_jobs import JobService;
from app.SK.services.send_application import ApplicationService;

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    configure_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # --->>> REFACTOR: DINAMICALLY CHANGE ID
        target_job_id = "6787"  
        cv_path = "example-cv.pdf" ## extract from our own cv tool
        
        # Get job with ID
        job = JobService.find_job_by_id(target_job_id)
        logger.info(f"Applying for job: {job.title} (ID: {job.job_id})")
        
        # Submit application POST
        response = ApplicationService.submit_application(
            job_id=job.job_id,
            applicant_name="Daniel Diego Hernández Alvarado",
            applicant_email="diego-hdzl-1933@gmail.com",
            applicant_phone="5521220527",
            cover_letter="Especialista en diseño gráfico y comunicación",
            cv_path=cv_path
        )
        
        logger.info(f"Application submitted successfully: {response}")
        
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()