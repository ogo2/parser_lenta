import requests
from urllib.request import urlopen
from lxml import etree
# get html from site and write to local file
url = 'https://brandshop.ru/sale/obuv/krossovki/?mfp=17-pol%5B%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%BE%D0%B9%5D'
headers = {'Content-Type': 'text/html',}
response = requests.get(url, headers=headers)
html = f"""{response.text}"""

htmlparser = etree.HTMLParser()
tree = etree.parse(html, htmlparser)

fuck = tree.xpath('/html/body/div[3]/div/div/main/div/div[2]/div[2]/div/div[1]/a/div/div[1]/picture/img')
print(fuck)