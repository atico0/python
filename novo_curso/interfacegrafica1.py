import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from  PyQt5.QtWidgets import QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('meu ovo')
        self.grid.addWidget(self.btn)
        self.btn.clicked.connect(lambda: print('É grande'))
        self.setCentralWidget(self.cw)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()