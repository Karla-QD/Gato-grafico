import unittest
import metodosUnidad



class TestCaseJvsCPU(unittest.TestCase):

    def __int__(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = []

    def test_matriz(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.matriz[0][0] = -1
        self.matriz[0][1] = "x"
        self.matriz[0][2] = "x"
        result = self.metodosUnidad.getmatriz()
        self.assertEqual(result[0][0], self.matriz[0][0])

    def test_gana(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.metodosUnidad.matriz[0][0] = "x"
        self.metodosUnidad.matriz[0][1] = "x"
        self.metodosUnidad.matriz[0][2] = "x"
        result = self.metodosUnidad.gana()
        self.assertEqual(result, "x")

    def test_facil(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        result = self.metodosUnidad.metodo_facil()
        self.assertEqual(result, "00")

    def test_medio(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.metodosUnidad.matriz[0][0] = "x"
        self.metodosUnidad.matriz[0][1] = "x"
        result = self.metodosUnidad.metodo_medio()
        self.assertEqual(result, "02")




if __name__ == '__main__':
    unittest.main()
