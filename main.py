from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

def get_imdb_rating():
    
    infomovie = BeautifulSoup(driver.page_source, 'html.parser')
    
    ratings = infomovie.find_all('div', {'class': 'jw-scoring-listing__rating'})
    for rating in ratings:
        count += 1
        if count ==2:
            imdb = rating.get_text()
    imdb = imdb.split()
    imdb = imdb[0]
    return imdb



count = 0

os.system('cls')
count = 0
    
print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
print()
print('    \033[34mCONSULTA DE FILMES E SÉRIES\033[m')  
print()
print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
print()
print('\033[34m1 - Detalhes sobre algum filme/série')
print('2 - Comparar nota de dois filmes ou séries')
print('3 - Top 10 mais populares atualmente')
print('4 - Consultar ator')
print('5 - SAIR.\033[m')
print()

user = int(input('Digite a opção: '))


if user == 1:
    
    ########### GETING THE MOVIE AND SEARCHING FOR HIM
    
    title = str(input('Digite o título do filme/série que deseja saber mais: '))
    driver = webdriver.Firefox()
    driver.get('https://www.justwatch.com/')
    driver.minimize_window
    sleep(2)
    search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div/div[2]/div[1]/div[1]/ion-searchbar/div/input')))
    search.click()
    sleep(2)
    search.send_keys(title)
    sleep(1)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-result-item__details'))).click()
    sleep(1)
    
    ############   GETTING THE DATA       ##############
    
    infomovie = BeautifulSoup(driver.page_source, 'html.parser')
    
    
    
    actors = infomovie.find_all('span', attrs = {'class': 'title-credit-name'})
    actorslist = list()
    for actor in actors:
        actorslist.append(actor.get_text())
        
    imdb = get_imdb_rating()
    
    title = infomovie.find('div', {'data-testid':"titleBlock"})
    title = title.get_text()
    
    
    print(infomovie.find(By.XPATH,'/html/body/div/div[4]/div/div[2]/div/div[2]/div[2]/article/div').get_text())
    
    ############ I GOT THE DATA, I JUST NEED TO SHOW IT MORE PRETTY      ##############
    
    
if user == 3:
    
    driver = webdriver.Firefox()
    driver.get('https://www.imdb.com/chart/moviemeter/')
    driver.minimize_window()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find_all('li', attrs = {'class': 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent'})
    
    
    dados = []
    
    for movie in movies:
        
        count += 1
        if count == 11:
            break
        title = movie.find('h3').get_text()
        details = movie.find('div', attrs = {'class': 'sc-b189961a-7 feoqjK cli-title-metadata'}).get_text()
        rating_ = movie.find('div', attrs = {'class': 'sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container'}).get_text()
        
        year,duration,minimalage,rating = details[0:4], details[4:10], details[10:], rating_[:4]
        
        dados.append([title,duration,minimalage,rating])
        
        print(f'{count} - {title}')
        print(f'Year: {year}   Duration: {duration}   Minimal Age: {minimalage} ')
        print(f'Rating: {rating}⭐')
        print()
    
    xlsx = str(input('Gerar Excel? [S] | [N]')).lower().strip()
    if xlsx == 's':
        data = pd.DataFrame(dados,columns=['Title','Duration','MinimalAge','Rating'])
        data.to_excel('top10.xlsx',index=False)
        print('Excel Criado!')
        os.system('start top10.xlsx')