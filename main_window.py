import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QToolTip, QCheckBox, 
    QPushButton, QApplication, QMessageBox, QMainWindow,
    QHBoxLayout, QVBoxLayout, QLabel)
from PyQt5.QtGui import (QIcon, QPixmap, QFont)
from PyQt5.QtCore import (Qt, QCoreApplication)


import _2_create_cvs_dataset
import _2_copy_dataset_name
import _2_copy_dataset_random_name

class Window( QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI() 
    
    def initUI(self):
        
        self.btn_x_size = 270
        self.btn_y_size = 40
        #-------------------------------------------------------------------------------------------------------
        self.btn_create_csv_dataset = QPushButton('Создать аннотацию для датасета', self)
        self.btn_create_csv_dataset.setGeometry(50, 0, self.btn_x_size, self.btn_y_size)
        self.btn_create_csv_dataset.clicked.connect(self.create_csv_dataset)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_name = QPushButton('Копировать датасет с новыми именами', self)
        self.btn_copy_dataset_name.setGeometry(50 + self.btn_x_size, 0, self.btn_x_size, self.btn_y_size)
        self.btn_copy_dataset_name.clicked.connect(self.copy_dataset_name)
        
        self.csv_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_name_checkbox.setGeometry(50 + self.btn_x_size, self.btn_y_size, 200, 40)
        self.csv_name_checkbox.toggle()
        self.csv_name_checkbox.stateChanged.connect(self.name_checkbox)
        #-------------------------------------------------------------------------------------------------------
        self.btn_copy_dataset_random_name = QPushButton('Копировать датасет с рандомными именами', self)
        self.btn_copy_dataset_random_name.setGeometry(50 + 2*self.btn_x_size, 0, self.btn_x_size, self.btn_y_size)
        self.btn_copy_dataset_random_name.clicked.connect(self.copy_dataset_random_name)
        
        self.csv_random_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_random_name_checkbox.setGeometry(50 + 2*self.btn_x_size, self.btn_y_size, 200, 40)
        self.csv_random_name_checkbox.toggle()
        self.csv_random_name_checkbox.stateChanged.connect(self.random_name_checkbox)
        #-------------------------------------------------------------------------------------------------------
        self.brown_bears_previous = QPushButton('<---', self)
        self.brown_bears_previous.setGeometry(50, 600, self.btn_x_size/3, self.btn_y_size)
        self.brown_bears_previous.clicked.connect(self.previous_brown)
        
        self.brown_bears_label = QLabel('Бурые мишки', self)
        self.brown_bears_label.setAlignment(Qt.AlignCenter)
        self.brown_bears_label.setGeometry(150, 600, self.btn_x_size/3, 40)
        
        self.brown_bears_next = QPushButton('--->', self)
        self.brown_bears_next.setGeometry(250, 600, self.btn_x_size/3, self.btn_y_size)
        self.brown_bears_next.clicked.connect(self.next_brown)
        #-------------------------------------------------------------------------------------------------------
        self.polar_bears_previous = QPushButton('<---', self)
        self.polar_bears_previous.setGeometry(600, 600, self.btn_x_size/3, self.btn_y_size)
        self.polar_bears_previous.clicked.connect(self.previous_polar)
        
        self.polar_bears_label = QLabel('Полярные мишки', self)
        self.polar_bears_label.setAlignment(Qt.AlignCenter)
        self.polar_bears_label.setGeometry(700, 600, self.btn_x_size/3, 40)
        
        self.polar_bears_next = QPushButton('--->', self)
        self.polar_bears_next.setGeometry(800, 600, self.btn_x_size/3, self.btn_y_size)
        self.polar_bears_next.clicked.connect(self.next_polar)
        
        #кнопка выхода - закрытия окна
        self.qbtn = QPushButton('Quit', self)
        self.qbtn.resize(50, self.btn_y_size)
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        
        hbox = QHBoxLayout()
        hbox.addStretch(100)
        hbox.addWidget(self.qbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(100)
        vbox.addLayout(hbox)
        
        self.setLayout(hbox)
        
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        
        #упраление окошком
        self.setGeometry(100, 100, 1000, 700)
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
    def previous_brown(self):
        self.image_way = 'C:\\Users\\zamot\\OneDrive\\Рабочий стол\\машушик\\github\Application-programming-laba-1-2\\dataset\dataset_name\\brown_bears_0000.jpg'
        if os.path.isfile(str(self.image_way)):
            image = QPixmap(self.image_way)
            image.scaled
            self.lbl = QLabel(self)
            self.lbl.setPixmap(image)
            self.lbl.adjustSize()
            self.lbl.move(100, 1)
            self.lbl.show()
        else:
            print('image dont find')
    def next_brown(self):
        print("") 
    def previous_polar(self):
        print("")
    def next_polar(self):
        print("")          
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