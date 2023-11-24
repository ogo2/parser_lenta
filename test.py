import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
import itertools
import numpy as np
import time
import csv
# Lamoda 
# https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481


def lamoda_women_sale():
    table_matrix = [['Название кроссовок', 'Старая цена', 'Новая цена', 'Ссылка на товар']]
    shop_list = {'Название кроссовок': [],
                    'Старая цена': [],
                    'Новая цена': [],
                    'Ссылка на товар': []}
    old_price_list = []
    new_price_list = []
    link_list = []
    name_list = []
    i = 1
    while True:
        URL_TEMPLATE = f'https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481&page={i}'
        r = requests.get(URL_TEMPLATE)
        try:
            if r.status_code == 200:
                soup = bs(r.text, 'html.parser')
                # title
                title_name = soup.find_all('div', class_='x-product-card-description__product-name')
                if len(title_name)>0:
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
                        name_list.append(name.get_text())
                        old_price_list.append(old_prices.get_text())
                        new_price_list.append(new_prices.get_text())
                        url_name_result = LINK_DOMEN + url_names.get('href')   
                        link_list.append(url_name_result)
                        table_matrix.append([name.get_text(), old_prices.get_text(), new_prices.get_text(), url_name_result])
                    print(tabulate(table_matrix))
                    i += 1
                    time.sleep(2)
                else:
                    shop_list['Название кроссовок'] = name_list
                    shop_list['Старая цена'] = old_price_list
                    shop_list['Новая цена'] = new_price_list
                    shop_list['Ссылка на товар'] = link_list
                    df = pd.DataFrame(shop_list)
                    df.to_excel('sneakers.xlsx')
                    print('Конец парсинга, кроссовок больше нет!')
                    break
            else:
                print(r.status_code+'\nОшибка. \тКонец парсинга!')
                break
        except Exception:
            print('Конец парсинга, ошибка!')
            break
    
if __name__=='__main__':
    lamoda_women_sale()
else:
    print(False)
    
  