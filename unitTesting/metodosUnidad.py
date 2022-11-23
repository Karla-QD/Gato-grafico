import random


"""
    explicacion:
     la clase metodos de unidad se encarga de realizar las pruebas unitarias de los metodos de la clase principal,
     los cuales fueron creados para verificar que los metodos de la clase principal funcionen correctamente.

    metodos:
        getmatriz: verifica que la matriz se haya inicializado correctamente
        gana: verifica que el metodo gana funcione correctamente, retornando el jugador correcto
        metodo_facil: verifica que el metodo facil funcione correctamente, retornando el movimiento correcto, 
        la mayoria de veces la prueba no pasa debido a que el metodo facil es aleatorio
        metodo_medio: verifica que el metodo medio funcione correctamente, retornando el movimiento correcto de el cpu
        metodo_dificil: verifica que el metodo dificil funcione correctamente, retornando el movimiento correcto de el 
        cpu, verificando metodos utilizados en el metodo dificil
    """
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

    def posibilidades(self, matriz):
        mat = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
        for i in range(0, 8):
            #interpretar la mejor jugada
            if (self.interpretar_jugador(matriz[mat[i][0]]) != 0 and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][1]]) and
                    self.interpretar_jugador(matriz[mat[i][0]]) == self.interpretar_jugador(matriz[mat[i][2]])):
                return self.interpretar_jugador(matriz[mat[i][2]])  # si hay un ganador, se retorna el valor del ganador
        return 0





