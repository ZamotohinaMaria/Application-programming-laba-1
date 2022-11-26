import os
import sys
from PyQt5.QtWidgets import ( QPushButton, QApplication,
                             QMainWindow, QLabel)
from PyQt5.QtGui import (QIcon, QPixmap, QFont)


import _2_create_cvs_dataset
import _2_copy_dataset_name
import _2_copy_dataset_random_name
import _2_class_iterator


class Window(QMainWindow):
    """class for main window
    """
    def __init__(self):
        """initializing function
        """
        super().__init__()

        self.initUI() 
    
    def initUI(self):
        """initializing function for window
        """
        self.btn_x_size = 300
        self.btn_y_size = 40
        self.lust = 140
        btn_font_main = QFont('Arial', 11)
        btn_StyleSheet_main = 'background-color: #171982; color: #dbdcff; border :1px solid; '
        btn_font_secondary = QFont('Arial', 10)
        btn_StyleSheet_secondary = 'background-color: #abacff; border :1px solid;'
        #-------------------------------------------------------------------------------------------------------
        self.btn_create_csv_dataset = QPushButton('Создать аннотацию для датасета', self)
        self.btn_create_csv_dataset.setGeometry(self.lust, 0, self.btn_x_size, self.btn_y_size)
        self.btn_create_csv_dataset.setFont(btn_font_main)
        self.btn_create_csv_dataset.setStyleSheet(btn_StyleSheet_main)
        self.btn_create_csv_dataset.clicked.connect(self.create_csv_dataset)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_name = QPushButton('Копировать с новыми именами', self)
        self.btn_copy_dataset_name.setGeometry(self.btn_x_size + self.lust + 5, 0, self.btn_x_size, self.btn_y_size)
        self.btn_copy_dataset_name.setFont(btn_font_main)
        self.btn_copy_dataset_name.setStyleSheet(btn_StyleSheet_main)
        self.btn_copy_dataset_name.clicked.connect(self.copy_dataset_name)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_random_name = QPushButton('Копироватьс рандомными именами', self)
        self.btn_copy_dataset_random_name.setGeometry(2*self.btn_x_size + self.lust + 10, 0, self.btn_x_size,
                                                      self.btn_y_size)
        self.btn_copy_dataset_random_name.setFont(btn_font_main)
        self.btn_copy_dataset_random_name.setStyleSheet(btn_StyleSheet_main)
        self.btn_copy_dataset_random_name.clicked.connect(self.copy_dataset_random_name)
        #-------------------------------------------------------------------------------------------------------
               
        self.brown_bears_next = QPushButton('Следующая картинка бурых мишек --->', self)
        self.brown_bears_next.setGeometry(150, 600, self.btn_x_size, self.btn_y_size)
        self.brown_bears_next.setFont(btn_font_secondary)
        self.brown_bears_next.setStyleSheet(btn_StyleSheet_secondary)
        self.brown_bears_next.clicked.connect(self.next_brown)
        #-------------------------------------------------------------------------------------------------------
        
        self.polar_bears_next = QPushButton('Следующая картинка полярных мишек --->', self)
        self.polar_bears_next.setGeometry(750, 600, self.btn_x_size, self.btn_y_size)
        self.polar_bears_next.setFont(btn_font_secondary)
        self.polar_bears_next.setStyleSheet(btn_StyleSheet_secondary)
        self.polar_bears_next.clicked.connect(self.next_polar)

        self.folderpath = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Select folder for dataset'))
        self.image_lbl_brown = QLabel(self)
        self.image_lbl_polar = QLabel(self)
        self.brown_iterator = _2_class_iterator.Iterator('dataset.csv', 'brown_bears')
        self.polar_iterator = _2_class_iterator.Iterator('dataset.csv', 'polar_bears')

        #упраление окошком
        self.setGeometry(50, 50, 1200, 675)
        self.setWindowTitle('Application programing laba 3')
        self.setWindowIcon(QIcon('web.png'))
        self.setStyleSheet('background-color: #dbdcff;')
        self.show()

    def create_csv_dataset(self):
        _2_create_cvs_dataset.main(self.folderpath)

    def copy_dataset_name(self):
        _2_copy_dataset_name.main(self.folderpath)

    def copy_dataset_random_name(self):
        _2_copy_dataset_random_name.main(self.folderpath)

    def next_brown(self):
        self.image_way_brown = next(self.brown_iterator)
        while self.image_way_brown == None:
            self.image_way_brown = next(self.brown_iterator)
        if os.path.isfile(str(self.image_way_brown)):
            image = QPixmap(self.image_way_brown)
            self.image_lbl_brown.clear()
            self.image_lbl_brown.setPixmap(image)
            self.image_lbl_brown.adjustSize()
            self.image_lbl_brown.move(50, 200)
            self.image_lbl_brown.show()
        else:
            print('image dont find')

    def next_polar(self):
        self.image_way_polar = next(self.polar_iterator)
        while self.image_way_polar == None:
            self.image_way_polar = next(self.brown_iterator)
        if os.path.isfile(str(self.image_way_polar)):
            image = QPixmap(self.image_way_polar)
            self.image_lbl_polar.clear()
            self.image_lbl_polar.setPixmap(image)
            self.image_lbl_polar.adjustSize()
            self.image_lbl_polar.move(650, 200)
            self.image_lbl_polar.show()
        else:
            print('image don`t find')

    #messege box при закрытии
    # def closeEvent(self, event):

    #     reply = QMessageBox.question(self, 'Message',
    #         "Are you sure to quit?", QMessageBox.Yes |
    #         QMessageBox.No, QMessageBox.No)

    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv) #объект приложение, должен быть всегда, принимает на вход аргументы командной строки
    ex = Window()
    sys.exit(app.exec_())
