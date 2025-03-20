import unittest

class TestEjemplos(unittest.TestCase):
    
    def test_equal(self):
        # assertEqual(a,b) => Verifica que a y b tienen los mismos valores
        a = [1,2,3]
        b = [1,2,3]
        self.assertEqual(a, b)
    
    def test_not_equal(self):
        # assertNotEqual(a,b) => Verifica que a y b tienen distintos valores
        a = [1,2,3]
        b = [1,2,3,4]
        self.assertNotEqual(a, b)
    
    def test_in(self):
        # assertIn(a,b) => Verifica que a pertenece al iterable b
        self.assertIn(1, [3,2,1,6,7,8])
    
    def test_not_in(self):
        # assertNotIn(a,b) => Verifica que a NO pertenece al iterable b
        self.assertNotIn(5, [3,2,1,6,7,8])
    
    def test_is(self):
        # assertIs(a,b) => Verifica que ambas variables son la misma
        a = [1,2,3]
        b = a
        self.assertIs(a, b)

    def test_is_not(self):
        # assertIsNot(a,b) => Verifica que ambas variables son distintas
        a = [1,2,3]
        b = a
        c = [1,2,3]
        self.assertIsNot(b, c)
    
    def test_true(self):
        # assertTrue(x) => Verifica que el valor es verdadero
        self.assertTrue(23>15)

    def test_false(self):
        # assertFalse(x) => Verifica que el valor es falso
        self.assertFalse(4==6)
    
    def test_is_none(self):
        # assertIsNone(x) => Verifica que el valor es None
        x = None
        self.assertIsNone(x)

    def test_is_not_none(self):
        # assertIsNotNone(x) => Verifica que el valor no es None
        x = 'Juan'
        self.assertIsNotNone(x)
    
    def test_exception(self):
        # assertRaises(x) => Verifica que que se lanza una excepción
        # Dividir x/0 dar error
        with self.assertRaises(ZeroDivisionError):
            x = 15/0
