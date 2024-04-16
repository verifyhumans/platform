import requests
import openai 
import random

from bs4 import BeautifulSoup

response = requests.get (
    url = ""
)

soup = BeautifulSoup(response.content, 'html.parser')


title = soup.find(id="firstHeading")
print(response.status.code)

