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

print("Текущая деректория:", os.getcwd())
if os.path.isdir("polar bears") == 1:
    shutil.rmtree('polar bears')
os.mkdir("polar bears")
os.chdir("polar bears")
print("Текущая деректория:", os.getcwd())

num_page = 0
i = 0
while True:
    URL_polar = f'https://yandex.ru/images/search?{num_page}=3&text=polar%20bear&uinfo=sw-1366-sh-768-ww-780-wh-625-pd-1-wp-16x9_1366x768&lr=51&rpt=image'
    num_page += 1
    html_text_polar = requests.get(URL_polar).content
    soup_polar = BeautifulSoup(html_text_polar, 'html.parser')
    time.sleep(3)

    urls_polar = []

    for link in soup_polar.find_all('img'):
        urls_polar.append("https:" + link.get('src'))

    for url in urls_polar:
        if url.find('n=13') != -1 :
            try:
                filename = str(i) + '.jpg'
                img = requests.get(url)
                img_op = open(filename, 'wb')
                img_op.write(img.content)
                img_op.close()
                i += 1
                if i == 200:
                    break
            except:
                print("Error after", i)

#---------------------------------------------------------------------------
print("Текущая деректория:", os.getcwd())
os.chdir("..")
if os.path.isdir("brown bears") == 1:
    shutil.rmtree('brown bears')
os.mkdir("brown bears")
os.chdir("brown bears")
print("Текущая деректория:", os.getcwd())

num_page = 0
i = 0
while True:
    URL_brown = f'https://yandex.ru/images/search?p={num_page}2&text=brown%20bear&lr=51&rpt=image&uinfo=sw-1366-sh-768-ww-780-wh-625-pd-1-wp-16x9_1366x768'
    num_page += 1
    html_text_brown = requests.get(URL_brown).content
    soup_brown = BeautifulSoup(html_text_brown, 'html.parser')
    time.sleep(3)

    urls_brown = []

    for link in soup_brown.find_all('img'):
        urls_brown.append("https:" + link.get('src'))

    for url in urls_brown:
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
    if i == 200:
        exit(0)
