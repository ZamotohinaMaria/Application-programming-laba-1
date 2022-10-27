
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QCheckBox, 
    QPushButton, QApplication, QMessageBox, QMainWindow,
    QHBoxLayout, QVBoxLayout, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Window( QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI() 
    #ДОБАВИТЬ QSplitter ДЛЯ КРАСОТЫ!!!!!! (виджеты часть 2)
    #инициализация пользовательского интерфейса
    def initUI(self):
        
        self.btn_x_size = 300
        self.btn_y_size = 40
        
        self.btn_create_csv = QPushButton('Создать аннотацию для исходного датасета', self)
        self.btn_create_csv.setGeometry(50, 50, self.btn_x_size, self.btn_y_size)
        
        self.btn_copy_dataset_name = QPushButton('Копировать датасет с новыми именами', self)
        self.btn_copy_dataset_name.setGeometry(50, 90, self.btn_x_size, self.btn_y_size)
        
        self.csv_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_name_checkbox.setGeometry(350, 90, 200, 40)
        self.csv_name_checkbox.toggle()
        self.csv_name_checkbox.stateChanged.connect(self.name_checkbox)
        
        self.btn_copy_dataset_name = QPushButton('Копировать датасет с рандомными именами', self)
        self.btn_copy_dataset_name.setGeometry(50, 130, self.btn_x_size, self.btn_y_size)
        
        self.csv_random_name_checkbox = QCheckBox('Создать аннотацию для датасета', self)
        self.csv_random_name_checkbox.setGeometry(350, 130, 200, 40)
        self.csv_random_name_checkbox.toggle()
        self.csv_random_name_checkbox.stateChanged.connect(self.random_name_checkbox)
        
        self.brown_bears_label = QLabel('Бурые мишки', self)
        self.brown_bears_label.setAlignment(Qt.AlignCenter)
        self.brown_bears_label.setGeometry(150, 170, 100, 40)
        
        self.brown_bears_previous = QPushButton('<---', self)
        self.brown_bears_previous.setGeometry(50, 170, self.btn_x_size/3, self.btn_y_size)
        
        self.brown_bears_next = QPushButton('--->', self)
        self.brown_bears_next.setGeometry(250, 170, self.btn_x_size/3, self.btn_y_size)
        
        self.polar_bears_label = QLabel('Бурые мишки', self)
        self.polar_bears_label.setAlignment(Qt.AlignCenter)
        self.polar_bears_label.setGeometry(150, 210, 100, 40)
        
        self.polar_bears_previous = QPushButton('<---', self)
        self.polar_bears_previous.setGeometry(50, 210, self.btn_x_size/3, self.btn_y_size)
        
        self.polar_bears_next = QPushButton('--->', self)
        self.polar_bears_next.setGeometry(250, 210, self.btn_x_size/3, self.btn_y_size)
        
        #кнопка выхода - закрытия окна
        self.qbtn = QPushButton('Quit', self)
        self.qbtn.resize(50, 25)
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        
        hbox = QHBoxLayout()
        hbox.addStretch(100)
        hbox.addWidget(self.qbtn)

        vbox = QVBoxLayout()
        vbox.addStretch(100)
        vbox.addLayout(hbox)
        
        self.setLayout(hbox)
        
        #упраление окошком
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def name_checkbox(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('name_checkbox')
        else:
            self.setWindowTitle('')
            
    def random_name_checkbox(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('random_name_checkbox')
        else:
            self.setWindowTitle('')
                   
    #messege box при закрытии
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv) #объект приложение, должен быть всегда, принимает на вход аргументы командной строки

    ex = Window()

    sys.exit(app.exec_())