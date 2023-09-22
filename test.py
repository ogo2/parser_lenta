import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate

# Lamoda 
# https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481

table_matrix = [['Название кроссовок', 'Старая цена', "Новая цена", "Фото", "Ссылка на пару кроссовок"]]


URL_TEMPLATE = 'https://www.lamoda.ru/c/2968/shoes-krossovki-kedy/?display_locations=outlet&is_sale=1&brands=1061,30349,1163,4035,27481'

r = requests.get(URL_TEMPLATE)

if r.status_code == 200:
    soup = bs(r.text, 'html.parser')
    
    file_reed = open('lenta.html', 'w', encoding='utf-8')
    file_reed.write(r.text)
    file_reed.close()
    title
    title_name = soup.find_all('div', class_='x-product-card-description__product-name _productName_1okc5_7')
    # old_price
    old_price = soup.find_all('span', class_='x-product-card-description__price-old _price_1okc5_8')
    # new_price
    new_price = soup.find_all('span', class_='x-product-card-description__price-new x-product-card-description__price-WEB8507_price_no_bold _price_1okc5_8')
    # img
    img_link = soup.find_all('img', class_='_root_1wiwn_3 x-product-card__pic-img x-product-card__pic-img')
    # url
    url_name = soup.find_all('a', class_='_root_f9xmk_2 _label_f9xmk_20 x-product-card__pic x-product-card__pic-catalog x-product-card__pic x-product-card__pic-catalog')
    print(url_name)
    LINK_IMG = 'https:'
    LINK_DOMEN = 'https://www.lamoda.ru'
    for name, old_prices, new_prices, img_links, url_names in zip(title_name, old_price, new_price, img_link, url_name):
        url_name_result = LINK_DOMEN + url_names.get('href')    
        link_result_img = LINK_IMG + img_links.get('href')
        table_matrix.append([name.get_text(), old_price.get_text(), new_price.get_text(), link_result_img, url_name_result])
        
            
        
    print(tabulate(table_matrix))
else:
    print(r.status_code)
# print(tabulate(table_matrix))
    

if __name__ == '__main__':
    print(True)