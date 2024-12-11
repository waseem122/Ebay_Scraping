import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw=canon+m50&_sacat=0&LH_PrefLoc=3&LH_Sold=1&LH_Complete=1&rt=nc&LH_Auction=1')
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def parse(soup):
    product_links = soup.find_all('div', class_ = 's-item__info clearfix')
    print(product_links[2])
    
parse(get_data())