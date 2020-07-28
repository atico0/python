import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Botoes(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


qt = QApplication(sys.argv)
bt = Botoes()
bt.show()
qt.exec_()