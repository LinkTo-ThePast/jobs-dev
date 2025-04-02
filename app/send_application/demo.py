import requests
from bs4 import BeautifulSoup


## Complete flow 'SALUD DIGNA':

## 1. Web application expected behaviour: 1) '/vacancies'; 2) pick a job from the list to obtain JOB ID ;  ----->
## 3) GET '/apply/{jobID}' to obtain "" __RequestVerificationToken "";
## 4) POST email to '/apply/{jobID} to obtain access to the form application


## 1) GET JOBS THAT MATCHES OUR USER DATABASE CHARACTERISTICS

JOB_FILTERS = {
    'keywords': ['operador', 'ayudante general', 'tecnico'],  ## TODO: refactor to automate GET ONLY the jobs that aligned with our app purpose!
    'salary': {
        'Más de $ 5,000': '5000',
        'Más de $ 10,000': '10000',
        'Más de $ 15,000': '15000',
        'Más de $ 20,000': '20000',
        'Más de $ 30,000': '30000',
    },
    
    'contractTypeList': {
        'Contrato por tiempo indeterminado': '1',
        'Contrato por obra o tiempo determinado': '2',
        'Contrato por temporada': '3',
        'Otro tipo de contrato': '4'
    },

    'IdWorkingHourList': {
        'Tiempo completo': '1',
        'Medio tiempo': '2',
        'Por horas': '3'
    },

    'deficiency': {
        'indiferente': '2',
        'si': '1',
        'no': '0'
    }

}




job_id = '7729244'
post_demo = f'https://empleos-salud-digna.pandape.computrabajo.com/Apply/{job_id}'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Referer': 'https://empleos-salud-digna.pandape.computrabajo.com/Vacancies',
    'Upgrade-Insecure-Requests': '1',
}


session = requests.Session()
get_job = session.get(post_demo, headers=headers)

if get_job.status_code == 200:
    soup = BeautifulSoup(get_job.text, 'html.parser')
    get_token = soup.find('input', attrs={'name': '__RequestVerificationToken'})
    if get_token:
        token_value = get_token['value']
        print("✅ Token found:", token_value)
    else:
        print("❌ Token not found in HTML.")
else:
    print("❌ Failed to get job page:", get_job.status_code, get_job.text)
