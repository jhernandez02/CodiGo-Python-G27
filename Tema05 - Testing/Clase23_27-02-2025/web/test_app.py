import unittest
from unittest.mock import patch, MagicMock
from app import app, db, Categoria

class CategoriaApiTestCase(unittest.TestCase):

    def setUp(self):
        # Se crea una apliación de prueba y un cliente para hacer peticiones
        self.app = app.test_client()
        self.app.testing = True

        # Mock de la base de datos para que no inteeractúe con la real
        #self.mock_db_session = MagicMock()
        self.ctx = app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        self.ctx.pop()
    
    # Prueba para obtener todas las categorías usando mocks
    @patch('app.Categoria.query.all') # Mockeo el método all del modelo Categoria
    def test_get_categorias(self, mock_request):
        # Configuramos el mock para que devuelva una lista de categorías simuladas
        mock_request.status_code = 200
        mock_request.json.return_value = [
            {"id":1, "nombre":"Electrónica"},
            {"id":2, "nombre":"Ropa"}
        ]

        # Realizamos la solicitud
        response = self.app.get('/categorias')
        print(response.json)
        # Verificamos que las respuestas sean correctas
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(len(response.json),2)

