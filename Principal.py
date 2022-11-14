import sys
import Juego
import Jugador_Jugador
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Principal(QMainWindow):
    """
    Explicacion
    la clase principal es la que se encarga de abrir las ventanas de juego, y de cerrar la aplicacion
    inicializa la ventana principal y la muestra asi como su titulo y su icono

    parametros:
    QMainWindow: clase de la que hereda la clase principal
    """
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/principal.ui", self)
        #si se presiona el boton de jugador contra jugador, se abre la ventana de juego
        self.jvsjButton.clicked.connect(self.j_vs_j)
        # si se presiona el boton de jugar contra la cpu, se abre la ventana de juego
        self.jcpu.clicked.connect(self.j_vs_cpu)
        #si se presiona el boton de salir, se cierra la aplicacion
        self.finalizar.clicked.connect(self.cerrar)

    def cerrar(self):
        sys.exit()

    #se abre la ventana de jugador vs jugador
    def j_vs_j(self):
        apli = Jugador_Jugador.Jugador_Jugador()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)

    #se abre la ventana de jugador vs cpu
    def j_vs_cpu(self):
        apli = Juego.Juego()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)
