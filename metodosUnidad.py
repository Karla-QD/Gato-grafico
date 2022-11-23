import random

class metodosUnidad():

    def __init__(self):
        self.matriz_len: int = 3
        self.gano = False
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


    def getmatriz(self):
        return self.matriz

    def gana(self) -> str:
        ganador: str = "-1"
        # verificamos si hay un ganador en las filas
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


    def metodo_facil(self):
      vacio: bool = False
      i: int = -1
      j: int = -1
      while not vacio:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if self.matriz[i][j] == -1:
            vacio = True
        valor = str(i) + str(j)
        return valor
        print(f'Estoy jugando en una pos. random: {i},{j}')

    def metodo_medio(self):
        valor: str = ""
        vacio: bool = False
        sigue: bool = False
        i: int = -1
        j: int = -1
        # verifica si la maquina puede ganar en el siguiente turno
        if ((self.matriz[0][0] == self.matriz[0][1] == "o" and self.matriz[0][2] == -1) or (self.matriz[2][0] ==
            self.matriz[1][1] == "o" and self.matriz[0][2] == -1) or (
                self.matriz[2][2] == self.matriz[1][2] ==
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
        # verifica si el jugador puede ganar en el siguiente turno y bloquea
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
        # si no puede ganar ni bloquear, elige una posicion aleatoria
        if (vacio == False):
            while not sigue:
                i = random.randint(0, 2)
                j = random.randint(0, 2)
                if self.matriz[i][j] == -1:
                    valor = str(i) + str(j)
                    sigue = True
        return valor



