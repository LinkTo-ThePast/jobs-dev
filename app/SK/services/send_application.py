import requests;
from typing import Dict, Optional;
from pathlib import Path;
from app.SK.models.job import Job;
from app.SK.config.settings import settings;


class ApplicationService:
    @staticmethod
    def submit_application( ## -----> SUKARNE DATA STRUCTURE
        job_id: str,
        applicant_name: str,
        applicant_email: str,
        applicant_phone: str,
        cover_letter: str,
        cv_path: str,
        privacy_policy_accepted: bool = True
    ) -> Dict:
        """
        Submits a job application to Sukarne.
        
        Args:
            job_id: The ID of the job to apply for
            applicant_name: Full name of applicant
            applicant_email: Email address
            applicant_phone: Phone number
            cover_letter: Application cover letter
            cv_path: Path to CV/resume file
            privacy_policy_accepted: Whether privacy policy is accepted
            
        Returns:
            Dict: Response from the server
            
        Raises:
            ValueError: For invalid inputs
            requests.RequestException: For network errors
            FileNotFoundError: If CV file doesn't exist
        """
        if not privacy_policy_accepted:
            raise ValueError("Privacy policy must be accepted to submit application")
        
        cv_file = Path(cv_path)
        if not cv_file.exists():
            raise FileNotFoundError(f"CV file not found at {cv_path}")
        
        files = {
            'awsm_file': (cv_file.name, open(cv_path, 'rb'))
        }
        
        data = {
            'awsm_applicant_name': applicant_name,
            'awsm_applicant_email': applicant_email,
            'awsm_applicant_phone': applicant_phone,
            'awsm_applicant_letter': cover_letter,
            'awsm_form_privacy_policy': 'yes' if privacy_policy_accepted else 'no',
            'awsm_job_id': job_id,
            'action': 'awsm_applicant_form_submission',
        }
        
        try:
            response = requests.post(
                settings.APPLICATION_POST_URL,
                data=data,
                headers=settings.DEFAULT_HEADERS,
                files=files
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise requests.RequestException(f"Application submission failed: {str(e)}")
        except ValueError:
            return {'status': 'success', 'message': 'Application submitted but no JSON response'}