
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI() 

    #инициализация пользовательского интерфейса
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))#установка шрифта подсказки
    
        
        #упраление кнопкой
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')#установка подсказки
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        #кнопка выхода - закрытия окна
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)
        
        #упраление окошком
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()
    
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

    ex = Example()

    sys.exit(app.exec_())