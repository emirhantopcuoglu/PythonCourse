import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.cbSinema.stateChanged.connect(self.show_state)
        # self.ui.cbKitap.stateChanged.connect(self.show_state)
        # self.ui.cbSpor.stateChanged.connect(self.show_state)
        # self.ui.cbMatematik.stateChanged.connect(self.show_state)
        # self.ui.cbProgramlama.stateChanged.connect(self.show_state)
        # self.ui.cbWeb.stateChanged.connect(self.show_state)
        self.ui.btnKaydet.clicked.connect(self.getAllHobiler)
        self.ui.btnKaydet_2.clicked.connect(self.getAllDersler)
    
    def getAllHobiler(self):
        result = ""
        items = self.ui.hobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + "\n"
        self.ui.lblresult.setText(result)
    def getAllDersler(self):
        result = ""
        items = self.ui.dersler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + "\n"
        self.ui.lblresult.setText(result)
    def show_state(self, value):
        cb = self.sender()
        print(value,cb.isChecked(),cb.text())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()