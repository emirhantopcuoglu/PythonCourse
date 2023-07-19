import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("First Application") # Uygulama ismi
        self.setGeometry(200,200,1920,1080) # Yatayda 200, dikeyde 200 pixel aşağı iner ve pencere boyutunu ayarlar
        self.setWindowIcon(QIcon("icon.png")) # Uygulamaya ikon ekleme
        self.setToolTip("My tool tip")
        self.initUI()

    def initUI(self): # Pencere üzerindeki elemanların özelliklerinin tanımlandığı fonksiyon
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)

        self.txt_name = QtWidgets.QLineEdit(self) 
        self.txt_name.move(150,30) # Textbox konumu
        self.txt_name.resize(200,32) # Textbox büyüklüğü

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70) # Textbox konumu
        self.txt_surname.resize(200,32) # Textbox büyüklüğü

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText("Hoşgeldin " + self.txt_name.text() + " " + self.txt_surname.text())

def window():
    app = QApplication(sys.argv) # Komutları uygulamaya aktarma
    win = MyWindow() # win nesnesi oluşturma
    win.show()
    sys.exit(app.exec_()) # Çarpı ikonuna tıkladığımızda uygulama kapanacak

window()