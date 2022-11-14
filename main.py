import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import Principal

if __name__ == "__main__":

    """
    inicio de la aplicacion y creacion de la ventana principal de la aplicacion. 
    """
    app = QApplication(sys.argv)
    apli = Principal.Principal()
    apli.show()
    apli.setWindowTitle("Tic-tac-toe")
    apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
    sys.exit(app.exec_())