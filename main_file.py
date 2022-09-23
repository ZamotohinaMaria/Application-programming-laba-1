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

soup = BeautifulSoup(requests.get(URL).text, 'lxml')
#print (soup)

img_url = "https://yandex.ru" + str(soup.find('div', class_ = "serp-item__preview").find('a', class_ = "serp-item__link").get('href'))
print('im=======', img_url)

img_url = img_url.replace('jpg&text=polar+bear&rpt', 'jpg&rpt') 

imgsoup = BeautifulSoup(requests.get(img_url).text, 'lxml')
print('im=======', img_url)

#save_url = imgsoup.find('div', class_="MediaViewer-LayoutMain MediaViewer_theme_fiji-LayoutMain").find('div', class_="MediaViewer-LayoutScene MediaViewer_theme_fiji-LayoutScene").find('div', class_="MediaViewer-View MediaViewer_theme_fiji-View").find('div', class_="SwipeImage MMImageWrapper").find('img', class_ = "MMImage-Origin").get('src')
save_url = imgsoup.find('div', class_="MediaViewer-LayoutMain MediaViewer_theme_fiji-LayoutMain")
print(save_url)



#https://yandex.ru/images/search?pos=0&from=tabbar&text=polar%20bear&img_url=http%3A%2F%2F1.bp.blogspot.com%2F-pyVg1yPyEqA%2FVmDazia5y3I%2FAAAAAAAAr5Q%2FbeuIfRNjGVs%2Fs1600%2FPolar-bear-HD-Widescreen-Wallpaper.jpg&rpt=simage&lr=51
# imgs_url = list(soup.find_all('div', class_ = "serp-item__preview").find('a', class_ = "serp-item__link").get('href'))

# for i in range (10):
#     imgs_url[i] = "https://yandex.ru" + str(imgs_url)
# print("imgs_url = \n", imgs_url)
# img = requests.get(img_url)
# img_op = open('2' + '.jpg', 'wb')
# img_op.write(img.content) 
# img_op.close()