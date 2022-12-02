import csv
import cv2
import matplotlib.pyplot as plt
import random
import pandas as pd


def filtering(dataframe, class_name):
    res_dataframe = (dataframe[dataframe.class_name == class_name])
    return res_dataframe


def shape_filtering(dataframe, class_name, max_width, max_hight):
    res_dataframe = (dataframe[dataframe.class_name == class_name][
                     dataframe.image_width <= max_width][dataframe.image_hight <= max_hight])
    return res_dataframe


def create_histograma(dataframe, class_name):
    result = [[], [], []]
    if (class_name == 'brown_beras'):
        image_index = random.randint(0, 1100)
    if (class_name == 'polar_bears'):
        image_index = random.randint(1100, 2200)
    image_way = filtering(dataframe, class_name)[
        'absolute_way'].loc[image_index]

    image = cv2.imread(image_way)

    cv2.imshow(f'image number {image_index}', image)
    cv2.waitKey(0)

    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
        result[i] = histr
    plt.gcf().canvas.set_window_title(f'картинка номер {image_index}')
    plt.show()

    return result


def show_histograma(hisrt_data):
    color = hisrt_data[0]
    name_color = hisrt_data[1]

    if name_color == "r":
        plt.hist(color, color="red")
        plt.title("Red color", color="red")
    if name_color == "g":
        plt.hist(color, color="green")
        plt.title("Green color", color="green")
    if name_color == "b":
        plt.hist(color, color="blue")
        plt.title("Blue color", color="blue")
    plt.xlabel("Intensity")
    plt.ylabel("Number of pixels")
    plt.show()


def create_dataframe():
    file_name = 'dataset.csv'
    class_label = []
    class_name = []
    absolute_way = []
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == 'brown_bears':
                class_label.append(0)
            elif row[2] == 'polar_bears':
                class_label.append(1)
            else:
                class_label.append('class label')
            class_name.append(row[2])
            absolute_way.append(row[0])

    dataframe = pd.DataFrame(
        {
            class_name[0]: pd.array(class_name[1:]),
            absolute_way[0]: pd.array(absolute_way[1:]),
        }
    )

    dataframe = dataframe.rename(
        columns={class_name[0]: 'class_name',
                 absolute_way[0]: 'absolute_way'}
    )

    dataframe['class_label'] = pd.array(class_label[1:])

    image_width = []
    image_hight = []
    image_depth = []
    pixels_count = []
    for way in absolute_way[1:]:
        try:
            image = cv2.imread(way)
            image_width.append(image.shape[1])
            image_hight.append(image.shape[0])
            image_depth.append(image.shape[2])
            pixels_count.append(image.size)
        except BaseException:
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
    print('----------------------------------------------------------')
    print(shape_filtering(dataframe, 'polar_bears', 300, 400))

    dataframe['pixels_count'] = pd.array(pixels_count)
    print('\nmin pixels\n')
    print(dataframe.groupby('class_name').pixels_count.min())
    print('\nmax pixels\n')
    print(dataframe.groupby('class_name').pixels_count.max())
    print('\nmean pixels\n')
    print(dataframe.groupby('class_name').pixels_count.mean())

    data_for_histograma = create_histograma(dataframe, 'polar_bears')
    about_picture = [(data_for_histograma[0], 'b'),
                     (data_for_histograma[1], 'g'),
                     (data_for_histograma[2], 'r')]

    show_histograma(about_picture[0])


def main():
    print('program start')
    pd.set_option('display.max_colwidth', None)
    create_dataframe()
    print('program finish')


if __name__ == '__main__':
    main()
