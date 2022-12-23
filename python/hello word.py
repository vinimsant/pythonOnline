import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class Calculador(QMainWindow()):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)