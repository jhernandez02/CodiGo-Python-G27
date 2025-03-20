from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Enum

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10762822:vhAESUFcCK@sql10.freesqldatabase.com/sql10762822'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.String(255))
    precio = db.Column(db.Float, nullable=False)
    imagen = db.Column(db.String(100), nullable=False)
    estado = db.Column(Enum('Disponible','Agotado','Descontinuado'), default='Disponible', nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

@app.route('/')
def producto_listar():
    return 'listado de productos'

@app.route('/productos/nuevo')
def producto_nuevo():
    return 'se muestra el formulario nuevo'

@app.route('/productos/editar/<int:id>')
def producto_editar(id):
    return 'se muestra el formulario nuevo'

@app.route('/productos/eliminar/<int:id>')
def producto_eliminar(id):
    return 'se muestra el formulario nuevo'