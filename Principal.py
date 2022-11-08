import sys
import Juego
import Jugador_Jugador
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/principal.ui", self)
        #si se presiona el boton de jugador contra jugador, se abre la ventana de juego
        self.jvsjButton.clicked.connect(self.j_vs_j)
        # si se presiona el boton de jugar contra la cpu, se abre la ventana de juego
        self.jcpu.clicked.connect(self.j_vs_cpu)
        #si se presiona el boton de salir, se cierra la aplicacion
        self.finalizar.clicked.connect(self.cerrar)

    #se cierra la aplicacion
    def cerrar(self):
        sys.exit()
    def j_vs_j(self):
        #se abre la ventana de juego
        apli = Jugador_Jugador.Jugador_Jugador()
        #se muestra la ventana
        apli.show()
        #se le pone un titulo a la ventana
        apli.setWindowTitle("Tic-tac-toe")
        #se le pone un icono a la ventana
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        #se le pone el turno del jugador 1
        apli.set_turno(1)
    def j_vs_cpu(self):
        #se abre la ventana de juego
        apli = Juego.Juego()
        #se muestra la ventana
        apli.show()
        #se le pone un titulo a la ventana
        apli.setWindowTitle("Tic-tac-toe")
        #se le pone un icono a la ventana
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        #se le pone el turno del jugador 1
        apli.set_turno(1)
