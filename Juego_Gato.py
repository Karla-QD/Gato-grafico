import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
import colorsys as cs #importamos la libreria colorsys

class Juego_Gato(QMainWindow):
    def __init__(self, pushButton=None):
        super(Juego_Gato, self).__init__()
        uic.loadUi("resource/game.ui", self)
        colorsys = cs.hsv_to_rgb(0.5, 0.5, 0.5)
        self.setStyleSheet("background-color: rgb(%d, %d, %d);" % (colorsys[0]*250, colorsys[1]*250, colorsys[2]*250))
        self.setWindowTitle("GATO")
        self.label_00.setPixmap(QPixmap("resource/X.png"))
        self.label_01.setPixmap(QPixmap("resource/X.png"))
        self.label_02.setPixmap(QPixmap("resource/O.png"))
        self.label_12.setPixmap(QPixmap("resource/O.png"))
    """
    un textfild que hagarre el numero de la posicion, un lbl en blanco al que se le setea texto y jugadores
    Ponerle numero a las casillas, lbl abajo que muestre los resultados del juego
    """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Juego_Gato()
    GUI.show()

    sys.exit(app.exec_())
