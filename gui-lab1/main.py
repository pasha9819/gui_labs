import datetime
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel

WIDTH = 200
HEIGHT = 100


class Screen(QtWidgets.QMainWindow):
    def __init__(self):
        super(Screen, self).__init__()

        self.setFixedSize(WIDTH, HEIGHT)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(25, 15, 150, 25))
        self.button = QPushButton(self)
        self.button.setText("Текущее время")
        self.button.setGeometry(QRect(25, 60, 150, 25))

        self.button.clicked.connect(self.on_click)
        self.on_click()

        self.show()

    def on_click(self):
        self.label.setText(str(datetime.datetime.now()))

if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = Screen()
    sys.exit(application.exec_())
