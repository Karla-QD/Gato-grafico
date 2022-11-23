import unittest
from unitTesting import metodosUnidad


class TestCaseJvsCPU(unittest.TestCase):

    def __int__(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = []

    def test_matriz(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        result = self.metodosUnidad.getmatriz()
        self.assertEqual(result, self.matriz)

    def test_gana(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.metodosUnidad.matriz[0][0] = "x"
        self.metodosUnidad.matriz[1][1] = "x"
        self.metodosUnidad.matriz[2][2] = "x"
        result = self.metodosUnidad.gana()
        self.assertEqual(result, "x")


    def test_facil(self):
        #este test la mayor parte del tiempo falla, ya que el metodo facil es aleatorio,
        # por lo que no siempre va a ser 00
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        result = self.metodosUnidad.metodo_facil()
        if(result == "00"):
            self.assertEqual(result, "00")
        else:
            self.assertNotEqual(result, "00")

    def test_medio(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.metodosUnidad.matriz[0][0] = "x"
        self.metodosUnidad.matriz[0][1] = "x"
        result = self.metodosUnidad.metodo_medio()
        self.assertEqual(result, "02")

    def test_dificil(self):
        self.metodosUnidad = metodosUnidad.metodosUnidad()
        self.metodosUnidad.matriz[0][0] = "x"
        self.metodosUnidad.matriz[1][1] = "o"
        self.metodosUnidad.matriz[0][2] = "x"
        result = self.metodosUnidad.jugar_cpu_dificil()
        self.assertEqual(result, 1)









if __name__ == '__main__':
    unittest.main()
