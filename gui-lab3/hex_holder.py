from PyQt5.QtCore import pyqtSignal, QObject


class HexHolder(QObject):
    update_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.value = ''

    def update_value(self, new_value: int):
        self.value = hex(new_value).upper()
        if new_value < 0:
            self.value = '-' + self.value[3:]
        else:
            self.value = self.value[2:]
