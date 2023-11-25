import requests

endpoint = 'https://clck.ru/--'

def click_url(url):
    url = (f'{url}', '?utm_source=sender')

    response = requests.get(
        endpoint,
        params = {'url': url}
    )
    return response.text