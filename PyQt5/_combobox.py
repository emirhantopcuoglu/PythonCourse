import sys
from PyQt5 import QtWidgets
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbSehirler
        # combo.addItem("İstanbul")
        # combo.addItem("Ankara")
        # combo.addItem("İzmir")
        # combo.addItems(["Adana","Kocaeli","Rize"])

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnGetItem.clicked.connect(self.GetItems)
    def LoadItems(self):
        sehirler = ["Adana","Kocaeli","Rize"]
        self.ui.cbSehirler.addItems(sehirler)

    def GetItems(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())
        print(self.ui.cbSehirler.count())
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()