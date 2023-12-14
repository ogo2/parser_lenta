import time
import json
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
import delete_text
import db
# options = Options()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36')
# driver = webdriver.Chrome()

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
    Lamoda().lamoda_catalog('https://www.lamoda.ru/c/2981/shoes-krossovk-kedy-muzhskie/?brands=570')
    
if __name__=='__main__':
    main()
else:
    print(False)

#     captcha
#   