# app.py

from flask import Flask, render_template
from config import Config
from models import db

# Importamos las rutas
from routes.autores import autores_router
from routes.generos import generos_router
from routes.libros import libros_router
from routes.prestamos import prestamos_router

app = Flask(__name__)
# Cargamos la configuración de la base de datos
app.config.from_object(Config)
# Inicializamos la base de datos
db.init_app(app)

app.register_blueprint(autores_router)
app.register_blueprint(generos_router)
app.register_blueprint(libros_router)
app.register_blueprint(prestamos_router)

# Manejo del error 404: Pá  gina no encontrada
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html'), 404