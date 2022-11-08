from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

class Jugador_Jugador(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/game_j_vs_j.ui", self)
        self.turno: int = 1  # 1 = X, 0 = O
        self.matriz_len: int = 3
        self.gano = False
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

        self.button_00.clicked.connect(lambda: self.botones_jugador("00"))
        self.button_01.clicked.connect(lambda: self.botones_jugador("01"))
        self.button_02.clicked.connect(lambda: self.botones_jugador("02"))
        self.button_10.clicked.connect(lambda: self.botones_jugador("10"))
        self.button_11.clicked.connect(lambda: self.botones_jugador("11"))
        self.button_12.clicked.connect(lambda: self.botones_jugador("12"))
        self.button_20.clicked.connect(lambda: self.botones_jugador("20"))
        self.button_21.clicked.connect(lambda: self.botones_jugador("21"))
        self.button_22.clicked.connect(lambda: self.botones_jugador("22"))
        self.regresarJ_J.clicked.connect(self.cerrar)
        #si se reinicia el juego, se reinicia la matriz y se vuelve a poner el turno en 1 para que empiece el jugador 1
        self.reinicioButton.clicked.connect(self.resetear)
    def cerrar(self):
        self.close()
    def resetear(self):
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.turno = 1
        self.gano = False
        self.button_00.setIcon(QtGui.QIcon())
        self.button_01.setIcon(QtGui.QIcon())
        self.button_02.setIcon(QtGui.QIcon())
        self.button_10.setIcon(QtGui.QIcon())
        self.button_11.setIcon(QtGui.QIcon())
        self.button_12.setIcon(QtGui.QIcon())
        self.button_20.setIcon(QtGui.QIcon())
        self.button_21.setIcon(QtGui.QIcon())
        self.button_22.setIcon(QtGui.QIcon())
        self.mensaje.setText("")
    def set_turno(self, turno: int):
        self.turno = turno

    def print_matriz(self):
        for i in range(self.matriz_len):
            for j in range(self.matriz_len):
                print(self.matriz[i][j], end=", ")
            print()
        print()

    def gana(self) -> str:
        ganador: str = "-1"
        if (self.matriz[0][0] == self.matriz[0][1] == self.matriz[0][2] and
                self.matriz[0][0] != -1):
            ganador = self.matriz[0][0]
            self.gano = True
            return ganador
        if (self.matriz[1][0] == self.matriz[1][1] == self.matriz[1][2] and
                self.matriz[1][0] != -1):
            ganador = self.matriz[1][0]
            self.gano = True
            return ganador
        if (self.matriz[2][0] == self.matriz[2][1] == self.matriz[2][2] and
                self.matriz[2][0] != -1):
            ganador = self.matriz[2][0]
            self.gano = True
            return ganador
        if (self.matriz[0][0] == self.matriz[1][0] == self.matriz[2][0] and
                self.matriz[0][0] != -1):
            ganador = self.matriz[0][0]
            self.gano = True
            return ganador
        if (self.matriz[0][1] == self.matriz[1][1] == self.matriz[2][1] and
                self.matriz[0][1] != -1):
            ganador = self.matriz[0][1]
            self.gano = True
            return ganador
        if (self.matriz[0][2] == self.matriz[1][2] == self.matriz[2][2] and
                self.matriz[0][2] != -1):
            ganador = self.matriz[0][2]
            self.gano = True
            return ganador
        if (self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] and
                self.matriz[0][0] != -1):
            ganador = self.matriz[0][0]
            self.gano = True
            return ganador
        if (self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] and
                self.matriz[0][2] != -1):
            ganador = self.matriz[0][2]
            self.gano = True
            return ganador
        return ganador

    def botones_jugador(self, valor: str):
        if self.gana() != "-1":
            if (self.gana() == "x"):
                self.mensaje.setText("El jugador 1 ganó")
            else:
                self.mensaje.setText("El jugador 2 ganó")
            return

        if self.matriz[int(valor[0])][int(valor[1])] == "x" or self.matriz[int(valor[0])][int(valor[1])] == "o": return

        if self.turno % 2 != 0:
            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
        if self.turno % 2 == 0:
            turno_icon = QtGui.QIcon("resource/o.png")
            turno_letra = "o"

        if (valor == "00"): self.button_00.setIcon(turno_icon)
        if (valor == "01"): self.button_01.setIcon(turno_icon)
        if (valor == "02"): self.button_02.setIcon(turno_icon)
        if (valor == "10"): self.button_10.setIcon(turno_icon)
        if (valor == "11"): self.button_11.setIcon(turno_icon)
        if (valor == "12"): self.button_12.setIcon(turno_icon)
        if (valor == "20"): self.button_20.setIcon(turno_icon)
        if (valor == "21"): self.button_21.setIcon(turno_icon)
        if (valor == "22"): self.button_22.setIcon(turno_icon)

        if self.turno == 9:
            for i in range(self.matriz_len):
                for j in range(self.matriz_len):
                    if self.matriz[i][j] == -1:
                        self.matriz[i][j] = "x"
            self.print_matriz()
            if (self.gana() == "x"):
                self.mensaje.setText("El jugador 1 ganó")
            elif (self.gana() == "o"):
                self.mensaje.setText("El jugador 2 ganó")
            else:
                self.mensaje.setText("Empate")
            return
        self.matriz[int(valor[0])][int(valor[1])] = turno_letra
        self.print_matriz()
        self.turno += 1
        if self.gana() != "-1":
            if (self.gana() == "x"):
                self.mensaje.setText("El jugador 1 ganó")
            else:
                self.mensaje.setText("El jugador 2 ganó")
            return
