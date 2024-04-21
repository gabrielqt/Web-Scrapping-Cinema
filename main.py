from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
os.system('cls')
count = 0

print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
print()
print('    \033[34mCONSULTA DE FILMES E SÉRIES\033[m')  
print()
print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
print()
print('\033[34m1 - Detalhes sobre algum filme/série')
print('2 - Opção 1 + gerar excel')
print('3 - Comparar nota de dois filmes ou séries')
print('4 - Top 10 mais populares atualmente')
print('5 - Consultar ator')
print('6 - SAIR.\033[m')
print()

user = int(input('Digite a opção: '))



if user == 4:
    
    driver = webdriver.Firefox()
    driver.get('https://www.imdb.com/chart/moviemeter/')
    driver.minimize_window()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find_all('li', attrs = {'class': 'ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent'})
    driver.quit()
    
    for movie in movies:
        
        count += 1
        if count == 11:
            break
        title = movie.find('h3').get_text()
        details = movie.find('div', attrs = {'class': 'sc-b189961a-7 feoqjK cli-title-metadata'}).get_text()
        rating = movie.find('div', attrs = {'class': 'sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP cli-ratings-container'}).get_text()
        
        
        print(f'{count} - {title}')
        print(f'Year: {details[0:4]}   Duration: {details[4:10]}   Minimal Age: {details[10:]} ')
        print(f'Rating: {rating[:4]}⭐')
        print()
        