import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
import itertools
import numpy as np

# Lamoda 
# https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481

table_matrix = [['Название кроссовок', 'Старая цена', 'Новая цена', 'Ссылка на товар']]


URL_TEMPLATE = 'https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481'

r = requests.get(URL_TEMPLATE)

if r.status_code == 200:
    soup = bs(r.text, 'html.parser')
    # title
    title_name = soup.find_all('div', class_='x-product-card-description__product-name')
    # old_price
    old_price = soup.find_all('span', class_='x-product-card-description__price-old')
    # new_price
    new_price = soup.find_all('span', class_='x-product-card-description__price-new')
    # img
    img_link = soup.find_all('img', class_='x-product-card__pic-img')
    # url
    url_name = soup.find_all('a', class_='x-product-card__link x-product-card__hit-area')
    LINK_IMG = 'https:'
    LINK_DOMEN = 'https://www.lamoda.ru'
    for name, old_prices, new_prices, url_names in zip(title_name, old_price, new_price, url_name, strict=False):
        
        url_name_result = LINK_DOMEN + url_names.get('href')   
        table_matrix.append([name.get_text(), old_prices.get_text(), new_prices.get_text(), url_name_result])
            
        
    print(tabulate(table_matrix))
else:
    print(r.status_code)
    
    
if __name__=='__main__':
    print(True)
else:
    print(False)
    
  