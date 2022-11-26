import csv
import cv2
import os
import pandas as pd


def filtering(dataframe, class_name):
    res_dataframe = pd.DataFrame(dataframe[dataframe['class_name'] == class_name])
    return res_dataframe

def create_dataframe():
    file_name = 'dataset.csv'
    class_label = []
    class_name =[]
    absolute_way = []
    with open(file_name) as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2]== 'brown_bears':
                    class_label.append(0)
                elif row[2]== 'polar_bears':
                    class_label.append(1)
                else:
                    class_label.append('class label')
                class_name.append(row[2])
                absolute_way.append(row[0])
                
    dataframe = pd.DataFrame(
        {
            class_name[0]: pd.array(class_name[1:]),
            absolute_way[0]:  pd.array(absolute_way[1:]),
        }
    )
    
    dataframe = dataframe.rename(
        columns={class_name[0]: 'class_name',
                 absolute_way[0]: 'absolute_way'}
        )
    
    dataframe['class_label'] = pd.array(class_label[1:])
    
    image_width =[]
    image_hight = []
    image_depth = []
    for way in absolute_way[1:]:
        try:
            image = cv2.imread(way)
            image_width.append(image.shape[1])
            image_hight.append(image.shape[0])
            image_depth.append(image.shape[2])
        except:
            pass
    dataframe['image_width'] = pd.array(image_width)
    dataframe['image_hight'] = pd.array(image_hight)
    dataframe['image_depth'] = pd.array(image_depth)
    
    print(dataframe.columns)
    print(dataframe)
    
    print('\nwidth statistic\n', dataframe['image_width'].describe())
    print('\nhight statistic\n', dataframe['image_hight'].describe())
    print('\ndepth statistic\n', dataframe['image_depth'].describe())
    print('\nclass label statistic\n', dataframe['class_label'].describe())
    
    print(filtering(dataframe, 'polar_bears'))
    #print(dataframe[dataframe['class_name'] == 'polar_bears'])

def main():
    print('program start')
    pd.set_option('display.max_colwidth', None)
    create_dataframe()
    print('program finish')
    
    
if __name__ == '__main__':
    main()
