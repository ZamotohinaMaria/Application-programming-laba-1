#variant №5

import imp
import os
from bs4 import BeautifulSoup
import requests
import re
from re import I, sub
from decimal import Decimal
import io
from datetime import datetime 
import pandas as pd
import shutil


print("Текущая деректория:", os.getcwd())
if os.path.isdir("polar bears")==1:
     shutil.rmtree('polar bears')
os.mkdir("polar bears")
os.chdir("polar bears")
print("Текущая деректория:", os.getcwd())

URL = 'https://yandex.ru/images/search?from=tabbar&text=polar%20bear'

html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'lxml')

img_tags = soup.find_all('img', class_ = "serp-item__thumb justifier__thumb")

urls = ["https:"+ img['src'] for img in img_tags]
print("urls\n", urls)
i=0
for url in urls:
    filename = str(i)+'.jpg'
    img = requests.get(url)
    img_op = open(filename, 'wb')
    img_op.write(img.content) 
    img_op.close()
    i+=1

    