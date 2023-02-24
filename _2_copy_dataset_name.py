import csv
import os
import shutil


def write_in_cvs_file(folderpath, class_name, img_name):
    """write inforamtion about images into csv file

    Args:
        class_name (_type_): image's class name
        img_name (_type_): image name
    """
    with open('copy_dataset_name_new.csv', mode='a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        relative_way = f'dataset/dataset_name/{img_name}'
        absolute_way = f'{folderpath}/dataset_name/{img_name}'
        file_writer.writerow(
            [absolute_way, relative_way, class_name, img_name])


def copy_images(folderpath, class_name, count_get):
    """copying images from one folder to another with new names

    Args:
        class_name (_type_): image's class name
        count_get (_type_): number for copying images
    """
    way = f'{folderpath}/{class_name}'
    print(way)
    images_way = []
    i = 0
    while i != count_get:
        images_way.append(way + '/' + str(i).zfill(4) + '.jpg')
        i += 1

    print(f'{folderpath}/dataset_name')
    i = 0
    for im in images_way:
        save_way = f'{folderpath}/dataset_name/{class_name}_{str(i).zfill(4)}.jpg'
        shutil.copyfile(im, save_way)
        write_in_cvs_file(folderpath, class_name, class_name + '_' + str(i).zfill(4) + '.jpg')
        i += 1


def main(folderpath):
    """main function
    """
    with open('copy_dataset_name_new.csv', mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(
            ['Absolute Path', 'Relative Path', 'Class Label', 'File name'])
    if os.path.isdir(f'{folderpath}/dataset_name') == 1:
        shutil.rmtree(f'{folderpath}/dataset_name')
    os.mkdir(f'{folderpath}/dataset_name')
    copy_images(folderpath, 'brown_bears', 1100)
    copy_images(folderpath, 'polar_bears', 1100)
    print('program _2_copy_dataset_name finished')


if __name__ == '__main__':
    main('dataset/')
