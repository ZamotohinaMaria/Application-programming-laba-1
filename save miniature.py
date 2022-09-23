#variant №5

import imp
import os
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime 
import pandas as pd



URL = 'https://yandex.ru/images/search?from=tabbar&text=polar%20bear'
print ('URL++======', URL)

html_text = requests.get(URL).text
#print (html_text)

soup = BeautifulSoup(html_text, 'lxml')
#print (soup)

img_url = "https:" + str(soup.find('div', class_ = "serp-item__preview").find('a', class_ = "serp-item__link").find('img', class_ = "serp-item__thumb justifier__thumb").get('src'))
#.find('img', class_ = "serp-item__thumb justifier__thumb")
print('im=======', img_url)

img = requests.get(img_url)
img_op = open('3' + '.jpg', 'wb')
img_op.write(img.content) 
img_op.close()