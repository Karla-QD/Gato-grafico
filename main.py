import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import Principal

if __name__ == "__main__":
    #se crea la aplicacion
    app = QApplication(sys.argv)
    #se crea la ventana principal
    apli = Principal.Principal()
    #se muestra la ventana
    apli.show()
    #se le pone un titulo a la ventana
    apli.setWindowTitle("Tic-tac-toe")
    #se le pone un icono a la ventana
    apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
    #se ejecuta la aplicacion
    sys.exit(app.exec_())