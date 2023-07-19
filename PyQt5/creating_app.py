import sys # uygulamayı konsoldan çalıştıracağımız için gerekli kütüphane
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv) # Komutları uygulamaya aktarma
    win = QMainWindow() # pencere oluşturmak için

    win.setWindowTitle("First Application") # Uygulama ismi
    win.setGeometry(200,200,1920,1080) # Yatayda 200, dikeyde 200 pixel aşağı iner ve pencere boyutunu ayarlar
    win.setWindowIcon(QIcon("icon.png")) # Uygulamaya ikon ekleme
    win.setToolTip("My tool tip")

    win.show() # hazırladığımız pencere ekranda gösterilir
    sys.exit(app.exec_()) # Çarpı ikonuna tıkladığımızda uygulama kapanacak

window()