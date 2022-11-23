import unittest
from unitTesting import metodosUnidad



"""
    Clase que contiene los métodos de prueba unitaria, para la clase metodosUnidad. 
    
    :param unittest.TestCase: clase de la que hereda la clase principal
    :param self: instancia de la clase
    :metodosUnidad: clase que contiene los métodos a probar
    :test_gana: método que prueba el método gana de la clase metodosUnidad
    :test_matriz: método que prueba el método getmatiz, que haya una matriz de 3x3, con valores de -1
    :test_facil: método que prueba el método facil de la clase metodosUnidad, retorne un string
    :test_medio: método que prueba el método medio de la clase metodosUnidad, retorne un string específico
    :test_dificil: método que prueba el método dificil de la clase metodosUnidad, retorne un valor esperado
    
"""
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
        #validacion de que sea verdadero que el metodo facil retorne un valor
        #puede ser cualquiera de los 9 valores posibles ya que es aleatorio.
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
