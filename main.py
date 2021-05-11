import sys
import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow
from MRZ_UI import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.main_wind = QMainWindow
        self.uic = Ui_MainWindow

        self.ButtonVNM.clicked.connect(self.Cal_VNM)
        self.ButtonUSA.clicked.connect(self.Cal_USA)

    def show(self):
        self.main_wind.show()

    def Cal_VNM(self):
        print("VNM")

    def Cal_USA(self):
        print("USA")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
