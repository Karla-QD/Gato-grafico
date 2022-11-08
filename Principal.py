import sys
import Juego
import Jugador_Jugador
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/principal.ui", self)
        self.jvsjButton.clicked.connect(self.j_vs_j)
        self.jcpu.clicked.connect(self.j_vs_cpu)
        self.finalizar.clicked.connect(self.cerrar)
    def cerrar(self):
        sys.exit()
    def j_vs_j(self):
        apli = Jugador_Jugador.Jugador_Jugador()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)
    def j_vs_cpu(self):

        apli = Juego.Juego()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)
