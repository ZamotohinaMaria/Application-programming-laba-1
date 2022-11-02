import cv2
import os
import shutil


def convert_images(way_name, save_way_name, count_get):
    os.chdir(way_name)
    images_way = []

    print("Текущая деректория:", os.getcwd())
    i = 0
    while i < count_get:
        images_way.append(str(i).zfill(4) + '.jpg')
        i += 1

    images = []
    for im in images_way:
        images.append(cv2.imread(im))

    if os.path.isdir(save_way_name) == 1:
        shutil.rmtree(save_way_name)
    os.mkdir(save_way_name)
    os.chdir(save_way_name)
    print("Текущая деректория:", os.getcwd())

    i = 0

    for im in images:
        save_way = str(i).zfill(4) + "_convert" + '.jpg'
        cv2.imwrite(save_way, im)
        i += 1


if __name__ == '__main__':
    convert_images("dataset_brown_bears", "brown_bears_convert", 4)
    os.chdir("..")
    os.chdir("..")
    convert_images("dataset_polar_bears", "polar_bears_convert", 30)
