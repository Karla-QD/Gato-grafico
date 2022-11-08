
import sys
import random
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
        apli = Jugador_Jugador()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)


    def j_vs_cpu(self):

        apli = Juego()
        apli.show()
        apli.setWindowTitle("Tic-tac-toe")
        apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
        apli.set_turno(1)


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

class Juego(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/game.ui", self)
        self.turno:int = 1      # 1 = X, 0 = O
        self.matriz_len:int = 3
        self.gano = False
        self.matriz = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
        self.modo:int = self.dificultad.currentIndex()

        self.button_00.clicked.connect(lambda:self.botones_jugador("00"))
        self.button_01.clicked.connect(lambda:self.botones_jugador("01"))
        self.button_02.clicked.connect(lambda:self.botones_jugador("02"))
        self.button_10.clicked.connect(lambda:self.botones_jugador("10"))
        self.button_11.clicked.connect(lambda:self.botones_jugador("11"))
        self.button_12.clicked.connect(lambda:self.botones_jugador("12"))
        self.button_20.clicked.connect(lambda:self.botones_jugador("20"))
        self.button_21.clicked.connect(lambda:self.botones_jugador("21"))
        self.button_22.clicked.connect(lambda:self.botones_jugador("22"))
        self.dificultad.currentIndexChanged.connect(self.set_modo)
        self.regresarJC.clicked.connect(self.cerrar)
        # si se reinicia el juego se reinicia la matriz y el turno y se limpian los botones de la interfaz grafica

        self.reiniciaButton.clicked.connect(self.resetear)
    def resetear(self):
        self.turno = 1
        self.matriz = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]
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
    def cerrar(self):
        self.close()

    def set_modo(self):
        self.modo = self.dificultad.currentIndex()
    def set_turno(self, turno:int):
       self.turno = turno

    def print_matriz(self):
        for i in range(self.matriz_len):
            for j in range(self.matriz_len):
                print(self.matriz[i][j], end = ", ")
            print()
        print()

    def gana(self) -> str:
        ganador:str = "-1"
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
    def llamar_valor(self, i:int):
        if i == 0: return self.matriz[0][0]
        if i == 1: return self.matriz[0][1]
        if i == 2: return self.matriz[0][2]
        if i == 3: return self.matriz[1][0]
        if i == 4: return self.matriz[1][1]
        if i == 5: return self.matriz[1][2]
        if i == 6: return self.matriz[2][0]
        if i == 7: return self.matriz[2][1]
        if i == 8: return self.matriz[2][2]
        
    def modificar_matriz(self, i:int, valor:str):
        turno_icon = QtGui.QIcon("resource/o.png")
        if i == 0: 
            self.matriz[0][0] = valor
            self.button_00.setIcon(turno_icon)
            return
        if i == 1:  
            self.matriz[0][1] = valor
            self.button_01.setIcon(turno_icon)
            return
        if i == 2:
            self.matriz[0][2] = valor
            self.button_02.setIcon(turno_icon)
            return
        if i == 3:
            self.matriz[1][0]= valor
            self.button_10.setIcon(turno_icon)
            return
        if i == 4:  
            self.matriz[1][1]= valor
            self.button_11.setIcon(turno_icon)
            return
        if i == 5:  
            self.matriz[1][2]= valor
            self.button_12.setIcon(turno_icon)
            return
        if i == 6:  
            self.matriz[2][0]= valor
            self.button_20.setIcon(turno_icon)
            return
        if i == 7:  
            self.matriz[2][1]= valor
            self.button_21.setIcon(turno_icon)
            return
        if i == 8:  
            self.matriz[2][2]= valor
            self.button_22.setIcon(turno_icon)
            return
        
    def interpretar_jugador(self, jug:str):
        if jug == "x": return -1
        if jug == "o": return 1
        if jug == "-1": return 0
        return 0
    def interpretar_jugador_inverso(self, jug:int):
        if jug == -1: return "x"
        if jug == 1: return "o"
        if jug == 0: return "-1"
        return "-1"
    
    def interpretar_matriz(self):
        aux = []
        for i in range(self.matriz_len):
            for j in range(self.matriz_len):
                aux.append(self.matriz[i][j])
        return aux

    def botones_jugador(self, valor: str):

        if self.modo == 0:
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")
                return

            if (valor == "AI"): pass
            elif self.matriz[int(valor[0])][int(valor[1])] == "x" or self.matriz[int(valor[0])][int(valor[1])] == "o": return

            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            if self.turno % 2 == 0:
                turno_icon = QtGui.QIcon("resource/o.png")
                turno_letra = "o"
                vacio:bool = False # Easy level starts, fix AI turn, delete this to PVP.
                i:int = -1
                j:int = -1
                while not vacio:
                    i = random.randint(0, 2)
                    j = random.randint(0, 2)
                    if self.matriz[i][j] == -1:
                        vacio = True
                valor = str(i) + str(j)
                print(f'Estoy jugando en una pos. random: {i},{j}')

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
                        if self.matriz[i][j] == -1: self.matriz[i][j] = "x"
                self.print_matriz()
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                elif (self.gana() == "o"):
                    self.mensaje.setText("El CPU ganó")

                else :self.mensaje.setText("Empate")
                return
            self.matriz[int(valor[0])][int(valor[1])] = turno_letra
            self.print_matriz()
            self.turno += 1
            if self.turno % 2 == 0: self.botones_jugador("AI")
            if self.gana() != "-1":
                if(self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")
                return
            
        if self.modo == 1:
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")
                return

            if (valor == "AI"):
                pass
            elif self.matriz[int(valor[0])][int(valor[1])] == "x" or self.matriz[int(valor[0])][int(valor[1])] == "o":
                return

            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            if self.turno % 2 == 0:
                turno_icon = QtGui.QIcon("resource/o.png")
                turno_letra = "o"
                vacio: bool = False
                sigue: bool = False
                i: int = -1
                j: int = -1
                if ((self.matriz[1][1] == self.matriz[0][0] == "o" and self.matriz[2][2] == -1) or (
                        self.matriz[0][2] == self.matriz[1][2] == "o" and self.matriz[2][2] == -1)
                        or (self.matriz[2][0] == self.matriz[2][1] == "o" and self.matriz[2][2] == -1)):
                    valor = str(2) + str(2)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[0][1] == "x" and self.matriz[0][2] == -1) or (self.matriz[2][0] ==
                                                                                                    self.matriz[1][
                                                                                                        1] == "x" and
                                                                                                    self.matriz[0][
                                                                                                        2] == -1) or (
                        self.matriz[2][2] == self.matriz[1][2] == "x" and self.matriz[0][2] == -1)):
                    valor = str(0) + str(2)
                    vacio = True
                if ((self.matriz[1][0] == self.matriz[1][1] == "x" and self.matriz[1][2] == -1) or (
                        self.matriz[0][2] == self.matriz[2][2] == "x"
                        and self.matriz[1][2] == -1)):
                    valor = str(1) + str(2)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[1][1] == "x" and self.matriz[2][2] == -1) or (
                        self.matriz[2][0] == self.matriz[2][1] == "x"
                        and self.matriz[2][2] == -1) or (
                        self.matriz[0][2] == self.matriz[1][2] == "x" and self.matriz[2][2] == -1)):
                    valor = str(2) + str(2)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[0][2] == "x" and self.matriz[0][1] == -1) or (
                        self.matriz[1][1] == self.matriz[2][1] == "x"
                        and self.matriz[0][1] == -1)):
                    valor = str(0) + str(1)
                    vacio = True
                if ((self.matriz[1][0] == self.matriz[1][2] == "x" and self.matriz[1][1] == -1) or (
                        self.matriz[0][0] == self.matriz[2][2] == "x" and self.matriz[1][1] == -1)
                        or (self.matriz[0][1] == self.matriz[2][1] == "x" and self.matriz[1][1] == -1)):
                    valor = str(1) + str(1)
                    vacio = True
                if ((self.matriz[0][1] == self.matriz[1][1] == "x" and self.matriz[2][1] == -1) or (
                        self.matriz[2][0] == self.matriz[2][2] == "x"
                        and self.matriz[2][1] == -1)):
                    valor = str(2) + str(1)
                    vacio = True
                if ((self.matriz[0][1] == self.matriz[0][2] == "x" and self.matriz[0][0] == -1) or (
                        self.matriz[1][1] == self.matriz[2][2] == "x" and self.matriz[0][0] == -1)
                        or (self.matriz[1][0] == self.matriz[2][0] == "x" and self.matriz[0][0] == -1)):
                    valor = str(0) + str(0)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[2][0] == "x" and self.matriz[1][0] == -1) or (
                        self.matriz[1][1] == self.matriz[1][2] == "x"
                        and self.matriz[1][0] == -1)):
                    valor = str(1) + str(0)
                    vacio = True
                if ((self.matriz[1][1] == self.matriz[0][2] == "x" and self.matriz[2][0] == -1) or (
                        self.matriz[2][1] == self.matriz[2][2] == "x" and self.matriz[2][0] == -1)
                        or (self.matriz[0][0] == self.matriz[1][0] == "x" and self.matriz[2][0] == -1)):
                    valor = str(2) + str(0)
                    vacio = True
                if ((self.matriz[1][1] == self.matriz[0][2] == "x" and self.matriz[2][0] == -1) or (
                        self.matriz[2][1] == self.matriz[2][2] == "x" and self.matriz[2][0] == -1)
                        or (self.matriz[0][0] == self.matriz[1][0] == "x" and self.matriz[2][0] == -1)):
                    valor = str(2) + str(0)
                    vacio = True
                if (vacio == False):
                    while not sigue:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.matriz[i][j] == -1:
                            valor = str(i) + str(j)
                            sigue = True

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
                        if self.matriz[i][j] == -1: self.matriz[i][j] = "x"
                self.print_matriz()
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                elif (self.gana() == "o"):
                    self.mensaje.setText("El CPU ganó")

                else:
                    self.mensaje.setText("Empate")
                return
            self.matriz[int(valor[0])][int(valor[1])] = turno_letra
            self.print_matriz()
            self.turno += 1
            if self.turno % 2 == 0: self.botones_jugador("AI")
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")

                return
# metodo para cpu contra jugador usando arboles de decision

        if self.modo == 2:
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")
                return

            if (valor == "AI"): pass
            elif self.matriz[int(valor[0])][int(valor[1])] == "x" or self.matriz[int(valor[0])][int(valor[1])] == "o": return

            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            if self.turno % 2 == 0:
                self.jugar_cpu_dificil()
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
                        if self.matriz[i][j] == -1: self.matriz[i][j] = "x"
                self.print_matriz()
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                elif (self.gana() == "o"):
                    self.mensaje.setText("El CPU ganó")

                else :self.mensaje.setText("Empate")
                return
            if self.turno % 2 != 0: self.matriz[int(valor[0])][int(valor[1])] = turno_letra
            self.print_matriz()
            self.turno += 1
            if self.turno % 2 == 0: self.botones_jugador("AI")
            if self.gana() != "-1":
                if(self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")
                return

    def arboles_decision(self, jugador:int, matriz_aux:[]):
        var = self.posibilidades(matriz_aux)
        if  var!= 0:
            return var * jugador
        indice = -1
        valor = -2
        for i in range(0, 9) :
            if self.interpretar_jugador(matriz_aux[i]) == 0:
                matriz_aux[i] = self.interpretar_jugador_inverso(jugador)
                puntaje =-self.arboles_decision((jugador * -1), matriz_aux)
                if puntaje > valor:
                    valor = puntaje
                    indice = i
                matriz_aux[i] = self.interpretar_jugador_inverso(0) # -1 = 0, esta vacio
        if indice == -1:
            return 0
        return valor
                
    def jugar_cpu_dificil(self):
        indice = -1
        valor = -2
        matriz_aux = self.interpretar_matriz()
        for i in range (0, 9):
            if self.interpretar_jugador(matriz_aux[i]) == 0:
                matriz_aux[i] = self.interpretar_jugador_inverso(1)
                puntaje =-self.arboles_decision(-1, matriz_aux)
                matriz_aux[i] = self.interpretar_jugador_inverso(0)
                if puntaje > valor:
                    valor = puntaje
                    indice= i
        self.modificar_matriz(indice, "o")
    
    def posibilidades(self, matriz):
        mat = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
        for i in range(0,8):
            if(self.interpretar_jugador(matriz[mat[i][0]]) != 0 and
               self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][1]]) and
               self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][2]])):
                return self.interpretar_jugador(matriz[mat[i][2]]); # si hay un ganador, se retorna el valor del ganador
        return 0;

        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apli = Principal()
    apli.show()
    apli.setWindowTitle("Tic-tac-toe")
    apli.setWindowIcon(QtGui.QIcon("resource/tic-tac-toe.png"))
    sys.exit(app.exec_())