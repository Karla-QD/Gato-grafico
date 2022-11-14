import unittest
import Juego
import Jugador_Jugador
import Principal
from PyQt5 import uic, QtGui


class TestCaseJvsJ(unittest.TestCase):
    def __int__(self):
        self.jugador = Jugador_Jugador.Jugador_Jugador()
    def test_jvsj(self):
        self.jugador = Jugador_Jugador.Jugador_Jugador()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.matriz[0][0] = "x"
        self.matriz[0][1] = "x"
        self.matriz[0][2] = "x"
        self.jugador.matriz[0][0] = self.matriz[0][0]
        self.jugador.matriz[0][1] = self.matriz[0][1]
        self.jugador.matriz[0][2] = self.matriz[0][2]
        self.assertEqual(self.jugador.gana(), True)



if __name__ == '__main__':
    unittest.main()
