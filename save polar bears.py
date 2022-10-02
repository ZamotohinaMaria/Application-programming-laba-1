#variant №5

import importlib
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
import cv2
import time

def Image_Search(Count_Find):
    num_page = 0
    i = 0
    while True:
        URL_polar = f'https://yandex.ru/images/search?pos={num_page}&text=polar%20bear&uinfo=sw-1366-sh-768-ww-780-wh-625-pd-1-wp-16x9_1366x768&lr=51&rpt=image'
        num_page += 1
        print(num_page)
        html_text_polar = requests.get(URL_polar).content
        soup_polar = BeautifulSoup(html_text_polar, 'html.parser')
        time.sleep(3)
        
        urls_polar = []

        for link in soup_polar.find_all('img'):
            urls_polar.append("https:" + link.get('src'))
        
        i = Save_Polar_Bears(urls_polar, Count_Find, i)


def Save_Polar_Bears(urls_polar, Count_Find, i):
    for url in urls_polar:
        if url.find('n=13') != -1 :
            try:
                filename = str(i) + '.jpg'
                img = requests.get(url)
                img_op = open(filename, 'wb')
                img_op.write(img.content)
                img_op.close()
                i += 1
            except:
                print("Error after", i)
            if i == Count_Find:
                Finish()
    return i


def Finish():
    print("\nProgramm is finished\n")
    exit(0)

print("Текущая деректория:", os.getcwd())
if os.path.isdir("polar bears") == 1:
    shutil.rmtree('polar bears')
os.mkdir("polar bears")
os.chdir("polar bears")
print("Текущая деректория:", os.getcwd())

Image_Search(100)