import requests, re, time
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    res = requests.get('https://www.google.com/')
    print(res.status_code)


get_data()