import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Configuramos el entorno de pruebas
        self.app = app.test_client()
        self.app.testing = True
    
    def test_usuario_crear(self):
        datos = {
            "nombre": "Javier Morales",
            "email": "javier@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/usuarios', json=datos)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, b'{"message":"Usuario creado satisfactoriamente"}\n')
    
    def test_usuario_crear_error(self):
        datos = {
            "email": "javier@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/usuarios', json=datos)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'{"message":"No se pudo crear el usuario"}\n')
    
    def test_login_ok(self):
        datos = {
            "email": "miguel@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Login satisfactorio"}\n')
    
    def test_not_login(self): # Escenario: credenciales incorrectas
        datos = {
            "email": "ramiro@mail.com",
            "clave": "abc123"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"message":"Credenciales incorrectas"}\n')

    def test_login_error(self): # Escenario: ocurre un error
        datos = {
            "usuario": "miguel@mail.com",
            "clave": "123456"
        }
        response = self.app.post('/login', json=datos)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, b'{"message":"Ocurrio un error"}\n')

    def test_recuperar_contrasena_ok(self):
        datos = {
            "email": "miguel@mail.com",
        }
        response = self.app.post('/recuperar-contrasena', json=datos)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"message":"Contrase\\u00f1a reiniciada satisfactoriamente"}\n')

    def test_recuperar_contrasena_not_ok(self):
        datos = {
            "email": "ramiro@mail.com",
        }
        response = self.app.post('/recuperar-contrasena', json=datos)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, b'{"message":"Usuario no encontrado"}\n')