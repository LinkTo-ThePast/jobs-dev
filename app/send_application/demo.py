import requests
from bs4 import BeautifulSoup


## Complete flow 'SALUD DIGNA':

## 1. Web application expected behaviour: 1) '/vacancies'; 2) pick a job from the list to obtain JOB ID ;  ----->
## 3) GET '/apply/{jobID}' to obtain "" __RequestVerificationToken "";
## 4) POST email to '/apply/{jobID} to obtain access to the form application


## 1) GET JOBS THAT MATCHES OUR USER DATABASE CHARACTERISTICS: SD/get_jobs.py

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
    },
}




job_id = '9110251';
post_demo = f'https://empleos-salud-digna.pandape.computrabajo.com/Apply/{job_id}'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Referer': 'https://empleos-salud-digna.pandape.computrabajo.com/Vacancies',
    'Upgrade-Insecure-Requests': '1',
}


paylodad_to_access_email = {
'actionFrom': 'SetEmail',
'requireLoginCt': 'false',
'IdVacancy': job_id,
'Email': 'Luis_Rivera1007@hotmail.com',
'__RequestVerificationToken': ""    
}

paylodad_to_access_form = {
    "PhotoArray": "",
    "IdVacancy": job_id,
    "IsVacancyDeficiencyRequired": False,
    "IdPortal": 2,
    "IdApplyMethodType": 1,
    "ConfirmedEmail": "",
    "Email": "Luis_Rivera1007@hotmail.com",
    "Name": "José Luis",
    "Surname": "Juárez Rivera",
    "BirthDate": "07/10/1999",
    "IdNationality": 139,
    "IdIdentificationDocumentType": 1,
    "IsRequiredCPF": False,
    "CPF": "",
    "IdSex": 1,
    "IdChildren": 3,
    "IdMaritalStatus": 1,
    "PrefixPhone": 52,
    "Phone": 5534420656,
    "PrefixPhone2": 52,
    "Phone2": 5534420656,
    "IdSkype": "",
    "IdLocation1": 139,
    "selectPostalCode": 193770,
    "IdPostalCode": 193770,
    "Latitude": "19,25452708",
    "Longitude": "-98,89607808",
    "CEP": 56600,
    "IdLocation1": 139,
    "IdLocation2": 16,
    "IdLocation3": 681,
    "IdLocation4": "",
    "IdLocation5": "",
    "Address": "Cerrada Felipe Ángeles Número",
    "AddressNumber": 7,
    "AddressComplement": "",
    "Deficiencies.Index": 0,
    "Deficiencies[0].Deficiencies2.Index": 0,
    "Deficiencies[0].Deficiencies2.Index": 1,
    "Deficiencies[0].Deficiencies2.Index": 2,
    "Deficiencies[0].Deficiencies2.Index": 3,
    "Deficiencies[0].Deficiencies2.Index": 4,
    "Deficiencies.Index": 1,
    "Deficiencies[1].Deficiencies2.Index": 0,
    "Deficiencies[1].Deficiencies2.Index": 1,
    "Deficiencies[1].Deficiencies2.Index": 2,
    "Deficiencies[1].Deficiencies2.Index": 3,
    "Deficiencies[1].Deficiencies2.Index": 4,
    "Deficiencies[1].Deficiencies2.Index": 5,
    "Deficiencies[1].Deficiencies2.Index": 6,
    "Deficiencies[1].Deficiencies2.Index": 7,
    "Deficiencies[1].Deficiencies2.Index": 8,
    "Deficiencies[1].Deficiencies2.Index": 9,
    "Deficiencies[1].Deficiencies2.Index": 10,
    "Deficiencies[1].Deficiencies2.Index": 11,
    "Deficiencies[1].Deficiencies2.Index": 12,
    "Deficiencies[1].Deficiencies2.Index": 13,
    "Deficiencies[1].Deficiencies2.Index": 14,
    "Deficiencies.Index": 2,
    "Deficiencies.Index": 3,
    "Deficiencies[3].Deficiencies2.Index": 0,
    "Deficiencies[3].Deficiencies2.Index": 1,
    "Deficiencies[3].Deficiencies2.Index": 2,
    "Deficiencies[3].Deficiencies2.Index": 3,
    "Deficiencies[3].Deficiencies2.Index": 4,
    "Deficiencies[3].Deficiencies2.Index": 5,
    "Deficiencies[3].Deficiencies2.Index": 6,
    "Deficiencies[3].Deficiencies2.Index": 7,
    "Deficiencies.Index": 4,
    "Deficiencies.Index": 5,
    "Deficiencies.Index": 6,
    "Deficiencies[6].Deficiencies2.Index": 0,
    "Deficiencies[6].Deficiencies2.Index": 1,
    "DeficiencyPercentage": "",
    "DeficiencyInformation": "",
    "SocialNetworks.index": "b332b28e-f12c-4c3d-8ee0-88c6a0d301ed",
    "SocialNetworks[b332b28e-f12c-4c3d-8ee0-88c6a0d301ed].IdSocialNetwork": 1,
    "SocialNetworks[b332b28e-f12c-4c3d-8ee0-88c6a0d301ed].Url": "https://mx.linkedin.com/in/aluisttp",
    "Job": "Desarrollador",
    "Summary": "Experto en carpinteria.",
    "PreferredJob": "Tecnico en carpinteria",
    "Experiences.index": "c16653d1-1f57-4169-a5aa-9fbd459a84af",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].IdPortal": 2,
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].Job": "Desarrollador Full stack",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].Company": "Entropía",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].Salary": "",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].IdJob": "",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].IdCategory1": 4,
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].BeginDate": "15/01/2025",
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].CurrentlyWorking": True,
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].CurrentlyWorking": False,
    "Experiences[c16653d1-1f57-4169-a5aa-9fbd459a84af].Description": "Desarrollo de aplicaciones web.\nDesarollo de agentes de IA.\nDesarollo de pipe lines.",
    "Experiences.index": "78559a1e-d675-4851-b03d-f8bf250cee34",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].IdPortal": 2,
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].Job": "Java Support engineer",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].Company": "Santander",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].Salary": "",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].IdJob": "",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].IdCategory1": 4,
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].BeginDate": "10/09/2024",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].EndDate": "10/01/2025",
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].CurrentlyWorking": False,
    "Experiences[78559a1e-d675-4851-b03d-f8bf250cee34].Description": "Servidores Oracle: soporte, debuggeo y tareas DevOps.\nBases de datos: normalización, reporteo y construcción de flujos.\nTareas de desarrollo: microservicios de mensajería del banco.\nSoporte: resolución de problemas en todas las área de mensajería del Banco.",
    "Studies.index": "a0b93737-1484-4dac-8ff9-bfca9baa3da2",
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].IdPortal": 2,
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].Study": "Ingeniería en Ciencia de Datos",
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].IdStudy1": 7,
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].Center": "UNAM",
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].StudyStatus": "Finished" ,
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].BeginDate": "21/08/2017",
    "Studies[a0b93737-1484-4dac-8ff9-bfca9baa3da2].EndDate": "19/05/2023",
    "Languages.index": "369478a0-dc46-4443-9d5b-2b2bd63e043e",
    "Languages[369478a0-dc46-4443-9d5b-2b2bd63e043e].IdLanguage": 77,
    "Languages[369478a0-dc46-4443-9d5b-2b2bd63e043e].IdLanguageLevel": 4,
    "Skills.index": "a59c57b1-f339-4539-b514-62c1121350b4",
    "Skills[a59c57b1-f339-4539-b514-62c1121350b4].Skill": "Python",
    "Skills.index": "b50bed19-7575-4e56-b8a8-d04b28453052",
    "Skills[b50bed19-7575-4e56-b8a8-d04b28453052].Skill": "Javascript",
    "Skills.index": "7cbfca4b-ed65-4857-93f8-7ae6158bd457",
    "Skills[7cbfca4b-ed65-4857-93f8-7ae6158bd457].Skill": "React",
    "Skills.index": "9ba25abf-3ff0-4f00-a294-2ae798bd263c",
    "Skills[9ba25abf-3ff0-4f00-a294-2ae798bd263c].Skill": "C#",
    "Skills.index": "2394a8d9-8364-4ac7-ac5e-ebe98004dafd",
    "Skills[2394a8d9-8364-4ac7-ac5e-ebe98004dafd].Skill": "Java",
    "Skills.index": "6f589622-28f0-48c7-adae-c608fb3b8f32",
    "Skills[6f589622-28f0-48c7-adae-c608fb3b8f32].Skill": "Microsoft Office",
    "SalaryMin": 14000,
    "SalaryMax": 17000,
    "IdWorkingHour": 1,
    "IdContractWorkType": 1,
    "HasAcceptedIJInformation": True,
    "__RequestVerificationToken": "",
    "AddressWithoutNumber": False,
    "HasDeficiency": False,
    "HasConsentUsePersonalData": False,
    "Travel": False,
    "ChangeResidence": False,
    "HasAcceptedTerms": False,
    "HasAcceptedIJInformation": False
}


session = requests.Session()
get_job = session.get(post_demo, headers=headers)

if get_job.status_code == 200:
    soup = BeautifulSoup(get_job.text, 'html.parser')
    get_token = soup.find('input', attrs={'name': '__RequestVerificationToken'})
    if get_token:
        token_value = get_token['value']
        print("✅ Token found:", token_value);
        paylodad_to_access_email["__RequestVerificationToken"] = token_value;
        get_job_submit_email = session.post(post_demo, data=paylodad_to_access_email, headers=headers);
        if get_job_submit_email.status_code == 200:
          soup_two = BeautifulSoup(get_job_submit_email.text, 'html.parser');
          get_token_two = soup_two.find('input', attrs={'name': '__RequestVerificationToken'});  
          if get_token_two:
            token_value_two = get_token_two['value'];
            print("✅ Token found:", token_value_two);
            paylodad_to_access_form["__RequestVerificationToken"] = token_value_two;
            get_job_submit_email = session.post(post_demo, data=paylodad_to_access_form, headers=headers);
            print(get_job_submit_email.status_code);

    else:
        print("☠️ Token not found in HTML.")
else:
    print("☠️ Failed to get job page:", get_job.status_code, get_job.text)
