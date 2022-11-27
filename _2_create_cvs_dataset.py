import csv
import os


def write_in_csv_file(folderpath, class_name):
    """write inforamtion about images into csv file

    Args:
        class_name (_type_): image's class name
    """
    with open('dataset.csv', mode='a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        i = 0
        while i != 1100:
            relative_way = f'dataset/{class_name}/{str(i).zfill(4)}.jpg'
            absolute_way = os.path.abspath(relative_way)
            if i == 0:
                print('aw ', absolute_way, '\nrw  ',
                      relative_way, '\n', class_name)
            if os.path.isfile(absolute_way):
                file_writer.writerow([absolute_way, relative_way, class_name])
            i += 1


def main(folderpath):
    """main function
    """
    print(folderpath)
    with open('dataset.csv', mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    write_in_csv_file(folderpath, 'brown_bears')
    write_in_csv_file(folderpath, 'polar_bears')
    print('program _2_create_cvs_dataset finished')


if __name__ == '__main__':
    main('dataset/')
