# app.py

from flask import Flask
from config import Config
from models import db
# Importamos las rutas
from routes.autores import autores_router
from routes.generos import generos_router

app = Flask(__name__)
# Cargamos la configuración de la base de datos
app.config.from_object(Config)
# Inicializamos la base de datos
db.init_app(app)

with app.app_context():
    db.reflect()

app.register_blueprint(autores_router)
app.register_blueprint(generos_router)

# Manejo del error 404: Pá  gina no encontrada
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html'), 404