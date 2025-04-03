import requests;
from bs4 import BeautifulSoup;
req_html = requests.get('https://empleos-salud-digna.pandape.computrabajo.com/Vacancies');

page = BeautifulSoup(req_html.text, 'html.parser');

find_all_cities = page.find_all('input', attrs={'class_': 'custom-control-input'}) ## returns a set

print(find_all_cities);