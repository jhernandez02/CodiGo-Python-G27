# test/test_rectangulo.py

import unittest
from modules.rectangulo import rectangulo_area, rectangulo_perimetro

class TestRectangulo(unittest.TestCase):

    def setUp(self):
        self.base = 5
        self.altura = 10

    def test_rectangulo_area(self):
        self.assertEqual(rectangulo_area(self.base, self.altura), 50)
        self.assertEqual(rectangulo_area(15, 10), 150)
        
    def test_rectangulo_perimetro(self):
        self.assertEqual(rectangulo_perimetro(self.base, self.altura), 30)
        self.assertEqual(rectangulo_perimetro(15, 10), 50)