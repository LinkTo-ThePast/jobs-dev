import requests;
from bs4 import BeautifulSoup;
## Get JOBS according to user input. => {ProfileModel: name, }

def get_jobs_(filters=None):
  SK_URL = 'https://www.sukarne.com/en/vacante';
  sk_html = requests.get(SK_URL)