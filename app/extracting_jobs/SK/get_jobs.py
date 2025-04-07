import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class JobList:
  """Data class representing a job listing in the HTML of SK"""
  job_id: str
  title: str
  state: str
  city: str
  job_type: str # 'Comercial', 'Operativo', 'Administrativo'
  URL: str


def get_jobs() -> List[JobList]:
  """
    Scrapes job listings from Sukarne careers page.
    
    Returns:
        List[JobListing]: A list of job listing objects
        
    Raises:
        requests.RequestException: If there's an issue with the HTTP request
        ValueError: If the page structure is not as expected
    """
  SK_URL = 'https://www.sukarne.com/es_mx/retosk_vacantes/'

  ## TRY - CATCH: network request
  try:
    response = requests.get(SK_URL, timeout=10);
    response.raise_for_status() ## --> bad response
  except requests.RequestException as e: (f'Failed to retrieve jobs from SuKarne: {str(e)}');

  soup = BeautifulSoup(response.text, 'html.parser');

  ## select div: class="awsm-job-listings awsm-row awsm-grid-col-3" or "class="awsm-job-listing-item awsm-grid-item""
  job_containers = soup.select('div.awsm-job-listing-item');
  
  ## detect if list is empty
  if not job_containers:
    raise ValueError("No jobs found in SuKarne web site. Maybe structure has changed!");

  jobs = [];

  for container in job_containers:
    try:
        # Retrieve job ID 
        job_id = container.get('id', '').replace('awsm-grid-item-', '')
            
        # Retrieve title
        title_element = container.select_one('h2.awsm-job-post-title')
        title = title_element.get_text(strip=True) if title_element else 'No definido'
            
        # Retrieve URL
        link_element = container.select_one('a.awsm-job-item')
        url = link_element.get('href', '') if link_element else ''
            
        # Retrieve state, city and job type
        spec_terms = container.select('span.awsm-job-specification-term')
            
        # 0 -> state, 1 -> city, 2 -> job type
        state = spec_terms[0].get_text(strip=True) if len(spec_terms) > 0 else 'No definido'
        city = spec_terms[1].get_text(strip=True) if len(spec_terms) > 1 else 'No definido'
        job_type = spec_terms[2].get_text(strip=True) if len(spec_terms) > 2 else 'No definido'

        jobs.append(JobList(
          job_id = job_id,
          title = title,
          state = state,
          city = city,
          job_type = job_type,
          URL = url
        ))
    except Exception as e:
      ## if some job container fails, continue with others
      print(f'Error trying to retrieve one job from the list: {e}');
      continue;
  return jobs;

if __name__ == "__main__":
  try:
    job_list = get_jobs();
    print(f'Se encontraron {len(job_list)} empleos.')
    for job in job_list:
      print(f'\nTítulo: {job.title}');
      print(f'Ubicación: {job.city}, {job.state}');
      print(f'Tipo de empleo: {job.job_type}')
      print(f'URL: {job.URL}');
  except Exception as e:
    print(f'Error al momento de recuperar las vacantes: {e}');    