import csv
import os
import random
import shutil

from _2_class_iterator import Iterator


def write_in_cvs_file(file_name, class_name, img_name):
    """write inforamtion about images into csv file

    Args:
        class_name (_type_): image's class name
        img_name (_type_): image name
    """
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        relative_way = f'dataset/dataset_random_name/{img_name}'
        absolute_way = os.path.abspath(relative_way)
        file_writer.writerow(
            [absolute_way, relative_way, class_name, img_name])


def copy_images(file_name, class_name, count_get):
    """copying images from one folder to another with new random names

    Args:
        class_name (_type_): image's class name
        count_get (_type_): number for copying images
    """
    way = f'dataset/{class_name}'
    print(way)
    images_way = []
    i = 0
    while i != count_get:
        images_way.append(way + '/' + str(i).zfill(4) + '.jpg')
        i += 1

    print('dataset/dataset_random_name')

    for im in images_way:
        new_name = str(random.randint(0, 10001)).zfill(5) + '.jpg'
        while os.path.isfile(new_name):
            new_name = str(random.randint(0, 10001)).zfill(5) + '.jpg'
        save_way = f'dataset/dataset_random_name/{new_name}'
        shutil.copyfile(im, save_way)
        write_in_cvs_file(file_name, class_name, new_name)


def main(file_name):
    """main function
    """
    with open(file_name, mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(
            ['Absolute Path', 'Relative Path', 'Class Label', 'File name'])
    if os.path.isdir('dataset/dataset_random_name') == 1:
        shutil.rmtree('dataset/dataset_random_name')
    os.mkdir('dataset/dataset_random_name')
    copy_images(file_name, 'brown_bears', 1100)
    copy_images(file_name, 'polar_bears', 1100)
    print('program _2_copy_dataset_random_name finished')


if __name__ == '__main__':
    main('dataset_random_name.csv')
