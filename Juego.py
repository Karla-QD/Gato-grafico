import random
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Juego(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("resource/game.ui", self)
        self.turno: int = 1  # 1 = X, 0 = O
        self.matriz_len: int = 3
        self.gano = False
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.modo: int = self.dificultad.currentIndex()

        # Conectar los botones con sus respectivos valores
        self.button_00.clicked.connect(lambda: self.botones_jugador("00"))
        self.button_01.clicked.connect(lambda: self.botones_jugador("01"))
        self.button_02.clicked.connect(lambda: self.botones_jugador("02"))
        self.button_10.clicked.connect(lambda: self.botones_jugador("10"))
        self.button_11.clicked.connect(lambda: self.botones_jugador("11"))
        self.button_12.clicked.connect(lambda: self.botones_jugador("12"))
        self.button_20.clicked.connect(lambda: self.botones_jugador("20"))
        self.button_21.clicked.connect(lambda: self.botones_jugador("21"))
        self.button_22.clicked.connect(lambda: self.botones_jugador("22"))
        self.dificultad.currentIndexChanged.connect(self.set_modo)
        # Conectar los botones de reset y cerrar
        self.regresarJC.clicked.connect(self.cerrar)
        # si se reinicia el juego se reinicia la matriz y el turno y se limpian los botones de la interfaz grafica
        self.reiniciaButton.clicked.connect(self.resetear)


    # reinicia el juego
    def resetear(self):
        self.turno = 1
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
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
        # cambia el modo de juego,  0 = facil, 1 = medio, 2 = dificil
        self.modo = self.dificultad.currentIndex()

    # funcion que se encarga de cambiar el turno
    def set_turno(self, turno: int):
        self.turno = turno

    # funcion que se encarga de imprimir la matriz en la consola
    def print_matriz(self):
        for i in range(self.matriz_len):
            for j in range(self.matriz_len):
                print(self.matriz[i][j], end=", ")
            print()
        print()

     #funcion que imprime si un jugador gano o no
    def gana(self) -> str:
        ganador: str = "-1"
        #verifica si hay un ganador en las filas, si sucede cambia el valor de ganador
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

    def llamar_valor(self, i: int):
        #se le asigna un valor a cada par de coordenadas
        if i == 0: return self.matriz[0][0]
        if i == 1: return self.matriz[0][1]
        if i == 2: return self.matriz[0][2]
        if i == 3: return self.matriz[1][0]
        if i == 4: return self.matriz[1][1]
        if i == 5: return self.matriz[1][2]
        if i == 6: return self.matriz[2][0]
        if i == 7: return self.matriz[2][1]
        if i == 8: return self.matriz[2][2]

    def modificar_matriz(self, i: int, valor: str):
        turno_icon = QtGui.QIcon("resource/o.png")
        #dependiendo del valor se le asigna un icono a la matriz, en la posicion correspondiente
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
            self.matriz[1][0] = valor
            self.button_10.setIcon(turno_icon)
            return
        if i == 4:
            self.matriz[1][1] = valor
            self.button_11.setIcon(turno_icon)
            return
        if i == 5:
            self.matriz[1][2] = valor
            self.button_12.setIcon(turno_icon)
            return
        if i == 6:
            self.matriz[2][0] = valor
            self.button_20.setIcon(turno_icon)
            return
        if i == 7:
            self.matriz[2][1] = valor
            self.button_21.setIcon(turno_icon)
            return
        if i == 8:
            self.matriz[2][2] = valor
            self.button_22.setIcon(turno_icon)
            return

    #funcion para verificar el turno del jugador y asignarle un valor
    def interpretar_jugador(self, jug: str):
        if jug == "x": return -1
        if jug == "o": return 1
        if jug == "-1": return 0
        return 0
    #funcion para verificar el valor y asignarle un icono
    def interpretar_jugador_inverso(self, jug: int):
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
        #si el modo de juego es facil, se ejecuta la siguiente funcion
        if self.modo == 0:
            #se verifica si gana el jugador o la maquina
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
            #se le asigna el icono correspondiente al jugador
            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            #si es el turno de la maquina, se ejecuta la siguiente funcion
            if self.turno % 2 == 0:
                #se le asigna el icono correspondiente a la maquina
                turno_icon = QtGui.QIcon("resource/o.png")
                turno_letra = "o"
                vacio: bool = False  # Easy level starts, fix AI turn, delete this to PVP.
                i: int = -1
                j: int = -1
                #mientras no se encuentre un espacio vacio, se ejecuta el siguiente ciclo
                while not vacio:
                    #se genera un numero aleatorio para i y j
                    i = random.randint(0, 2)
                    j = random.randint(0, 2)
                    #si el espacio esta vacio, se sale del ciclo y se asigna el valor
                    if self.matriz[i][j] == -1:
                        vacio = True
                valor = str(i) + str(j)
                print(f'Estoy jugando en una pos. random: {i},{j}')

            #se asigna el icono correspondiente al boton, seguun el valor de i y j
            if (valor == "00"): self.button_00.setIcon(turno_icon)
            if (valor == "01"): self.button_01.setIcon(turno_icon)
            if (valor == "02"): self.button_02.setIcon(turno_icon)
            if (valor == "10"): self.button_10.setIcon(turno_icon)
            if (valor == "11"): self.button_11.setIcon(turno_icon)
            if (valor == "12"): self.button_12.setIcon(turno_icon)
            if (valor == "20"): self.button_20.setIcon(turno_icon)
            if (valor == "21"): self.button_21.setIcon(turno_icon)
            if (valor == "22"): self.button_22.setIcon(turno_icon)

            #si el turno es 9, se ejecuta la siguiente funcion
            if self.turno == 9:
                for i in range(self.matriz_len):
                    for j in range(self.matriz_len):
                        #se asigna el icono correspondiente a el ultimo espacio disponible
                        if self.matriz[i][j] == -1: self.matriz[i][j] = "x"
                self.print_matriz()
                #se muestra el ganador o si es empate
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
            #si el turno es par, juega la maquina
            if self.turno % 2 == 0: self.botones_jugador("AI")
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")
                else:
                    self.mensaje.setText("El CPU ganó")
                return

        if self.modo == 1:
            #se verifica si gana el jugador o la maquina
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

            #se le asigna el icono correspondiente al jugador
            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            #si es el turno de la maquina, se ejecuta la siguiente funcion
            if self.turno % 2 == 0:
                #se le asigna el icono correspondiente a la maquina
                turno_icon = QtGui.QIcon("resource/o.png")
                turno_letra = "o"
                vacio: bool = False
                sigue: bool = False
                i: int = -1
                j: int = -1
                #verifica si la maquina puede ganar en el siguiente turno
                if ((self.matriz[0][0] == self.matriz[0][1] == "o" and self.matriz[0][2] == -1) or (self.matriz[2][0] ==
                     self.matriz[1][1] == "o" and self.matriz[0][2] == -1) or (self.matriz[2][2] == self.matriz[1][2] ==
                     "o" and self.matriz[0][2] == -1)):
                    valor = str(0) + str(2)
                    vacio = True
                if ((self.matriz[1][0] == self.matriz[1][1] == "o" and self.matriz[1][2] == -1) or (
                        self.matriz[0][2] == self.matriz[2][2] == "o"
                        and self.matriz[1][2] == -1)):
                    valor = str(1) + str(2)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[1][1] == "o" and self.matriz[2][2] == -1) or (
                        self.matriz[2][0] == self.matriz[2][1] == "o"
                        and self.matriz[2][2] == -1) or (
                        self.matriz[0][2] == self.matriz[1][2] == "o" and self.matriz[2][2] == -1)):
                    valor = str(2) + str(2)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[0][2] == "o" and self.matriz[0][1] == -1) or (
                        self.matriz[1][1] == self.matriz[2][1] == "o"
                        and self.matriz[0][1] == -1)):
                    valor = str(0) + str(1)
                    vacio = True
                if ((self.matriz[1][0] == self.matriz[1][2] == "o" and self.matriz[1][1] == -1) or (
                        self.matriz[0][0] == self.matriz[2][2] == "o" and self.matriz[1][1] == -1)
                        or (self.matriz[0][1] == self.matriz[2][1] == "o" and self.matriz[1][1] == -1)):
                    valor = str(1) + str(1)
                    vacio = True
                if ((self.matriz[0][1] == self.matriz[1][1] == "o" and self.matriz[2][1] == -1) or (
                        self.matriz[2][0] == self.matriz[2][2] == "o"
                        and self.matriz[2][1] == -1)):
                    valor = str(2) + str(1)
                    vacio = True
                if ((self.matriz[0][1] == self.matriz[0][2] == "o" and self.matriz[0][0] == -1) or (
                        self.matriz[1][1] == self.matriz[2][2] == "o" and self.matriz[0][0] == -1)
                        or (self.matriz[1][0] == self.matriz[2][0] == "o" and self.matriz[0][0] == -1)):
                    valor = str(0) + str(0)
                    vacio = True
                if ((self.matriz[0][0] == self.matriz[2][0] == "o" and self.matriz[1][0] == -1) or (
                        self.matriz[1][1] == self.matriz[1][2] == "o"
                        and self.matriz[1][0] == -1)):
                    valor = str(1) + str(0)
                    vacio = True
                if ((self.matriz[1][1] == self.matriz[0][2] == "o" and self.matriz[2][0] == -1) or (
                        self.matriz[2][1] == self.matriz[2][2] == "o" and self.matriz[2][0] == -1)
                        or (self.matriz[0][0] == self.matriz[1][0] == "o" and self.matriz[2][0] == -1)):
                    valor = str(2) + str(0)
                    vacio = True
                if ((self.matriz[1][1] == self.matriz[0][2] == "o" and self.matriz[2][0] == -1) or (
                        self.matriz[2][1] == self.matriz[2][2] == "o" and self.matriz[2][0] == -1)
                        or (self.matriz[0][0] == self.matriz[1][0] == "o" and self.matriz[2][0] == -1)):
                    valor = str(2) + str(0)
                    vacio = True
                #verifica si el jugador puede ganar en el siguiente turno y bloquea
                if ((self.matriz[0][0] == self.matriz[0][1] == "x" and self.matriz[0][2] == -1) or (self.matriz[2][0] ==
                     self.matriz[1][1] == "x" and self.matriz[0][2] == -1) or (self.matriz[2][2] == self.matriz[1][2] ==
                     "x" and self.matriz[0][2] == -1)):
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
                #si no puede ganar ni bloquear, elige una posicion aleatoria
                if (vacio == False):
                    while not sigue:
                        i = random.randint(0, 2)
                        j = random.randint(0, 2)
                        if self.matriz[i][j] == -1:
                            valor = str(i) + str(j)
                            sigue = True
            #se setea el icono en la posicion elegida
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
                #verifica si hay ganador o empate
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
            # si el turno es par, juega la maquina
            if self.turno % 2 == 0: self.botones_jugador("AI")
            #muestra el mensaje de quien ganó
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                else:
                    self.mensaje.setText("El CPU ganó")

                return

        # metodo para cpu contra jugador usando arboles de decision
        if self.modo == 2:
            #muestra el mensaje de quien gana
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
            # se le asigna el icono correspondiente al jugador
            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            # si el turno es par, juega la maquina
            if self.turno % 2 == 0:
                #se hace un arbol de decision para elegir la mejor jugada
                self.jugar_cpu_dificil()
            #se asigna el icono correspondiente segun valores de i y j
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
                #verifica si hay ganador o empate
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")

                elif (self.gana() == "o"):
                    self.mensaje.setText("El CPU ganó")

                else:
                    self.mensaje.setText("Empate")
                return
            if self.turno % 2 != 0: self.matriz[int(valor[0])][int(valor[1])] = turno_letra
            self.print_matriz()
            self.turno += 1
            if self.turno % 2 == 0: self.botones_jugador("AI")
            if self.gana() != "-1":
                if (self.gana() == "x"):
                    self.mensaje.setText("El jugador ganó")
                else:
                    self.mensaje.setText("El CPU ganó")
                return


     #arbol de decision para elegir la mejor jugada del cpu
    def arboles_decision(self, jugador: int, matriz_aux: []):
        var = self.posibilidades(matriz_aux)
        if var != 0:
            return var * jugador
        indice = -1
        valor = -2
        for i in range(0, 9):
            if self.interpretar_jugador(matriz_aux[i]) == 0:
                matriz_aux[i] = self.interpretar_jugador_inverso(jugador)
                puntaje = -self.arboles_decision((jugador * -1), matriz_aux)
                if puntaje > valor:
                    valor = puntaje
                    indice = i
                matriz_aux[i] = self.interpretar_jugador_inverso(0)  # -1 = 0, esta vacio
        if indice == -1:
            return 0
        return valor

    def jugar_cpu_dificil(self):
        indice = -1
        valor = -2
        matriz_aux = self.interpretar_matriz()
        for i in range(0, 9):
            if self.interpretar_jugador(matriz_aux[i]) == 0:
                matriz_aux[i] = self.interpretar_jugador_inverso(1)
                puntaje = -self.arboles_decision(-1, matriz_aux)
                matriz_aux[i] = self.interpretar_jugador_inverso(0)
                if puntaje > valor:
                    valor = puntaje
                    indice = i
        self.modificar_matriz(indice, "o")

    #muestra las posibles jugadas que tendra el cpu
    def posibilidades(self, matriz):
        mat = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
        for i in range(0, 8):
            #interpretar la mejor jugada
            if (self.interpretar_jugador(matriz[mat[i][0]]) != 0 and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][1]]) and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][2]])):
                return self.interpretar_jugador(
                    matriz[mat[i][2]])  # si hay un ganador, se retorna el valor del ganador
        return 0
