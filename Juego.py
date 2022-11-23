import random
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Juego(QMainWindow):
    """
        Explicacion
        la clase juego se encarga de manejar la logica del juego, se encarga de verificar si el jugador gano o perdio,
        todo esto dependiendo del modo de juego que se seleccione, si es facil, medio o dificil.
        unicamente para el modo de juego jugador vs cpu.

        parametros:
        QMainWindow: clase de la que hereda la clase principal

        metodos:
        resetear: reinicia el juego
        cerrar: cierra la ventana
        set_modo: cambia el modo de juego  0 = facil, 1 = medio, 2 = dificil
        set_turno: cambia el turno del jugador
        print_matriz: imprime la matriz en la consola
        llamar_valor: retorna el valor de la matriz dependiendo de la posicion
        botones_jugador: funcion que se encarga de manejar los tipos de juego, facil, medio y dificil
        interpretar_jugador: funcion que se encarga de interpretar el turno del jugador
        interpretar_jugador_inverso: funcion que se encarga de interpretar el valor de la matriz
        verificar_ganador: funcion que se encarga de verificar si el jugador gano o perdio
        arboles_decision: funcion que se encarga de manejar el arbol de decision para el modo de juego dificil
        posibilidades: funcion que se encarga de manejar las posibilidades de ganar o perder

        """

    def __init__(self):
        super().__init__()
        """
        atributos:
            turno int: variable que se encarga de manejar el turno del jugador, 1 x = jugador 1, 2 = jugador 2 O
            matriz_len int: variable que se encarga de manejar el tamaño de la matriz, en este caso es 3x3
            gano bool: variable que se encarga de verificar si un jugador gano o no
            modo int: variable que se encarga de manejar el modo de juego, 0 = facil, 1 = medio, 2 = dificil
        """
        # Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("resource/game.ui", self)
        self.turno: int = 1
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
        self.regresarJC.clicked.connect(self.cerrar)
        # si se reinicia el juego se reinicia la matriz y el turno y se limpian los botones de la interfaz grafica
        self.reiniciaButton.clicked.connect(self.resetear)


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
        self.modo = self.dificultad.currentIndex()

    def set_turno(self, turno: int):
        self.turno = turno

    # funcion que se encarga de imprimir la matriz en la consola
    def print_matriz(self):
        for i in range(self.matriz_len):
            for j in range(self.matriz_len):
                print(self.matriz[i][j], end=", ")
            print()
        print()


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
        """
            Explicacion
            cuenta con tres distintos niveles de dificultad que es seleccionado por el usuario
            modo 0 = facil, se ejecutara una funcion que seleccionara un boton aleatorio
            modo 1 = medio, se ejecutara una funcion donde la maquina se defendera  de las jugadas
            del jugador
            modo 2 = dificil, se ejecutara una funcion donde la maquina utilizara arboles de decision
            para saber cual es la mejor jugada y ejecutarla.
        """
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
            turno_icon = QtGui.QIcon("resource/x.png")
            turno_letra = "x"
            #si es el turno de la maquina, se ejecuta la siguiente funcion
            if self.turno % 2 == 0:
                turno_icon = QtGui.QIcon("resource/o.png")
                turno_letra = "o"
                vacio: bool = False
                i: int = -1
                j: int = -1
                while not vacio:
                    #se genera un numero aleatorio para i y j
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
                        #se asigna el icono correspondiente a el ultimo espacio disponible
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

        if self.modo == 2:
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
                #se hace un arbol de decision para elegir la mejor jugada
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


    def arboles_decision(self, jugador: int, matriz_aux: []):
        """
         Explicacion
           este metodo crea un arbol de decision para elegir la mejor jugada de la maquina en el modo dificil del juego
           dejando asi a el jugador con pocas posibilidades de ganar contra la maquina en este modo de juego (dificil),
           siempre seguira el mismo algoritmo para la toma de decisiones, pero con diferentes valores de profundidad.
         """
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

    def posibilidades(self, matriz):
        mat = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
        for i in range(0, 8):
            #interpretar la mejor jugada
            if (self.interpretar_jugador(matriz[mat[i][0]]) != 0 and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][1]]) and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][2]])):
                return self.interpretar_jugador(matriz[mat[i][2]])  # si hay un ganador, se retorna el valor del ganador
        return 0