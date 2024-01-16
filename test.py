import requests
# from fake_useragent import UserAgent

headers = {
    'Referer': 'https://street-beat.ru/cat/man/sale/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = '{"pagination":{"page":2},"sorting":{"key":"sort","value":"desc"},"seo":{"uri":"/cat/man/sale/"},"search":""}'

response = requests.post('https://street-beat.ru/api/catalog/page', headers=headers, data=data)

print(response.text)