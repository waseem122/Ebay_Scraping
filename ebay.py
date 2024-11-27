import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    res = requests.get('https://www.ebay.com/')
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def parse(soup):
    print(soup.title.text)
    
parse(get_data())