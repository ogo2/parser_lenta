import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
import itertools
import numpy as np
import time
import list_list
from click import click_url
# Lamoda 
# https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481


def lamoda_women_sale(url):
    i = 1
    while True:
        URL_TEMPLATE = url+f'&page={i}'
        r = requests.get(URL_TEMPLATE)
        
        try:
            if r.status_code == 200:
                soup = bs(r.text, 'html.parser')
                # title 
                title_name = soup.find_all('div', class_='x-product-card-description__product-name')
                if len(title_name)>0 and i<2:
                    # old_price
                    old_price = soup.find_all('span', class_='x-product-card-description__price-old')
                    #brand
                    brand = soup.find_all('div', class_='x-product-card-description__brand-name')
                    # new_price
                    new_price = soup.find_all('span', class_='x-product-card-description__price-new')
                    # img
                    img_link = soup.find_all('img', class_='x-product-card__pic-img')
                    # url
                    url_name = soup.find_all('a', class_='x-product-card__link x-product-card__hit-area')
                    LINK_IMG = 'https:'
                    LINK_DOMEN = 'https://www.lamoda.ru'
                    for name, old_prices, new_prices, url_names, brand_names in zip(title_name, old_price, new_price, url_name, brand, strict=False):
                        list_list.name_list.append(name.get_text())
                        list_list.old_price_list.append(old_prices.get_text())
                        list_list.brand_list.append(brand_names.get_text())
                        list_list.new_price_list.append(new_prices.get_text())
                        # сокращение ссылок
                        url_name_click = LINK_DOMEN + url_names.get('href')   
                        url_name_result = click_url(url_name_click)
                        
                        list_list.link_list.append(url_name_result)
                        list_list.table_matrix.append([name.get_text(), brand_names.get_text(), old_prices.get_text(), new_prices.get_text(), url_name_result])
                    print(tabulate(list_list.table_matrix))
                    i += 1
                    print(i)
                    time.sleep(2)
                else:
                    list_list.shop_list['Название кроссовок'] = list_list.name_list
                    list_list.shop_list['Брeнд'] = list_list.brand_list
                    list_list.shop_list['Старая цена'] = list_list.old_price_list
                    list_list.shop_list['Новая цена'] = list_list.new_price_list
                    list_list.shop_list['Ссылка на товар'] = list_list.link_list
                    df = pd.DataFrame(list_list.shop_list)
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
    lamoda_women_sale('https://www.lamoda.ru/c/4152/default-men/?labels=36914&display_locations=all&sf=235&ad_id=909823')
else:
    print(False)
    
  