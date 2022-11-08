import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
import Principal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apli = Principal.Principal()
    apli.show()
    apli.setWindowTitle("Tic-tac-toe")
    apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
    sys.exit(app.exec_())