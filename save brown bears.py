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
        URL_brown = f'https://yandex.ru/images/search?p={num_page}&text=brown%20bear&lr=51&from=tabbar&rpt=image'
        num_page += 1
        print(num_page)
        html_text_brown = requests.get(URL_brown).content
        soup_brown = BeautifulSoup(html_text_brown, 'html.parser')
        time.sleep(10)
        
        urls_brown = []

        for link in soup_brown.find_all('img'):
            urls_brown.append("https:" + link.get('src'))
        
        i = Save_Brown_Bears(urls_brown, Count_Find, i)


def Save_Brown_Bears(urls_brown, Count_Find, i):
    for url in urls_brown:
        if url.find('captcha') != -1 :
            print("\nCAPTCHA ERROR")
            Finish()
        print(url)
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
if os.path.isdir("brown bears") == 1:
    shutil.rmtree('brown bears')
os.mkdir("brown bears")
os.chdir("brown bears")
print("Текущая деректория:", os.getcwd())


Count_Find = 1100
Image_Search(Count_Find)