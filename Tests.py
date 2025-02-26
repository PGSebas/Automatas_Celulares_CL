import unittest
#import (Módulo con la lógica)

class AutomatasTest(unittest.TestCase):

    def testNormal1(self):
        orden_matriz: int = 250
        poblacion_inicial: int = 10
        probabilidad: float = 3.5
        tiempo_simulacion: int = 20

        pob_final_esperada: int = 240

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testNormal2(self):
        orden_matriz: int = 100
        poblacion_inicial: int = 1
        probabilidad: float = 2
        tiempo_simulacion: int = 10

        pob_final_esperada: int = 4

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testNormal3(self):
        orden_matriz: int = 500
        poblacion_inicial: int = 25
        probabilidad: float = 5
        tiempo_simulacion: int = 30

        pob_final_esperada: int = 3076

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testExtraordinario1(self):
        orden_matriz: int = 50
        poblacion_inicial: int = 3
        probabilidad: float = 5
        tiempo_simulacion: int = 5

        pob_final_esperada: int = 10

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testExtraordinario2(self):
        orden_matriz: int = 1000
        poblacion_inicial: int = 79
        probabilidad: float = 0.2
        tiempo_simulacion: int = 2

        pob_final_esperada: int = 81

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testExtraordinario3(self):
        orden_matriz: int = 50
        poblacion_inicial: int = 3
        probabilidad: float = 100
        tiempo_simulacion: int = 5

        pob_final_esperada: int = 50

        pob_final_obtenida = ### Definir lógica

        self.assertAlmostEqual(pob_final_esperada, pob_final_obtenida, delta=20) # Cambiar delta según el caso

    def testError1(self):
        orden_matriz: int = 0
        poblacion_inicial: int = 32
        probabilidad: float = 3.2
        tiempo_simulacion: int = 50

        with self.assertRaises(Exception):
          resultado_esperado = # ERROR: El tiempo de simulación debe ser mayor a cero

    def testError2(self):
        orden_matriz: int = 100
        poblacion_inicial: int = 1
        probabilidad: float = 5
        tiempo_simulacion: int = 0

        with self.assertRaises(Exception):
          resultado_esperado = # ERROR: El tiempo de simulación debe ser mayor a cero

    def testError3(self):
        orden_matriz: int = 50
        poblacion_inicial: int = 0
        probabilidad: float = 5
        tiempo_simulacion: int = 5

        with self.assertRaises(Exception):
          resultado_esperado = # ERROR: la población inicial debe ser mayor o igual a 2

    def testError4(self):
        orden_matriz: int = 60
        poblacion_inicial: int = 21
        probabilidad: float = 2.1
        tiempo_simulacion: int = -10

        with self.assertRaises(Exception):
          resultado_esperado = # ERROR: El tiempo de simulación no puede ser negativo


if __name__ == "__main__":
   unittest.main()
