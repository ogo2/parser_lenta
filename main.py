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
from cutlink import lamoda_admitad, superstep_admitad, brandshop_admitad, shopotam_admitad, urbanvibes_admitad, elyts_admitad, bestwatch_admitad

# options = Options()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')
# driver = webdriver.Chrome()
class UrbanVibes:
    def urbanvibes_catalog(self, url: str):
        
        cookies = {
    'aid': '3d866249-5308-42e0-acac-e120f528c0b6',
    'auth_state': '2',
    'deduplication_cookie': 'admitad',
    'deduplication_cookie': 'admitad',
    'userTastyPieUrbanvibes': '2fbe28e4-366c-4a0a-ae42-c27e4335f5d6',
    'userPropertiesUrbanvibes': '.eJyrVsosLlayUspNUtJRSq0oULIyNDc0MbUwNzI301EqqSxIVbIy0VEqSKzMyU9MUbKqVkpPzY_Kz0sFakpLzClOra0FAJFzFN8.hPH0aAVTgzlXEQDfZ2yeaVp1KT_cMKlcoRnSGmF5e_E',
    'qrator_jsr': '1711997463.353.okIQ76sh2qLa5d4l-t06ordf3unco88f7l8ainu47hh7pr70l-00',
    'qrator_jsid': '1711997463.353.okIQ76sh2qLa5d4l-ru93rl2sjq9u51u7u80mk6gbma6bivc4',
    'JSESSIONID': 'F4058D803A05BB345AEACAA1052D9472',
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'baggage': 'sentry-public_key=9a4de0bdc92c49ec9536c393d3e24908,sentry-trace_id=78f1cf0d9321442697f762c7daf1259b,sentry-sample_rate=0.01',
            # 'cookie': 'aid=3d866249-5308-42e0-acac-e120f528c0b6; auth_state=2; deduplication_cookie=admitad; deduplication_cookie=admitad; userTastyPieUrbanvibes=2fbe28e4-366c-4a0a-ae42-c27e4335f5d6; userPropertiesUrbanvibes=.eJyrVsosLlayUspNUtJRSq0oULIyNDc0MbUwNzI301EqqSxIVbIy0VEqSKzMyU9MUbKqVkpPzY_Kz0sFakpLzClOra0FAJFzFN8.hPH0aAVTgzlXEQDfZ2yeaVp1KT_cMKlcoRnSGmF5e_E; qrator_jsr=1711997463.353.okIQ76sh2qLa5d4l-t06ordf3unco88f7l8ainu47hh7pr70l-00; qrator_jsid=1711997463.353.okIQ76sh2qLa5d4l-ru93rl2sjq9u51u7u80mk6gbma6bivc4; JSESSIONID=F4058D803A05BB345AEACAA1052D9472',
            'referer': 'https://urbanvibes.com/catalog/skidki/?f-age_gender_uv=age_gender_uv_muzhchinam&f-cat=cat_obuv',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': '78f1cf0d9321442697f762c7daf1259b-b37bd9bbed48c618-0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }


        
        i = 1
        while True:
            URL_TEMPLATE = url+f'&page={i}'
        #     params = {
        #     'f-cat': 'cat_obuv',
        #     'page': str(i),
        # }

            r = requests.get(URL_TEMPLATE, cookies=cookies, headers=headers)
            if r.status_code == 200:
                soup = bs(r.text, 'html.parser')
                title_name = soup.find_all('a', class_='catalog-product__link-name')
                if len(title_name)>0 and i<10:
                    old_price = soup.find_all('span', class_='app-price catalog-product__price app-price--old')
                    new_price = soup.find_all('span', class_='app-price catalog-product__price app-price--sale')
                    img_link = soup.find_all('img', class_='catalog-product__photo')
                    url_name = soup.find_all('a', class_='catalog-product__link-name')

                    # LINK_IMG = 'https://superstep.ru'
                    LINK_DOMEN = 'https://urbanvibes.com'
                    
                    for name, old_prices, new_prices, url_names, img_link in zip(title_name, old_price, new_price, url_name, img_link):
                        link = LINK_DOMEN+url_names.attrs['href']
                        re = requests.get(link, cookies=cookies, headers=headers)
                        if re.status_code == 200:
                            soup = bs(re.text, 'html.parser')
                            brand = soup.find('img', class_='product-page__logo-image')
                            brand = brand.attrs['alt']
                        list_list.name_list.append(name.get_text())
                        list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                        list_list.brand_list.append(brand)
                        list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                        
                        url_img_click = img_link.get('src')
                        url_prod = LINK_DOMEN + url_names.get('href')
                        list_list.link_list.append(urbanvibes_admitad(url_prod))
                        
                        list_list.link_img_list.append(url_img_click)
                        list_list.table_matrix.append([name.get_text(), brand, old_prices.get_text(), new_prices.get_text(), urbanvibes_admitad(url_prod), url_img_click])
                        time.sleep(0.2)
                    print(tabulate(list_list.table_matrix))
                    i += 1
                    time.sleep(0.4)
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
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'man', brand_names, 'shoes')
            print('good add db!-->', name)
        print('Больше нет страниц!')

class ShopoTam:
    def shopotam_catalog(url):
        o = 1
        while True:
            r = requests.get(url, f'?page={o}')
            soup = bs(r.text, 'html.parser')
            
            title_name = soup.find_all('div', class_='product-listing-card-info control-200 tablet-small:control-350 weight-medium product-listing-card-info_line-clamp_2')
            if len(title_name)>0 and o<10:
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
                    list_list.link_list.append(shopotam_admitad(url))
                    
                    list_list.link_img_list.append(url_img_click)
                    list_list.table_matrix.append([name.attrs['title'], brand_names.attrs['title'], old_prices.get_text(), new_prices.get_text(), shopotam_admitad(url), url_img_click])
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

            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'man', brand_names, 'shoes')
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
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, sex, brand_names, 'shoes')
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
                if len(title_name)>0 and i<29:
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
                        list_list.link_list.append(superstep_admitad(url_name_click))
                        list_list.link_img_list.append(url_img_click)
                        if name.contents[1].get_text() == '':
                            list_list.table_matrix.append([name.contents[2].get_text(), name.contents[0].get_text(), old_prices.get_text(), new_prices.get_text(), superstep_admitad(url_name_click), url_img_click])
                        else:
                            list_list.table_matrix.append([name.contents[1].get_text(), name.contents[0].get_text(), old_prices.get_text(), new_prices.get_text(), superstep_admitad(url_name_click), url_img_click])
                        
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
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'women', brand_names)
            print('good add db!-->', name)
        print('Больше нет страниц!')
        
class BrandShop:
    def brandshop_catalog(self, url: str):
        opts = Options()
        opts.ignore_local_proxy_environment_variables()
        i = 1
        while True: 
            URL_TEMPLATE = url+f'&page={i}'
            r = requests.get(URL_TEMPLATE)
            driver = webdriver.Chrome(options=opts)
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
                if len(title_name)>0 and i<2:
                    old_price = soup.find_all('span', class_='product-card__price_old')
                    new_price = soup.find_all('div', class_='product-card__price_new')
                    # img_link = soup.find_all('img', class_='lazyLoad')
                    # img_link = soup.find_all('img', zclass_='lazyLoad isLoaded')
                    img_link = soup.select('div > div.product-card__img._ibg > picture > img')
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
                        
                        list_list.link_list.append(brandshop_admitad(url_name_click))
                        list_list.link_img_list.append(url_img_click)
                        list_list.table_matrix.append([name.contents[2].get_text().strip(), brand_names, old_prices.get_text(), new_prices.get_text(), brandshop_admitad(url_name_click), url_img_click])
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
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'unisex', brand_names, 'watch')
        print('Больше нет страниц!')
        
class Lamoda:
    def lamoda_catalog(self, url: str):
        i = 1
        while True:
            URL_TEMPLATE = url+f'&page={i}'
            r = requests.get(URL_TEMPLATE)
            try:
                if r.status_code == 200:
                    soup = bs(r.text, 'html.parser')
                    # title 
                    title_name = soup.find_all('div', class_='x-product-card-description__product-name')
                    if len(title_name)>0 and i<29:
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
                        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
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
                            
                            list_list.link_list.append(lamoda_admitad(url_name_click))
                            list_list.link_img_list.append(url_img_click)
                            list_list.table_matrix.append([name.get_text(), brand_names, old_prices.get_text(), new_prices.get_text(), lamoda_admitad(url_name_click), url_img_click])
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
                return 'error'
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'man', brand_names, 'watch')
            print('good db')
            time.sleep(0.5)
        print('The end')

class Bestwatch:
    def bestwatch_catalog(self, url: str):
        i = 1
        while True:
            URL_TEMPLATE = url+f'?pages={i}'
            r = requests.get(URL_TEMPLATE)
            try:
                if r.status_code == 200:
                    soup = bs(r.text, 'html.parser')
                    # title 
                    title_name = soup.find_all('span', class_='catalog-item__name')
                    if len(title_name)>0 and i<10:
                        # old_price
                        old_price = soup.find_all('p', class_='catalog-item__oldprice')
                        #brand
                        brand = soup.find_all('span', class_='catalog-item__name')
                        # new_price
                        new_price = soup.find_all('p', class_='catalog-item__price with-sale')
                        # img
                        img_link = soup.find_all('img', class_='item_img')
                        # url
                        url_name = soup.select('div.catalog-item__body > a')
                        LINK_IMG = 'https:'
                        LINK_DOMEN = 'https://www.bestwatch.ru'
                        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
                            g = ''.join(filter(str.isnumeric, old_prices.get_text()))
                            if g == '':
                                continue
                            list_list.name_list.append(name.get_text())
                            list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                            brand_names = brand_names.contents[1].get_text().replace("'", "`")
                            list_list.brand_list.append(brand_names)
                            list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                            # сокращение ссылок
                            url_name_click = LINK_DOMEN + url_names.get('href')   
                            # url_name_result = click_url(url_name_click)
                            
                            url_img_click = LINK_IMG + img_link.get('src')
                            # url_img_result = click_url(url_img_click)
                            
                            list_list.link_list.append(bestwatch_admitad(url_name_click))
                            list_list.link_img_list.append(url_img_click)
                            list_list.table_matrix.append([name.get_text(), brand_names, old_prices.get_text(), new_prices.get_text(), bestwatch_admitad(url_name_click), url_img_click])
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
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'women', brand_names, 'watch')
            print('good db')
            time.sleep(0.5)
        print('The end')

class Elyts:
    def elyts_catalog(self, url: str):
        i = 1
        while True:
            URL_TEMPLATE = url
            r = requests.get(URL_TEMPLATE)
            try:
                if r.status_code == 200:
                    soup = bs(r.text, 'html.parser')
                    # title 
                    title_name = soup.select('div.product__content > div.product__description.text-center > a')
                    if len(title_name)>0 and i<2:
                        # old_price
                        old_price = soup.find_all('del', class_='product-item-price-old mr-2')
                        #brand
                        brand = soup.select('div.product__content > div.product__title.text-center > a')
                        # new_price
                        new_price = soup.find_all('span', class_='final-price with-discount')
                        # img
                        img_link = soup.select('span.product-item-image-slide.item.active > img')
                        # url
                        url_name = soup.select('div.product__content > div.product__description.text-center > a')
                        # LINK_IMG = 'https:'
                        LINK_DOMEN = 'https://elyts.ru'
                        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(title_name, old_price, new_price, url_name, brand, img_link):
                            list_list.name_list.append(name.get_text())
                            list_list.old_price_list.append(''.join(filter(str.isnumeric, old_prices.get_text())))
                            brand_names = brand_names.get_text().replace("'", "`")
                            list_list.brand_list.append(brand_names)
                            list_list.new_price_list.append(''.join(filter(str.isnumeric, new_prices.get_text())))
                            # сокращение ссылок
                            url_name_click = LINK_DOMEN + url_names.get('href')   
                            # url_name_result = click_url(url_name_click)
                            
                            url_img_click = img_link.get('src')
                            # url_img_result = click_url(url_img_click)
                            
                            list_list.link_list.append(elyts_admitad(url_name_click))
                            list_list.link_img_list.append(url_img_click)
                            list_list.table_matrix.append([name.get_text(), brand_names, old_prices.get_text(), new_prices.get_text(), elyts_admitad(url_name_click), url_img_click])
                                                  
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
                return 'error'
        for name, old_prices, new_prices, url_names, brand_names, img_link in zip(list_list.shop_list['Название товара'], list_list.shop_list['Старая цена'], 
                                                                                  list_list.shop_list['Новая цена'], list_list.shop_list['Ссылка на товар'],
                                                                                  list_list.shop_list['Брeнд'], list_list.shop_list['Ссылка на фото']):
            name = name.replace("'", "`")
            brand_names = brand_names.replace("'", "`")
            db.add_product(name, img_link, new_prices, old_prices, url_names, 'women', brand_names, 'watch')
            print('good db')
            time.sleep(0.5)
        print('The end')            


def main():
    # ShopoTam.shopotam_catalog()
    # StreetBeat().streetbeat_catalog('woman')
    # SuperStep().superstep_catalog('https://superstep.ru/sale/filter/kategoriya-is-%D0%B1%D0%BE%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-or-%D0%BA%D0%B5%D0%B4%D1%8B-or-%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8/gender-is-%D0%B6%D0%B5%D0%BD%D1%89%D0%B8%D0%BD%D0%B0%D0%BC/apply/')
    # BrandShop().brandshop_catalog('https://brandshop.ru/sale/aksessuary/naruchnye-chasy/')
    # Bestwatch().bestwatch_catalog('https://www.bestwatch.ru/watch/filter/sale:yes/pol:ladies/')
    # Elyts().elyts_catalog('https://elyts.ru/catalog/woman/aksessuary/chasy/filter/sale-is-20/')
    # Lamoda().lamoda_catalog('https://www.lamoda.ru/c/799/accs-muzhskie-chasy/?display_locations=outlet&is_sale=1')
    UrbanVibes().urbanvibes_catalog('https://urbanvibes.com/catalog/skidki/?f-age_gender_uv=age_gender_uv_zhenschinam&f-cat=cat_obuv')
    
if __name__=='__main__':
    main()
else:
    print(False)

#     captcha
#   
