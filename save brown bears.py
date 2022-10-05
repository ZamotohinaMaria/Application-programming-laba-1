import os
from bs4 import BeautifulSoup
import requests
import shutil
import time


def image_search(count_find):
    num_page = 0
    i = 0
    while True:
        url_brown = f'https://yandex.ru/images/search?p={num_page}&text=brown%20bear&lr=51&from=tabbar&rpt=image'
        num_page += 1
        print(num_page)
        html_text_brown = requests.get(url_brown).content
        soup_brown = BeautifulSoup(html_text_brown, 'html.parser')
        time.sleep(15)
        
        urls_brown = []

        for link in soup_brown.find_all('img'):
            urls_brown.append("https:" + link.get('src'))
        
        i = save_images(urls_brown, count_find, i)


def save_images(urls_brown, count_find, i):
    for url in urls_brown:
        if url.find('captcha') != -1:
            print("\nCAPTCHA ERROR")
            finish()
        print(url)
        if url.find('n=13') != -1:
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
    if os.path.isdir("dataset_brown_bears") == 1:
        shutil.rmtree('dataset_brown_bears')
    os.mkdir("dataset_brown_bears")
    os.chdir("dataset_brown_bears")
    print("Текущая деректория:", os.getcwd())

    Count_Find = 1100
    image_search(Count_Find)
