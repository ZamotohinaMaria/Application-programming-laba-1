import os
import sys
from typing import Iterator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QToolTip, QCheckBox, 
    QPushButton, QApplication, QMessageBox, QMainWindow,
    QHBoxLayout, QVBoxLayout, QLabel)
from PyQt5.QtGui import (QIcon, QPixmap, QFont)
from PyQt5.QtCore import (Qt, QCoreApplication)


import _2_create_cvs_dataset
import _2_copy_dataset_name
import _2_copy_dataset_random_name
import _2_class_iterator

class Window( QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI() 
    
    def initUI(self):
        
        self.btn_x_size = 270
        self.btn_y_size = 40
        #-------------------------------------------------------------------------------------------------------
        self.btn_create_csv_dataset = QPushButton('Создать аннотацию для датасета', self)
        self.btn_create_csv_dataset.setGeometry(0, 0, self.btn_x_size, self.btn_y_size)
        self.btn_create_csv_dataset.clicked.connect(self.create_csv_dataset)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_name = QPushButton('Копировать датасет с новыми именами', self)
        self.btn_copy_dataset_name.setGeometry(self.btn_x_size, 0, self.btn_x_size, self.btn_y_size)
        self.btn_copy_dataset_name.clicked.connect(self.copy_dataset_name)
        
        self.csv_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_name_checkbox.setGeometry(self.btn_x_size, self.btn_y_size, 200, 40)
        self.csv_name_checkbox.toggle()
        self.csv_name_checkbox.stateChanged.connect(self.name_checkbox)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_random_name = QPushButton('Копировать датасет с рандомными именами', self)
        self.btn_copy_dataset_random_name.setGeometry(2*self.btn_x_size, 0, self.btn_x_size, self.btn_y_size)
        self.btn_copy_dataset_random_name.clicked.connect(self.copy_dataset_random_name)
        
        self.csv_random_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_random_name_checkbox.setGeometry(2*self.btn_x_size, self.btn_y_size, 200, 40)
        self.csv_random_name_checkbox.toggle()
        self.csv_random_name_checkbox.stateChanged.connect(self.random_name_checkbox)
        #-------------------------------------------------------------------------------------------------------
               
        self.brown_bears_next = QPushButton('Следующая картинка бурых мишек --->', self)
        self.brown_bears_next.setGeometry(150, 600, self.btn_x_size, self.btn_y_size)
        self.brown_bears_next.clicked.connect(self.next_brown)
        #-------------------------------------------------------------------------------------------------------
        
        self.polar_bears_next = QPushButton('Следующая картинка полярных мишек --->', self)
        self.polar_bears_next.setGeometry(750, 600, self.btn_x_size, self.btn_y_size)
        self.polar_bears_next.clicked.connect(self.next_polar)

        
        #self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select folder for dataset')
        self.image_lbl_brown = QLabel(self)
        self.image_lbl_polar = QLabel(self)
        self.brown_iterator = _2_class_iterator.Iterator('dataset.csv', 'brown_bears')
        self.polar_iterator = _2_class_iterator.Iterator('dataset.csv', 'polar_bears')
        
        #упраление окошком
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def name_checkbox(self, state):
        if state == Qt.Checked:
            self.create_csv_dataset
            
    def random_name_checkbox(self, state):
        if state == Qt.Checked:
            self.create_csv_dataset
    
    def create_csv_dataset(self):
        _2_create_cvs_dataset.main('files_dataset.csv')
    def copy_dataset_name(self):
        _2_copy_dataset_name.main('copy_dataset_name.csv')
    def copy_dataset_random_name(self):
        _2_copy_dataset_random_name.main('copy_dataset_random_name.csv')
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
            self.image_lbl_polar.move(650, 150)
            self.image_lbl_polar.show()
        else:
            print('image dont find')       
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