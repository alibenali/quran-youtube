from bs4 import BeautifulSoup
import requests
from random import randint

url = input('URL: ')
ext = 'mp3'

def listFD(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

for file in reversed(listFD(url, ext)):
    print(file)
    doc = requests.get(file)
    directory = 'audios/'+str(randint(9999999999,999999999999999))+'.mp3'
    with open(directory, 'wb') as f:
        f.write(doc.content)