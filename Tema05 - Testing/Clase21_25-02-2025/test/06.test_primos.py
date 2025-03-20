import unittest
from ..modules.primo import es_primo

class TestEsPrimo(unittest.TestCase):

    # Prueba para números primos
    def test_numeros_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))

    # Prueba para números que no son primos
    def test_numeros_no_primos(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))

    # Prueba para números negativos
    def test_numeros_negativos(self):
        self.assertFalse(es_primo(-1))
        self.assertFalse(es_primo(-2))
        self.assertFalse(es_primo(-3))