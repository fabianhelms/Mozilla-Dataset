import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from locale import *

setlocale(LC_NUMERIC, 'French_Canada.1252')

baseurl = 'https://eatsmarter.de/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}



dataframe = pd.read_csv('find-links.csv')

alle_rezepte = []

zaehlen = 0

for link in dataframe['links']:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        name = soup.find('h1', class_ = "fn title p-name").text.strip()
    except:
        name = 'kein Name gefunden'
    try:
        parent_health_score = soup.find('span', class_='health-score-value').text.strip()
        
    
        dict = {'name': name,'health score':health_score}
        print(name)
        data.append(dict) 
        zaehlen = zaehlen + 1
        if zaehlen == 5:
            df = pd.DataFrame(data)
            df.to_csv('test2.csv', index=False)
            zaehlen = 0
    except:
        print('hallo')



df = pd.DataFrame(data)
df.to_csv('Dataset.csv',index = False)
