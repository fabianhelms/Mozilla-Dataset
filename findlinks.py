from bs4 import BeautifulSoup
import lxml
import pandas as pd
from selenium import webdriver
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://eatsmarter.de/suche/rezepte?op=Suchen')
time.sleep(20)


search1 = driver.find_element_by_id('edit-ft')
search1.send_keys('Mittagessen')
search2 = driver.find_element_by_id('edit-submit-container')
search2.click()

lala = driver.find_elements_by_class_name('teaser-wrapper-link')
links = []
for ii in lala:
    links.append(ii.get_attribute('href'))



xpath_links = []

for x in range(2,9):
    text = '/html/body/div[6]/div/div[2]/div[5]/div/div[1]/div/div/div[1]/div/div[5]/div[26]/ul/li['
    ganzer_xpath = text + str(x) + ']'
    xpath_links.append(ganzer_xpath)

search4 = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div/div[1]/div/div/div[1]/div/div[5]/div[26]/ul/li[2]')
time.sleep(5)
   
search4.click()
time.sleep(5)
lala = driver.find_elements_by_class_name('teaser-wrapper-link')
for ii in lala:
    links.append(ii.get_attribute('href'))
    print(ii)



for z in range(197):

    try:
        search4 = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[5]/div/div[1]/div/div/div[1]/div/div[5]/div[26]/ul/li[8]')
        time.sleep(5)
        search4.click()
        time.sleep(5)
        lala = driver.find_elements_by_class_name('teaser-wrapper-link')
        for ii in lala:
            links.append(ii.get_attribute('href'))
        print('es hat geklappt')
    except:
        print('es hat nicht geklappt')



df = pd.DataFrame(links,columns=['links'])
print(df)
df.to_csv('find-links.csv',index = False)
