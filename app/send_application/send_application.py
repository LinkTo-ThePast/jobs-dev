import requests;

POST_URL = "https://www.sukarne.com/wp-admin/admin-ajax.php";

## trying POST request

## 1. first, structure our body payload: 

## binary for our PDF file:

file = {
   'awsm_file': open('d-cv.pdf', 'rb')
}




headers = {
  'Accept': "application/json, text/javascript, */*; q=0.01",
  'Accept-encoding': "gzip, deflate, br, zstd",
  'Connection': "keep-alive",
}

body = {
  'awsm_applicant_name': "Luis Diego",
  'awsm_applicant_email': "luis@entropia.ai",
  'awsm_applicant_phone': "5581055662",
  'awsm_applicant_letter': "Especialista técnico, reparación de distinto tipo de maquinaria.",
  'awsm_form_privacy_policy': "yes",
  'awsm_job_id': "5262",
  'action': 'awsm_applicant_form_submission', 
}

req = requests.post(POST_URL, data=body, headers=headers, files=file);

print("Status:", req.status_code)
print("Response:", req.text)
try:
    print("JSON:", req.json())
except Exception:
    print("No JSON returned") 