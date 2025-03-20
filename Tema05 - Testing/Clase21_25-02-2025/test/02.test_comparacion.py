import unittest

class TestComparacion(unittest.TestCase):

    def test_greater(self):
        # assertGreater(x,y) => Verifica que 'x' sea mayor a 'y'
        self.assertGreater(8,6)

    def test_greater_equal(self):
        # assertGreaterEqual(x,y) => Verifica que 'x' sea mayor o igual a 'y'
        self.assertGreaterEqual(8,6)
        self.assertGreaterEqual(9,9)

    def test_less(self):
        # assertLess(x,y) => Verifica que 'x' sea menor a 'y'
        self.assertLess(3,7)
    
    def test_less_equal(self):
        # assertLessEqual(x,y) => Verifica que 'x' sea menor o igual a 'y'
        self.assertLessEqual(3,7)
        self.assertLessEqual(7,7)
    
    def test_count_equal(self):
        # assertCountEqual(x,y) =>  Verifica que 'x' tenga los mismos elementos que 'y'
        #                           con el mismo número de ocurrencias
        lista1 = [1,2,3,4]
        lista2 = [4,3,2,1]
        lista3 = [1,2,2,3]
        lista4 = [3,2,1,2]
        self.assertCountEqual(lista1, lista2)
        self.assertCountEqual(lista4, lista4)