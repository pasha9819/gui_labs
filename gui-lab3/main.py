import sys
from PyQt5 import QtWidgets

from PyQt5.QtCore import QRect, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QLineEdit, QLabel

from bin_holder import BinHolder
from hex_holder import HexHolder

WINDOW_WIDTH = 360
WINDOW_HEIGHT = 200


class Screen(QtWidgets.QMainWindow):
    def __init__(self):
        super(Screen, self).__init__()

        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.binHolder = BinHolder()
        self.hexHolder = HexHolder()

        self.defaultFont = QFont("Times New Roman", 14)

        self.convertButton = QPushButton(self)
        self.convertButton.setFont(self.defaultFont)
        self.convertButton.setText("Конвертировать")
        self.convertButton.setGeometry(QRect(100, 160, 160, 25))

        self.decLineEdit = QLineEdit(self)
        self.decLineEdit.setGeometry(QRect(70, 20, 280, 25))
        self.decLineEdit.setValidator(QIntValidator())
        self.decLineEdit.setFont(self.defaultFont)
        self.decLabel = QLabel(self)
        self.decLabel.setFont(self.defaultFont)
        self.decLabel.setText("DEC")
        self.decLabel.setGeometry(QRect(10, 20, 40, 25))

        self.binLineEdit = QLineEdit(self)
        self.binLineEdit.setGeometry(QRect(70, 60, 280, 25))
        self.binLineEdit.setReadOnly(True)
        self.binLineEdit.setFont(self.defaultFont)
        self.binLabel = QLabel(self)
        self.binLabel.setFont(self.defaultFont)
        self.binLabel.setText("BIN")
        self.binLabel.setGeometry(QRect(10, 60, 40, 25))

        self.hexLineEdit = QLineEdit(self)
        self.hexLineEdit.setGeometry(QRect(70, 100, 280, 25))
        self.hexLineEdit.setReadOnly(True)
        self.hexLineEdit.setFont(self.defaultFont)
        self.hexLabel = QLabel(self)
        self.hexLabel.setFont(self.defaultFont)
        self.hexLabel.setText("HEX")
        self.hexLabel.setGeometry(QRect(10, 100, 40, 25))

        self.binHolder.update_signal.connect(self.binHolder.update_value)
        self.hexHolder.update_signal.connect(self.hexHolder.update_value)

        self.convertButton.clicked.connect(self.on_convert_button_click)

        self.show()

    def on_convert_button_click(self):
        text_val = self.decLineEdit.text()
        if text_val is None or len(text_val) == 0:
            val = 0
        else:
            val = int(text_val)
        self.binHolder.update_signal.emit(val)
        self.hexHolder.update_signal.emit(val)
        self.binLineEdit.setText(self.binHolder.value)
        self.hexLineEdit.setText(self.hexHolder.value)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    ex = Screen()
    sys.exit(application.exec_())
