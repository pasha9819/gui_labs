from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPen, QPainter


class RectanglePainter(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.begin = QPoint()
        self.end = QPoint()
        self.setGeometry(0, 0, 0, 0)
        self.pixmap = None
        self.rectangles = []
        self.pen = QPen(Qt.red, 3, Qt.SolidLine)
        self.show()

    def paintEvent(self, event):
        if self.pixmap is not None:
            qp = QPainter(self)
            qp.drawPixmap(0, 0, self.pixmap)
            if self.begin != self.end:
                qp.setPen(self.pen)
                qp.drawRect(QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        self.drawRect()
        self.rectangles.append(QRect(self.begin, event.pos()))
        self.update()

    def setPixmap(self, pm: QPixmap):
        self.pixmap = pm

    def drawRect(self):
        if self.pixmap is not None:
            qp = QtGui.QPainter(self.pixmap)
            qp.setPen(self.pen)
            qp.drawRect(QtCore.QRect(self.begin, self.end))

