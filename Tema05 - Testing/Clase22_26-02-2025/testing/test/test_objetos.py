# test/test_objetos.py

import unittest
from modules.shape import Shape, Square

class TestObjetos(unittest.TestCase):

    def setUp(self):
        self.square = Square() # instanciamos un objeto de la clase Square()

    def test_is_instance(self):
        # assertIsInstance(a,b) => Valida que a(obj) sea una instancia de b(class)
        self.assertIsInstance(self.square, Square)
    
    def test_is_instance_of_parent_class(self):
        self.assertIsInstance(self.square, Shape)

    def test_is_not_instance(self):
        shape = Shape()
        # assertIsNotInstance(a,b) => Valida que a(obj) no sea una instancia de b(class)
        self.assertNotIsInstance(shape, Square)