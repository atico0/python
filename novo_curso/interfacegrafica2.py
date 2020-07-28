import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QGridLayout


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora pica')
        self.setFixedSize(400,400)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()