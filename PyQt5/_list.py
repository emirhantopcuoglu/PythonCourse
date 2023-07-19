from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
import sys
from _listForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # load students
        self.loadStudents()

    def loadStudents(self):
        self.ui.listItems.addItems(["Ahmet","Mehmet","Can"])

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()