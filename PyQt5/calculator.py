import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(300,300,700,850)
        self.setWindowIcon(QIcon("calculator.png"))
        self.setToolTip("Hesap Makinesi")
        self.initUI()
    
    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Sayı 1: ")
        self.lbl_num1.move(50,50)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Sayı 2: ")
        self.lbl_num2.move(50,150)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Sonuç: ")
        self.lbl_result.move(50,300)
        self.lbl_result.resize(500,30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(250,50)
        self.txt_num1.resize(100,30)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(250,150)
        self.txt_num2.resize(100,30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText("Topla (+)")
        self.btn1.move(50,250)
        self.btn1.clicked.connect(self.topla)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText("Çıkar (-)")
        self.btn2.move(200,250)
        self.btn2.clicked.connect(self.cikar)

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setText("Çarp (x)")
        self.btn3.move(350,250)
        self.btn3.clicked.connect(self.carp)

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setText("Böl (/)")
        self.btn4.move(500,250)
        self.btn4.clicked.connect(self.bol)

    def topla(self):
        result = str(int(self.txt_num1.text()) + int(self.txt_num2.text())) 
        self.lbl_result.setText("Sonuç: " + result)
    def cikar(self):
        result = str(int(self.txt_num1.text()) - int(self.txt_num2.text()))
        self.lbl_result.setText("Sonuç: " + result)
    def carp(self):
        result = str(int(self.txt_num1.text()) * int(self.txt_num2.text()))
        self.lbl_result.setText("Sonuç: " + result)
    def bol(self):
        if int(self.txt_num1.text()) == 0 and int(self.txt_num2.text()) == 0:
            self.lbl_result.setText("Sonuç: Belirsiz")
        elif int(self.txt_num2.text()) == 0:
            self.lbl_result.setText("Sonuç: Tanımsız")
        else:
            result = str(int(self.txt_num1.text()) / int(self.txt_num2.text()))
            self.lbl_result.setText("Sonuç: " + result)

def window():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

window()