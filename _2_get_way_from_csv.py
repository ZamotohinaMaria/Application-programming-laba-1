from _2_class_iterator import Iterator


def main():
    """main function
    """
    i = Iterator('dataset.csv', 'polar_bears')
    for val in i:
        print(val)

    print('program _2_get_way_from_csv finished')


if __name__ == '__main__':
    main()
