#variant №5
import os
from bs4 import BeautifulSoup
import requests
import shutil
import time


def image_search(count_find):
    num_page = 0
    i = 0
    time_sleep = 10.5
    while True:
        url_polar = f'https://yandex.ru/images/search?p={num_page}&from=tabbar&text=polar%20bear&lr=51&rpt=image'
        num_page += 1
        print(num_page)
        html_text_polar = requests.get(url_polar).content
        soup_polar = BeautifulSoup(html_text_polar, 'html.parser')
        time.sleep(time_sleep )
        time_sleep +=0.1
        
        urls_polar = []

        for link in soup_polar.find_all('img'):
            urls_polar.append("https:" + link.get('src'))
        
        i = save_images(urls_polar, count_find, i)


def save_images(urls_polar, count_find, i):
    for url in urls_polar:
        if url.find('captcha') != -1 :
            print("\nCAPTCHA ERROR")
            finish()
        print(url)
        if url.find('n=13') != -1 :
            try:
                filename = str(i).zfill(4) + '.jpg'
                img = requests.get(url)
                img_op = open(filename, 'wb')
                img_op.write(img.content)
                img_op.close()
                i += 1
            except:
                print("Error after", i)
            if i == count_find:
                finish()
    return i


def finish():
    print("\nProgramm is finished\n")
    exit(0)


if __name__ == '__main__':
    print("Текущая деректория:", os.getcwd())
    if os.path.isdir("dataset_polar_bears") == 1:
        shutil.rmtree('dataset_polar_bears')
    os.mkdir("dataset_polar_bears")
    os.chdir("dataset_polar_bears")
    print("Текущая деректория:", os.getcwd())
    Count_Find = 1100
    image_search(Count_Find)
