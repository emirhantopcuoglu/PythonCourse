import sys
from PyQt5 import QtWidgets
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True) # varsayılan olarak seçili
        self.ui.radioLise.setChecked(True) # varsayılan olarak seçili

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radiyoYunanistan.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUni.toggled.connect(self.onClickedEgitim)
        self.ui.radiIlkokul.toggled.connect(self.onClickedEgitim)
        self.ui.radiYuksek.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen ülke: " + rb.text())

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen eğitim: " + rb.text()),
    
    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen ülke: " + rb.text())

    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblEgitim.setText("Seçilen eğitim: " + rb.text())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()