# app.py

from flask import Flask
from config import Config
from models import db, Genero

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'codigo2025'
db.init_app(app)

@app.route("/")
def index():
    # SELECT * FROM generos
    generos = Genero.query.all()
    for item in generos:
        print(item.nombre)
    return "<p>Hello, World!</p>"