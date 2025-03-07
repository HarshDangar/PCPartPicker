import time
import json
from itertools import product
from platform import processor

from bs4 import BeautifulSoup
import requests


def find_info():
    html_text = requests.get("https://tlggaming.com/processors").text
    soup = BeautifulSoup(html_text, 'lxml')

    processor = soup.find_all('div', class_ = 'caption')

    for i in processor:
        product_name = i.find('div', class_ = 'name').text
        product_price = i.find('span', class_ = 'price-new').text
        product_link = i.find('div',class_ = 'name')

        print(f'''
        Product Name : {product_name}
        Price : {product_price.replace("Rs.", "").replace(",", "").replace(".00", "")}
        Link : {product_link.a['href']}
        ''')

        print('')

if __name__ == '__main__':
    while True:
        find_info()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)