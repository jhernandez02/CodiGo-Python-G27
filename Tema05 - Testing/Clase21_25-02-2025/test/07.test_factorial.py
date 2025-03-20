import unittest
from modules.factorial import factorial

class TestFactorial(unittest.TestCase):

    # Prueba para números positivos
    def test_factorial_positivo(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(3), 6)
    
    # Prueba para el número 0
    def test_factorial_cero(self):
        self.assertEqual(factorial(0), 1)

    # Prueba para el número 1
    def test_factorial_uno(self):
        self.assertEqual(factorial(1), 1)

    # Prueba para número negativos (debe lanzar una excepción)
    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            factorial(-5)

