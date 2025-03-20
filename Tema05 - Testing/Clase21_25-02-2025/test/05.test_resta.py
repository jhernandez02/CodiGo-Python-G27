# test_resta.py
import unittest

# Código a ser probado
def resta(a,b):
    total = a - b
    return total

class TestResta(unittest.TestCase):
    # Método de prueba para la funcion resta
    def test_resta(self):
        self.assertEqual(resta(6,2),4)
        self.assertEqual(resta(17,11),6)
        self.assertEqual(resta(11,2),9)
    
if __name__ == '__main__':
    unittest.main()