from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('c_p.ui', None)
        self.ui.show()

        self.ui.setWindowTitle("Color Picker")
        self.ui.red.valueChanged.connect(self.pick_color)
        self.ui.green.valueChanged.connect(self.pick_color)
        self.ui.blue.valueChanged.connect(self.pick_color)

    def pick_color(self):

        self.ui.line_red.setText(str(self.ui.red.value()))
        self.ui.line_green.setText(str(self.ui.green.value()))
        self.ui.line_blue.setText(str(self.ui.blue.value()))


        self.ui.tb_1.setStyleSheet(F"background-color: rgb({self.ui.red.value()}, {self.ui.green.value()}, {self.ui.blue.value()});")
        self.ui.tb_1.setText(str(F"rgb({self.ui.red.value()}, {self.ui.green.value()}, {self.ui.blue.value()}"))

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()