from bs4 import BeautifulSoup;
import requests;

def parse_tag(soup, html_tag):
  
  label = [e.text[:-2] for e in soup.find_all(html_tag)];
  
  return label;

## For demo purposes: extract directly an URL from "bolsa de trabajo - suKarne" ---> but needs refactor
JOB_URL = "https://www.sukarne.com/es/vacante/job";
job_response = requests.get(JOB_URL);

soup = BeautifulSoup(job_response.text, 'html.parser');
print(soup.text)

## Form structure 

form = {
  'awsm-applicant-name': "name",
  'awsm-applicant-phone': "phone",
  'awsm-applicant-email': "email", 
  'awsm-cover-latter': "description", 
  'awsm-application-file': "file"
}

#find all job requirements

get_jobs = parse_tag(soup, "label");
print(get_jobs);





