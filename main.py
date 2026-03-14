import requests
from bs4 import BeautifulSoup

def scrape_data(url, tag):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all(tag)
    for el in elements:
        print(el.text.strip())
