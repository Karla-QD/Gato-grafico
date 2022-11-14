import unittest
import Juego
import Jugador_Jugador
import Principal
from PyQt5 import uic, QtGui


class TestCaseJvsJ(unittest.TestCase):

    def __int__(self):
        self.jugador = Jugador_Jugador.Jugador_Jugador()
        self.juego = Juego.Juego()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    #def test_jvsC(self):
     #   result = "x"
      #  self.assertEqual(result, "x")

    def test_jvsj(self):
        self.jugador = Jugador_Jugador.Jugador_Jugador()
        self.matriz = []
        self.jugador.matriz[0][0] = "x"
        self.jugador.matriz[0][1] = "x"
        self.jugador.matriz[0][2] = "x"
        result = self.jugador.gana()
        self.assertEqual(result, "x")


if __name__ == '__main__':
    unittest.main()
