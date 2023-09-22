import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tabulate import tabulate

table_matrix = [['Заголовок новости', 'Ссылка на новость']]
i = 1
for i in range(10):
    URL_TEMPLATE = f'https://lenta.ru/parts/news/{i+1}/'
    
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')
    print(URL_TEMPLATE)
    # title
    title_name = soup.find_all('h3', class_='card-full-news__title')

    # url
    url_name = soup.find_all('a', class_='card-full-news _parts-news')

    
    
    LINK_DOMEN = 'https://lenta.ru/'

    for name, link in zip(title_name, url_name):
        link_result = LINK_DOMEN + link.get('href');
        table_matrix.append([name.get_text(), link_result])
    print(f'{i+1}0%')
        
    
print(tabulate(table_matrix))

# print(tabulate(table_matrix))
    

if __name__ == '__main__':
    print(True)