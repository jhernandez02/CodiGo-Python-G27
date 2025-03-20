# test_suma.py
import unittest

# Código a ser probado
def suma(a,b):
    return a + b

class TestSuma(unittest.TestCase):
    # Método de prueba para la funcion suma
    def test_suma(self):
        self.assertEqual(suma(2,2),4)
        self.assertEqual(suma(2,4),6)
        self.assertEqual(suma(6,3),9)
    
if __name__ == '__main__':
    unittest.main()

