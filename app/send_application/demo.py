import requests
from bs4 import BeautifulSoup

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
