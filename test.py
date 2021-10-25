import sys
from PyQt6 import uic,  QtCore, QtGui, QtWidgets
import time
import sys
import os
from PyQt6.QtWidgets import *

class page(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("bar_hide.ui",self)
        self.setWindowTitle("bar hide")
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)



    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()
     




app = QApplication(sys.argv)
window = page()
window.show()
sys.exit(app.exec())