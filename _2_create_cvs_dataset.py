import csv
import os


def write_in_cvs_file(file_name, class_name):
    """write inforamtion about images into csv file

    Args:
        class_name (_type_): image's class name
    """
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        i = 0
        while i != 1100:
            relative_way = f'dataset/{class_name}/{str(i).zfill(4)}.jpg'
            absolute_way = os.path.abspath(relative_way)
            if i == 0:
                print('aw ', absolute_way, '\nrw  ',
                      relative_way, '\n', class_name)
            if os.path.isfile(relative_way):
                file_writer.writerow([absolute_way, relative_way, class_name])
            i += 1


def main(file_name):
    """main function
    """
    with open(file_name, mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        file_writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
    write_in_cvs_file(file_name, 'brown_bears')
    write_in_cvs_file(file_name, 'polar_bears')
    print('program _2_create_cvs_dataset finished')


if __name__ == '__main__':
    main('dataset.csv')
