import requests
from bs4 import BeautifulSoup


def get_proxy():
    print("GETTING PROXY")
    try:
        page = requests.get('https://free-proxy-list.net/')
    except ConnectionError:
        return ''
    parsed_html = BeautifulSoup(page.content, "lxml")
    table = parsed_html.body.find('tbody')

    proxies = []
    for line in table:
        line = list(line)
        https = line[6].text

        if https == 'yes':
            host = line[0].text
            port = line[1].text
            proxies.append(f'{host}:{port}')
    return proxies
