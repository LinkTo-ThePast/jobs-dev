## Building our IDEAL JOBS to our users: scrapping "ideal" jobs.

JOB_FILTERS = {
    'keywords': ['operador', 'ayudante general', 'tecnico'],  ## TODO: refactor to automate GET ONLY the jobs that aligned with our app purpose!
    
    'salary': {
        'Más de $ 5,000': '5000', ## ----> values based on 'https://empleos-salud-digna.pandape.computrabajo.com/Vacancies'
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

    'deficiency': {   ## --> users with some physical/health disability
        'indiferente': '2',
        'si': '1',
        'no': '0'
    },
}