import datetime
from selenium import webdriver

from utils import get_proxy


def get_code():
    url_index = 'https://russian.rt.com/'
    proxies = get_proxy()
    while True:
        print(f'Start: {datetime.datetime.now()}')

        if not proxies:
            proxies = get_proxy()
        proxy = proxies.pop()


        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--proxy-server=' + proxy)


        browser = webdriver.Chrome(chrome_options=options)
        browser.set_page_load_timeout(10)

        try:
            browser.get(url_index)
            browser.quit()
            print("Fucked")
        except KeyboardInterrupt:
            browser.quit()
        except Exception as e:
            print(e)
            continue
        print(f'End: {datetime.datetime.now()}')


if __name__ == "__main__":
    get_code()
