
cookies = {
    'ipp_sign': '274a385fbb1f0602f5c592e5a720692d_952849163_b2ba8819de3df2046d266cbeb2f00660',
    'ipp_uid': '1705301453537/t3c5hlhtTveYl9kR/YJuaqxuG+hZo0pT2142rDQ==',
    'rerf': 'AAAAAGWk1dslKC7ABS3wAg==',
    'user_city': '%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3',
    'BX_USER_ID': '235f63a86f2040bf5da5058c6aa3f2f9',
    '_gid': 'GA1.2.267980212.1705301469',
    '_ym_uid': '170530147038501009',
    '_ym_d': '1705301470',
    'tmr_lvid': '67b3c6066b2c3281887a3b110fd16df2',
    'tmr_lvidTS': '1705301469527',
    'adrcid': 'Aar6u6XO0tC0dvwfeZ4xudg',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'mainpagetype': 'man',
    'user_usee': 'a%3A1%3A%7Bi%3A0%3Bs%3A7%3A%223723666%22%3B%7D',
    'PHPSESSID': 'HyOTwUSOug77xc3LLpHsnAOH6r7M4wQ4',
    'ipp_key': 'v1705476719672/v33947245ba5adc7a72e273/cz2XKJMlk6boNUTp4H+29Q==',
    'topMenu_active': '%2Fman%2F',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_ga': 'GA1.1.330262409.1705301469',
    'mindboxDeviceUUID': 'f3f59a7f-4af4-47d9-bf6d-8163f11ec92f',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22f3f59a7f-4af4-47d9-bf6d-8163f11ec92f%22%7D',
    'tmr_detect': '0%7C1705477958551',
    '_ga_E3GN5VV3T0': 'GS1.1.1705476722.8.1.1705478065.59.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'ipp_sign=274a385fbb1f0602f5c592e5a720692d_952849163_b2ba8819de3df2046d266cbeb2f00660; ipp_uid=1705301453537/t3c5hlhtTveYl9kR/YJuaqxuG+hZo0pT2142rDQ==; rerf=AAAAAGWk1dslKC7ABS3wAg==; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BX_USER_ID=235f63a86f2040bf5da5058c6aa3f2f9; _gid=GA1.2.267980212.1705301469; _ym_uid=170530147038501009; _ym_d=1705301470; tmr_lvid=67b3c6066b2c3281887a3b110fd16df2; tmr_lvidTS=1705301469527; adrcid=Aar6u6XO0tC0dvwfeZ4xudg; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; mainpagetype=man; user_usee=a%3A1%3A%7Bi%3A0%3Bs%3A7%3A%223723666%22%3B%7D; PHPSESSID=HyOTwUSOug77xc3LLpHsnAOH6r7M4wQ4; ipp_key=v1705476719672/v33947245ba5adc7a72e273/cz2XKJMlk6boNUTp4H+29Q==; topMenu_active=%2Fman%2F; _ym_isad=2; _ym_visorc=b; _ga=GA1.1.330262409.1705301469; mindboxDeviceUUID=f3f59a7f-4af4-47d9-bf6d-8163f11ec92f; directCrm-session=%7B%22deviceGuid%22%3A%22f3f59a7f-4af4-47d9-bf6d-8163f11ec92f%22%7D; tmr_detect=0%7C1705477958551; _ga_E3GN5VV3T0=GS1.1.1705476722.8.1.1705478065.59.0.0',
    'Origin': 'https://street-beat.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://street-beat.ru/cat/man/obuv/krossovki/sale/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pagination': {
        'page': 1,
    },
    'sorting': {
        'key': 'sort',
        'value': 'desc',
    },
    'seo': {
        'uri': '/cat/man/obuv/krossovki/sale/',
    },
    'search': '',
}

response = requests.post('https://street-beat.ru/api/catalog/page', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pagination":{"page":2},"sorting":{"key":"sort","value":"desc"},"seo":{"uri":"/cat/man/obuv/krossovki/sale/"},"search":""}'
#response = requests.post('https://street-beat.ru/api/catalog/page', cookies=cookies, headers=headers, data=data)
data = response.json()
for i in data['catalog']['listing']['items']:
    print('name------>',i['title'])
    print('brand------>',i['brand'])
    print('old_price------>',i['price']['recommended']['price'])
    print('new_price------>',i['price']['special']['price'])
    print('photo------>',i['image']['main']['desktop'])
    f = i['url']
    print('url------>',f'https://street-beat.ru{f}')
