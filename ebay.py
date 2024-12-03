import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=camera&_sacat=0')
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def parse(soup):
    product_links = soup.find_all('div', class_ = 's-item__info clearfix')
    print(product_links[0])
    
parse(get_data())