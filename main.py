import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate
import csv
import itertools
import numpy as np
import list_list
from click import click_url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import delete_text
import db

# options = Options()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')
# driver = webdriver.Chrome()
class ShopoTam:
    def shopotam_catalog():
        o = 1
        while True:
            r = requests.get(f'https://shopotam.ru/r-mens-sports-shoes/sale?page={o}')
            soup = bs(r.text, 'html.parser')
            
            title_name = soup.find_all('div', class_='product-listing-card-info control-200 tablet-small:control-350 weight-medium product-listing-card-info_line-clamp_2')
            if len(title_name)>0 and o<2:
                old_price = soup.find_all('s', class_='product-listing-card-prices__old-price control-200 tablet-small:control-250 weight-heavy')
                new_price = soup.find_all('span', class_='product-listing-card-prices__price control-350 tablet-small:control-600 weight-heavy product-listing-card-prices__price_profit')
                img_link = soup.find_all('img', class_='product-listing-card__image')
                url_name = soup.find_all('a', class_='product-listing-card__preview-link')
                brand = soup.find_all('div', class_='product-listing-card-info control-150 tablet-small:control-250 weight-heavy product-listing-card-info_line-clamp_1')
                LINK_DOMEN = 'https://shopotam.ru'
                for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
                    list_list.name_list.append(name.attrs['title'])
                    list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                    list_list.brand_list.append(brand_names.attrs['title'])
                    list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                    
                    url_img_click = img_link.get('src')
                    url = LINK_DOMEN + url_names.get('href')
                    list_list.link_list.append(url)
                    
                    list_list.link_img_list.append(url_img_click)
                    list_list.table_matrix.append([name.attrs['title'], brand_names.attrs['title'], old_prices.get_text(), new_prices.get_text(), url, url_img_click])
                print(tabulate(list_list.table_matrix))
                o += 1
                time.sleep(1)
            else:
                break
        list_list.shop_list['Название товара'] = list_list.name_list
        list_list.shop_list['Брeнд'] = list_list.brand_list
        list_list.shop_list['Старая цена'] = list_list.old_price_list
        list_list.shop_list['Новая цена'] = list_list.new_price_list
        list_list.shop_list['Ссылка на товар'] = list_list.link_list
        list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
        df = pd.DataFrame(list_list.shop_list)
        df.to_excel('sneakers.xlsx')
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            for i in range(len(name)):
                if name[i] == "'":
                    name = name.replace("'", "`")
                    print(name)
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'man', brand_names)
            print('Good add db!', name)
        print('Конец!')
        
        
class StreetBeat:
    def streetbeat_catalog(self, sex: str):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            # 'Cookie': 'ipp_sign=274a385fbb1f0602f5c592e5a720692d_952849163_b2ba8819de3df2046d266cbeb2f00660; ipp_uid=1705301453537/t3c5hlhtTveYl9kR/YJuaqxuG+hZo0pT2142rDQ==; rerf=AAAAAGWk1dslKC7ABS3wAg==; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BX_USER_ID=235f63a86f2040bf5da5058c6aa3f2f9; _gid=GA1.2.267980212.1705301469; _ym_uid=170530147038501009; _ym_d=1705301470; tmr_lvid=67b3c6066b2c3281887a3b110fd16df2; tmr_lvidTS=1705301469527; adrcid=Aar6u6XO0tC0dvwfeZ4xudg; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; mainpagetype=man; user_usee=a%3A1%3A%7Bi%3A0%3Bs%3A7%3A%223723666%22%3B%7D; PHPSESSID=HyOTwUSOug77xc3LLpHsnAOH6r7M4wQ4; ipp_key=v1705476719672/v33947245ba5adc7a72e273/cz2XKJMlk6boNUTp4H+29Q==; topMenu_active=%2Fman%2F; _ym_isad=2; _ym_visorc=b; _ga=GA1.1.330262409.1705301469; mindboxDeviceUUID=f3f59a7f-4af4-47d9-bf6d-8163f11ec92f; directCrm-session=%7B%22deviceGuid%22%3A%22f3f59a7f-4af4-47d9-bf6d-8163f11ec92f%22%7D; tmr_detect=0%7C1705477958551; _ga_E3GN5VV3T0=GS1.1.1705476722.8.1.1705478065.59.0.0',
            'Origin': 'https://street-beat.ru',
            'Pragma': 'no-cache',
            'Referer': f'https://street-beat.ru/cat/{sex}/obuv/krossovki/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        y = 1
        while True:
            json_data = {
                'pagination': {
                    'page': y,
                },
                'sorting': {
                    'key': 'sort',
                    'value': 'desc',
                },
                'seo': {
                    'uri': f'/cat/{sex}/obuv/krossovki/sale/',
                },
                'search': '',
            }
            response = requests.post('https://street-beat.ru/api/catalog/page', headers=headers, json=json_data)
            data = response.json()
            if not data['catalog']['listing']['items']:
                break
            else:
                print('---------------------------------------------------------------',y,'-----------------------------------------------------------------')
                try:
                    for i in data['catalog']['listing']['items']:
                        name = i['title']
                        old_price = i['price']['recommended']['price']
                        brand = i['brand']
                        new_price = i['price']['special']['price']
                        f = i['url']
                        url_img = i['image']['main']['desktop']    
                        url = f'https://street-beat.ru{f}'
                        
                        list_list.name_list.append(name)
                        list_list.old_price_list.append(old_price)
                        list_list.brand_list.append(brand)
                        list_list.new_price_list.append(new_price)
                        list_list.link_list.append(url)
                        list_list.link_img_list.append(url_img)
                        list_list.table_matrix.append([name, brand, old_price, new_price, url, url_img])
                    print(tabulate(list_list.table_matrix))
                    y += 1
                    time.sleep(2)
                except Exception:
                    print('Закончился товар!')
                    break
        list_list.shop_list['Название товара'] = list_list.name_list
        list_list.shop_list['Брeнд'] = list_list.brand_list
        list_list.shop_list['Старая цена'] = list_list.old_price_list
        list_list.shop_list['Новая цена'] = list_list.new_price_list
        list_list.shop_list['Ссылка на товар'] = list_list.link_list
        list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
        df = pd.DataFrame(list_list.shop_list)
        df.to_excel('sneakers.xlsx')
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            db.add_product(name, img_link, new_prices, old_prices, url_names, sex, brand_names)
            print('Good add db!')

    
class SuperStep:
    def superstep_catalog(self, url: str):
        i = 1
        while True:
            URL_TEMPLATE = url+f'?PAGEN_1={i}'
            r = requests.get(URL_TEMPLATE)
            if r.status_code == 200:
                soup = bs(r.text, 'html.parser')
                title_name = soup.select('div:nth-child(2) > p:nth-child(1) > a:nth-child(1)')
                if len(title_name)>0 and i<26:
                    old_price = soup.find_all('span', class_='product-list-price')
                    new_price = soup.find_all('span', class_='product-sale-price')
                    img_link = soup.find_all('img', class_='product-item-image product-item-image_first')
                    url_name = soup.find_all('a', class_='cur_p js-catalog-card-click')
                    brand = soup.find_all('a', class_='js-catalog-card-click')

                    LINK_IMG = 'https://superstep.ru'
                    LINK_DOMEN = 'https://superstep.ru'
                    
                    for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
                        if name.contents[1].get_text() == '':
                            list_list.name_list.append(name.contents[2].get_text())
                        else:
                            list_list.name_list.append(name.contents[1].get_text())
                        list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                        list_list.brand_list.append(name.contents[0].get_text().strip())
                        list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                        # сокращение ссылок
                        url_name_click = LINK_DOMEN + url_names.get('href')   
                        # url_name_result = click_url(url_name_click)
                        url_img_click = LINK_IMG + img_link.get('src')
                        # url_img_result = click_url(url_img_click)
                        list_list.link_list.append(url_name_click)
                        list_list.link_img_list.append(url_img_click)
                        if name.contents[1].get_text() == '':
                            list_list.table_matrix.append([name.contents[2].get_text(), name.contents[0].get_text(), old_prices.get_text(), new_prices.get_text(), url_name_click, url_img_click])
                        else:
                            list_list.table_matrix.append([name.contents[1].get_text(), name.contents[0].get_text(), old_prices.get_text(), new_prices.get_text(), url_name_click, url_img_click])
                        
                    print(tabulate(list_list.table_matrix))
                    i += 1
                else:
                    list_list.shop_list['Название товара'] = list_list.name_list
                    list_list.shop_list['Брeнд'] = list_list.brand_list
                    list_list.shop_list['Старая цена'] = list_list.old_price_list
                    list_list.shop_list['Новая цена'] = list_list.new_price_list
                    list_list.shop_list['Ссылка на товар'] = list_list.link_list
                    list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
                    df = pd.DataFrame(list_list.shop_list)
                    df.to_excel('sneakers.xlsx')
                    print(404)
                    break
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'men', brand_names)
        print('Больше нет страниц!')
        
class BrandShop:
    def brandshop_catalog(self, url: str):
        
        i = 1
        while True:
            
            URL_TEMPLATE = url+f'&page={i}'
            r = requests.get(URL_TEMPLATE)
            driver = webdriver.Firefox()
            driver.get(URL_TEMPLATE)
            driver.maximize_window()
            for f in range(100):
                driver.execute_script("window.scrollBy(0, 100);")
                time.sleep(0.1) 
            main_page = driver.page_source

            driver.quit()
            if r.status_code == 200:
                soup = bs(main_page, 'html.parser')
               
                title_name = soup.find_all('div', class_='product-card__title')
                if len(title_name)>0 and i<6:
                    old_price = soup.find_all('span', class_='product-card__price_old')
                    new_price = soup.find_all('div', class_='product-card__price_new')
                    # img_link = soup.find_all('img', class_='lazyLoad')
                    # img_link = soup.find_all('img', zclass_='lazyLoad isLoaded')
                    img_link = soup.select('div:nth-child(1) > div:nth-child(1) > picture:nth-child(1) > img:nth-child(1)')
                    url_name = soup.find_all('a', class_='product-card__link')
                    brand = soup.find_all('div', class_='product-card__title')

                    LINK_IMG = 'https:'
                    LINK_DOMEN = 'https://brandshop.ru'
                    
                    for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
                        list_list.name_list.append(name.contents[2].get_text().strip())
                        list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                        brand_names = brand_names.contents[0].strip()
                        list_list.brand_list.append(brand_names)
                        list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                        # сокращение ссылок
                        url_name_click = LINK_DOMEN + url_names.get('href')   
                        # url_name_result = click_url(url_name_click)
                        
                        url_img_click = img_link.get('src')
                        # url_img_result = click_url(url_img_click)
                        
                        list_list.link_list.append(url_name_click)
                        list_list.link_img_list.append(url_img_click)
                        list_list.table_matrix.append([name.contents[2].get_text().strip(), brand_names, old_prices.get_text(), new_prices.get_text(), url_name_click, url_img_click])
                    print(tabulate(list_list.table_matrix))
                    i += 1
                else:
                    list_list.shop_list['Название товара'] = list_list.name_list
                    list_list.shop_list['Брeнд'] = list_list.brand_list
                    list_list.shop_list['Старая цена'] = list_list.old_price_list
                    list_list.shop_list['Новая цена'] = list_list.new_price_list
                    list_list.shop_list['Ссылка на товар'] = list_list.link_list
                    list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
                    df = pd.DataFrame(list_list.shop_list)
                    df.to_excel('sneakers.xlsx')
                    print('Конец парсинга, кроссовок больше нет!')
                    break
            else:
                list_list.shop_list['Название товара'] = list_list.name_list
                list_list.shop_list['Брeнд'] = list_list.brand_list
                list_list.shop_list['Старая цена'] = list_list.old_price_list
                list_list.shop_list['Новая цена'] = list_list.new_price_list
                list_list.shop_list['Ссылка на товар'] = list_list.link_list
                list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
                df = pd.DataFrame(list_list.shop_list)
                df.to_excel('sneakers.xlsx')
                print(404)
                break
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'women', brand_names)
        print('Больше нет страниц!')
        
class Lamoda:
    def lamoda_catalog(self, url: str):
        i = 1
        while True:
            URL_TEMPLATE = url
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
                        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link, strict=False):
                            list_list.name_list.append(name.get_text())
                            list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                            brand_names = brand_names.get_text().replace("'", "`")
                            list_list.brand_list.append(brand_names)
                            list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                            # сокращение ссылок
                            url_name_click = LINK_DOMEN + url_names.get('href')   
                            # url_name_result = click_url(url_name_click)
                            
                            url_img_click = LINK_IMG + img_link.get('src')
                            # url_img_result = click_url(url_img_click)
                            
                            list_list.link_list.append(url_name_click)
                            list_list.link_img_list.append(url_img_click)
                            list_list.table_matrix.append([name.get_text(), brand_names, old_prices.get_text(), new_prices.get_text(), url_name_click, url_img_click])
                        print(tabulate(list_list.table_matrix))
                        i += 1
                        print(i)
                    else:
                        list_list.shop_list['Название товара'] = list_list.name_list
                        list_list.shop_list['Брeнд'] = list_list.brand_list
                        list_list.shop_list['Старая цена'] = list_list.old_price_list
                        list_list.shop_list['Новая цена'] = list_list.new_price_list
                        list_list.shop_list['Ссылка на товар'] = list_list.link_list
                        list_list.shop_list['Ссылка на фото'] = list_list.link_img_list
                        df = pd.DataFrame(list_list.shop_list)
                        df.to_excel('sneakers.xlsx')
                        print('Конец парсинга, кроссовок больше нет!')
                        break
                else:
                    print(r.status_code+'\nОшибка. \тКонец парсинга!')
                    break
            except Exception:
                print('Конец парсинга, ошибка!')
                raise Exception('error')
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'men', brand_names)
        print('good db')
            
class Ozon:
    
    def ozon_catalog(url):
        options = Options()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')
        i = 1
        while True:
            driver = webdriver.Chrome()
            URL = url+f'?page={i}'
            driver.get(URL)
            driver.maximize_window()
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
                time.sleep(1)
                i+=1
            else:
                list_list.shop_list_ozon['Название товара'] = list_list.name_list
                list_list.shop_list_ozon['Старая цена'] = list_list.old_price_list
                list_list.shop_list_ozon['Новая цена'] = list_list.new_price_list
                list_list.shop_list_ozon['Ссылка на товар'] = list_list.link_list
                df = pd.DataFrame(list_list.shop_list_ozon)
                df.to_excel('table/xlsx/shop_ozon.xlsx')
                print('Конец парсинга, товара больше нет!')
                return driver.quit()
    
    def ozon_stock():
        
        URL = 'https://seller-edu.ozon.ru/fbo/warehouses/adresa-skladov-fbo'
        driver.get(URL)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        main_page = driver.page_source
        soup = bs(main_page, 'html.parser')
        elem = soup.find_all('p', class_='paragraph paragraph_zFY6U')
        name_city = soup.find_all('h3', class_='heading_B-bMK heading2 heading2_AQ929 heading-400_UXsA+')
        flag_name = 0
        name_city_flag = 0
        
        flag = 0
        f = 6
        u = 0
        g = 0
        vlans = {"Город": [], "Название в системе": [], "Координаты": [], "Фактический адрес": [], "Юридический адрес": [], 'ИНН / КПП склада': [], 'Р/С': [], 'Телефон': [], 'GLN': [], 'GUID': []}
        
        for name_ci in name_city:
            vlans['Город'].append(name_ci.get_text())
            g = 0
            
            # обработка информации о складах Озон
            while True:
                try:
                    if g == 8:
                        break
                    lol = elem[f]
                    i = lol
                    if i.get_text().startswith('Название в системе'):   #проверка на начало названия
                        start_name = i.get_text()
                        if i.get_text().startswith('МОСКВА_СППЗ'):  #Исключение для СППЗ
                            pass
                        else:
                            name_systym = i.get_text()  #Свежее "название в системе" с сайта
                            if name_systym[19:].startswith('('):    #Проверка на начало текста с кросс-кодингом, для большего сокращения текста
                                name = vlans['Название в системе'][-1]
                                flag = 1
                                if len(name)==2:    #Проверка на уже существующие пары одного города
                                    vlans['Название в системе'].append(delete_text.text(name_systym))
                                    f += 1
                                    continue
                                else:   #Если пары нету, то проверяем последний элемент массива с входящим названием в системе
                                    name_two = name
                                    name = name[:3] #Берем первые три буквы последнего названия в массиве
                                    if delete_text.text(name_systym).lower().startswith(name.lower()):   #Делаем нижний регистр для первых символов
                                        vlans['Название в системе'].pop(-1)       #Если есть совпадение то удаляем последний элемент массива и 
                                        vlans['Название в системе'].append([delete_text.text(name_systym), name_two])  #добавляем "названия в системе" одного города
                                        f += 1
                                        continue
                                    else:   #Если названия отличаются то добавляем "название" для следующего города
                                        vlans['Название в системе'].append(delete_text.text(name_systym))  
                                        f += 1
                                        continue
                            else:   #Стандартная запись "название в системе:"
                                if len(vlans['Название в системе'])>0:    #Проверка на пустоту массива с названиями        
                                    name = vlans['Название в системе'][-1]
                                    if len(name)==2 or flag == 0:                                #Проверка на уже существующие пары одного города
                                        vlans['Название в системе'].append(delete_text.text(name_systym))
                                        f += 1
                                        flag = 0
                                        continue
                                    else:      #Если пары нету, то проверяем последний элемент массива с входящим названием в системе
                                        name_two = name
                                        name = name[:3]
                                        if delete_text.text(name_systym).lower().startswith(name.lower()) and len(name)>0:
                                            vlans['Название в системе'].pop(-1)
                                            vlans['Название в системе'].append([delete_text.text(name_systym), delete_text.text(name_two)]) 
                                            f += 1
                                            continue
                                        else:
                                            flag = 0
                                            vlans['Название в системе'].append(delete_text.text(name_systym))
                                            f += 1
                                            continue
                                else:       #Если названий еще нет в массиве // самая первая проверка // первый элемент
                                    vlans['Название в системе'].append(delete_text.text(name_systym))
                                    f += 1
                                    continue
                    if lol.get_text().startswith('Фактический адрес'):
                        if len(vlans['Город']) == len(vlans['Фактический адрес']):
                            break
                        else:
                            vlans['Фактический адрес'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('GLN'):
                        if len(vlans['Город']) == len(vlans['GLN']):
                            break
                        else:
                            vlans['GLN'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('GUID'):
                        if len(vlans['Город']) == len(vlans['GUID']):
                            break
                        else:
                            vlans['GUID'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('Телефон') or lol.get_text().startswith('Контактные телефоны'):
                        if len(vlans['Город'])==len(vlans['Телефон']):
                            break
                        else:
                            vlans['Телефон'].append(lol.get_text())
                            f += 1  
                            
                            while elem[f].get_text().startswith('+7'):
                                lol = elem[f]
                                number = []
                                number.append(''.join(vlans['Телефон'][-1]))
                                number.append(delete_text.text(lol.get_text()))
                                vlans['Телефон'].pop(-1)
                                vlans['Телефон'].append(''.join(number))
                                f += 1
                                
                            g += 1
                            continue
                    if lol.get_text().startswith('ИНН / КПП склада'):
                        if len(vlans['Город']) == len(vlans['ИНН / КПП склада']):
                            break
                        else:
                            vlans['ИНН / КПП склада'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('Р/С'):
                        if len(vlans['Город']) == len(vlans['Р/С']):
                            break
                        else:
                            vlans['Р/С'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('Юридический адрес для'):
                        if len(vlans['Город']) == len(vlans['Юридический адрес']):
                            break
                        else:
                            vlans['Юридический адрес'].append(delete_text.text(lol.get_text()))
                            f += 1
                            g += 1
                            continue
                    if lol.get_text().startswith('Координаты'):
                        if len(vlans['Город']) == len(vlans['Координаты']):
                            break
                        else:
                            vlans['Координаты'].append(delete_text.text(lol.get_text()))
                            g += 1
                            f += 1
                            continue
                    else:
                        f += 1
                except Exception:
                    f-=1
                    g = 0
                    break
            # Проверка существования данных у склада
            if len(vlans['Город']) != len(vlans['Фактический адрес']):
                vlans['Фактический адрес'].append('Нет фактического адреса')
            if len(vlans['Город']) != len(vlans['Юридический адрес']):
                vlans['Юридический адрес'].append('Нет юридического адреса')
            if len(vlans['Город']) != len(vlans['Координаты']):
                vlans['Координаты'].append('Нет координат')
            if len(vlans['Город']) != len(vlans['ИНН / КПП склада']):
                vlans['ИНН / КПП склада'].append('Нет ИНН')
            if len(vlans['Город']) != len(vlans['Р/С']):
                vlans['Р/С'].append('Нет Р/С')
            if len(vlans['Город']) != len(vlans['Телефон']):
                vlans['Телефон'].append('Нет номера телефона')
            if len(vlans['Город']) != len(vlans['GLN']):
                vlans['GLN'].append('Нет GLN')
            if len(vlans['Город']) != len(vlans['GUID']):
                vlans['GUID'].append('Нет GUID')
        # если названий несколько, то они добавлены в таблицу с помощью массива, цикл проходит по всей таблицы и форматирует массивы в строки
        for i in range(len(vlans['Название в системе'])):
            if type(vlans['Название в системе'][i]) is list:
                f = vlans['Название в системе'][i]
                vlans['Название в системе'].pop(i)
                vlans['Название в системе'].insert(i, ', '.join(f))
        
                
        df = pd.DataFrame(vlans)
        df.to_excel('table/xlsx/stock_ozon.xlsx', index=False)
        df.to_csv('table/csv/stock_ozon.csv', index=False)

        print('Конец парсинга, все склады добавлены в excel!')
        
        driver.quit()

class Wildberries:
    #link of JSON wb
    
    #https://catalog.wb.ru/catalog/toys5/catalog?TestGroup=no_test&TestID=no_test&action=170902&appType=1&cat=9541&curr=rub&dest=-1257786&page=3&sort=popular&spp=26
    #/catalog/toys5/catalog
    #https://catalog.wb.ru/catalog/electronic14/catalog?TestGroup=no_test&TestID=no_test&action=170902&appType=1&cat=9835&curr=rub&dest=-1257786&page=3&sort=popular&spp=26
    def wildberries_catalog(url):
        
        # URL = url+f'/&page={i}'
        r = requests.get(url).json()
        print(r)
       
        
def main():
    ShopoTam.shopotam_catalog()
    # StreetBeat().streetbeat_catalog('woman')
    # SuperStep().superstep_catalog('https://superstep.ru/sale/filter/kategoriya-is-%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8/gender-is-%D0%BC%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D0%B0%D0%BC/apply/')
    # BrandShop().brandshop_catalog('https://brandshop.ru/sale/obuv/krossovki/?mfp=17-pol%5B%D0%96%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%5D')
    # Lamoda().lamoda_catalog('https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?brands=570')
    
if __name__=='__main__':
    main()
else:
    print(False)

#     captcha
#   
