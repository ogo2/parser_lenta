table_matrix = [['Название товара', 'Брeнд','Старая цена', 'Новая цена', 'Ссылка на товар']]
shop_list = {'Название товара': [],
             'Брeнд': [],
                'Старая цена': [],
                'Новая цена': [],
                'Ссылка на товар': []}

old_price_list = []
new_price_list = []
link_list = []
name_list = []
brand_list = []

table_matrix_ozon = [['Название товара', 'Старая цена', 'Новая цена', 'Ссылка на товар']]
shop_list_ozon = {'Название товара': [],
                'Старая цена': [],
                'Новая цена': [],
                'Ссылка на товар': []}

HEADERS = {
      'User-Agentt': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36',
      # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      # 'Accept-Language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      # 'Accept-Encoding':'gzip, deflate, br',
      # 'Cache-Control':'max-age=0',
      # 'Sec-Ch-Ua-Platform': '"Windows"',
      # 'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"'
    }

proxy = {'https' : 'https://37.19.220.133:8443',  
           'http': 'http://147.182.132.21:80', 
           'https': 'https://52.21.81.75:3128',
           'https': 'https://37.19.220.129:8443'}
table_matrix = [['Название кроссовок', 'Брeнд','Старая цена', 'Новая цена', 'Ссылка на товар']]
shop_list = {'Название кроссовок': [],
             'Брeнд': [],
                'Старая цена': [],
                'Новая цена': [],
                'Ссылка на товар': []}
old_price_list = []
new_price_list = []
link_list = []
name_list = []
brand_list = []
