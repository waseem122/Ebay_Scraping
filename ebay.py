import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=canon+m50&_sacat=0&LH_PrefLoc=3&LH_Sold=1&LH_Complete=1&rt=nc&LH_Auction=1')
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def parse(soup):
    product_links = soup.find_all('div', class_ = 's-item__info clearfix')
    product_list = []
    for i in product_links:
        try:
            products = {
                'title': i.find('div', class_ = 's-item__title').text,
                'soldprice': i.find('span', class_ = 's-item__price').text,
                'soldDate': i.find('div', class_ = 's-item__caption').text,
                'bids': i.find('span', class_ = 's-item__bids s-item__bidCount').text,
                'link': i.find('a', class_ = 's-item__link')['href'],
            }
            product_list.append(products)
        except:
            pass
        # print(product)
    return product_list
product_list = parse(get_data())
print(product_list)