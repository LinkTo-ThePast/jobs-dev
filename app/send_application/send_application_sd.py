
## Flow simulating browser session!

## 1. get cookies
JOB_URl = "https://empleos-salud-digna.pandape.computrabajo.com/Detail/7729244"


## 2. mimic the data structure required for the payload ----> needs refactor!

experience_id = str(uuid.uuid4())
study_id = str(uuid.uuid4())
skill_id1 = str(uuid.uuid4())
skill_id2 = str(uuid.uuid4())
skill_id3 = str(uuid.uuid4())

payload = {
    "PhotoArray": "",
    "IdVacancy": 9180489,
    "IsVacancyDeficiencyRequired": False,
    "IdPortal": 2,
    "IdApplyMethodType": 1,
    "ConfirmedEmail": "",
    "Email": "Luis_Rivera1007@hotmail.com",
    "Name": "Luis",
    "Surname": "Juárez Rivera",
    "BirthDate": "07/10/1999",
    "IdNationality": 139,
    "IdIdentificationDocumentType": 1,
    "IsRequiredCPF": False,
    "CPF": "",
    "IdSex": 1,
    "IdChildren": 3,
    "IdMaritalStatus": 1,
    "PrefixPhone": "52",
    "Phone": "5534420656",
    "PrefixPhone2": "52",
    "Phone2": "5534420656",
    "IdSkype": "",
    "IdLocation1": 139,
    "selectPostalCode": "193770",
    "IdPostalCode": 193770,
    "Latitude": "19,25452708",
    "Longitude": "-98,89607808",
    "CEP": "56600",
    "IdLocation1": 139,
    "IdLocation2": 16,
    "IdLocation3": 681,
    "IdLocation4": "",
    "IdLocation5": "",
    "Address": "Cerrada Felipe Ángeles Número",
    "AddressNumber": "7",
    "AddressComplement": "",
    
    # Deficiencies (structured as they appear in the original payload)
    "Deficiencies.Index": [0, 1, 2, 3, 4, 5, 6],
    "Deficiencies[0].Deficiencies2.Index": [0, 1, 2, 3, 4],
    "Deficiencies[1].Deficiencies2.Index": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "Deficiencies[3].Deficiencies2.Index": [0, 1, 2, 3, 4, 5, 6, 7],
    "Deficiencies[6].Deficiencies2.Index": [0, 1],
    "DeficiencyPercentage": "",
    "DeficiencyInformation": "",
    
    "Job": "Desarrollador",
    "Summary": "Web dev experience.",
    "PreferredJob": "Desarrollador",
    
    # Experiences
    f"Experiences.index": experience_id,
    f"Experiences[{experience_id}].IdPortal": 2,
    f"Experiences[{experience_id}].Job": "Programador de aplicaciones",
    f"Experiences[{experience_id}].Company": "TELMEX",
    f"Experiences[{experience_id}].Salary": "",
    f"Experiences[{experience_id}].IdJob": 307,
    f"Experiences[{experience_id}].IdCategory1": 4,
    f"Experiences[{experience_id}].BeginDate": "01/04/2025",
    f"Experiences[{experience_id}].EndDate": "19/04/2025",
    f"Experiences[{experience_id}].CurrentlyWorking": False,
    f"Experiences[{experience_id}].Description": "PROGRAMAR web apps",
    
    # Studies
    f"Studies.index": study_id,
    f"Studies[{study_id}].IdPortal": 2,
    f"Studies[{study_id}].Study": "Prepa",
    f"Studies[{study_id}].IdStudy1": 3,
    f"Studies[{study_id}].Center": "ENP 3",
    f"Studies[{study_id}].StudyStatus": "Finished",
    f"Studies[{study_id}].BeginDate": "28/01/2015",
    f"Studies[{study_id}].EndDate": "01/08/2018",
    
    # Skills
    "Skills.index": [skill_id1, skill_id2, skill_id3],
    f"Skills[{skill_id1}].Skill": "comunicacion",
    f"Skills[{skill_id2}].Skill": "python",
    f"Skills[{skill_id3}].Skill": "bases de datos",
    
    "SalaryMin": 10000,
    "SalaryMax": 15000,
    "IdWorkingHour": 1,
    "IdContractWorkType": 1,
    "HasAcceptedTerms": True,
    "HasAcceptedIJInformation": True,
    "__RequestVerificationToken": "CfDJ8JPLgbr0W8hJnxPpFJDQtcnRfRqgxM-61cBrmRoxgbcfWA1XzO2XowcJZXwAhr_erQC8hhdyw_SPsZPnHEmOq9OYqjtAFTKSjsh41glSIaB-VWjcTD3RaJIZsATqv_u2B25BL8kscam73008VfMSVgo",
    "AddressWithoutNumber": False,
    "HasDeficiency": False,
    "HasConsentUsePersonalData": False,
    "Travel": False,
    "ChangeResidence": False,
    "HasAcceptedTerms": False,
    "HasAcceptedIJInformation": False
}
