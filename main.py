import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
import itertools
import numpy as np
import list_list
from click import click_url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def lamoda_catalog(url):
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
                    list_list.shop_list['Название товара'] = list_list.name_list
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

def ozon_catalog(url):
    
    options = Options()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')
    
    i = 1
    while True:
        driver = webdriver.Firefox()
        URL = url+f'?page={i}'
        driver.get(URL)
        driver.maximize_window()
        #проверка капчи
        # try:
        #     if driver.find_element(By.CSS_SELECTOR, "#challenge-running").text == "Checking if the site connection is secure":
        #         print("Всё пропало, шеф!")
        #         elem1 = driver.find_element(By.CSS_SELECTOR, '.ctp-checkbox-label > input:nth-child(1)')        
        #         elem1.click()
        #         time.sleep(10)
        # except Exception:
        #     pass

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        main_page = driver.page_source
        soup = bs(main_page, 'html.parser')
        title_name = soup.find_all('div', class_='b7a ab9 ba9 vi')
        if len(title_name)>0 and i<10:
            old_price = soup.find_all('span', class_='c3118-a1 tsBodyControl400Small c3118-b0')
            new_price = soup.find_all('span', class_='c3118-a1 tsHeadline500Medium c3118-b9')
            url_name = soup.find_all('a', class_='tile-hover-target vi vi0')
            for name, old_prices, new_prices, url_names in zip(title_name, old_price, new_price, url_name):
                list_list.name_list.append(name.get_text())
                list_list.old_price_list.append(old_prices.get_text())
                list_list.new_price_list.append(new_prices.get_text())
                # сокращение ссылок
                url_name_click = list_list.LINK_DOMEN_OZON + url_names.get('href')   
                url_name_result = click_url(url_name_click)
                list_list.link_list.append(url_name_result)
                list_list.table_matrix_ozon.append([name.get_text(), old_prices.get_text(), new_prices.get_text(), url_name_result])
            
            print(tabulate(list_list.table_matrix_ozon))
            driver.quit()
            time.sleep(3)
            i+=1
        else:
            list_list.shop_list_ozon['Название товара'] = list_list.name_list
            list_list.shop_list_ozon['Старая цена'] = list_list.old_price_list
            list_list.shop_list_ozon['Новая цена'] = list_list.new_price_list
            list_list.shop_list_ozon['Ссылка на товар'] = list_list.link_list
            df = pd.DataFrame(list_list.shop_list_ozon)
            df.to_excel('shop_ozon.xlsx')
            print('Конец парсинга, кроссовок больше нет!')
            break
            time.sleep(1)
            return driver.quit()
    

def sneaker_store(url):
    r = requests.get(url)
    print(r.status_code)
    
if __name__=='__main__':
    ozon_catalog('https://www.ozon.ru/category/zhenskaya-odezhda-7501/')
else:
    print(False)

#     captcha
#   