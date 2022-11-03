class tic_tac_toe:
    def __init__(self):
        self.board = [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ']
        self.jugador = 1
        self.CPU = 2
        self.ganador = 0
        self.turno = ' '

    def draw_board(self):   # Dibuja el tablero
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print("-----------")
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print("-----------")
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])

    def ganador_empate(self):   # Verifica si hay un ganador
        if self.board[0] == self.board[1] == self.board[2]:
            self.ganador = self.jugador
        elif self.board[3] == self.board[4] == self.board[5]:
            self.ganador = self.jugador
        elif self.board[6] == self.board[7] == self.board[8]:
            self.ganador = self.jugador
        elif self.board[0] == self.board[3] == self.board[6]:
            self.ganador = self.jugador
        elif self.board[1] == self.board[4] == self.board[7]:
            self.ganador = self.jugador
        elif self.board[2] == self.board[5] == self.board[8]:
            self.ganador = self.jugador
        elif self.board[0] == self.board[4] == self.board[8]:
            self.ganador = self.jugador
        elif self.board[2] == self.board[4] == self.board[6]:
            self.ganador = self.jugador
        elif self.board[0] != ' 0 ' and self.board[1] != ' 1 ' and self.board[2] != ' 2 ' and self.board[3] != ' 3 ' and self.board[4] != ' 4 ' and self.board[5] != ' 5 ' and self.board[6] != ' 6 ' and self.board[7] != ' 7 ' and self.board[8] != ' 8 ':
            self.ganador = 3
        else:
            self.ganador = 0

    def jugar(self):   # Juega el juego
        while self.ganador == 0:
            self.draw_board()
            self.ganador_empate()
            if self.ganador == 0:
                self.jugador = self.jugador % 2 + 1
                if(self.jugador == 1):
                    self.turno = ' X '
                if(self.jugador == 2):
                    self.turno = ' O '
                print("Turno del jugador %d" % self.jugador)
                self.board[int(input(">> "))] = self.turno
        self.draw_board()
        if(self.winner == 3):
            print("Empate")
        else:
         print("El jugador %d gana!" % self.winner)


if __name__ == "__main__":
    game = tic_tac_toe()
    game.jugar()

