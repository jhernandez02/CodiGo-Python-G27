# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
import enum

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Genero(db.Model):
    __tablename__ = 'generos'
    id = db.Column(db.Integer, primary_key=True) # Indicamos la clave primaria
    nombre = db.Column(db.String(50),nullable=False)

class Autor(db.Model):
    __tablename__ = 'autores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    nacionalidad = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date)

class Libro(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255),nullable=False)
    autor_id = db.Column(db.Integer,nullable=False)
    genero_id = db.Column(db.Integer,nullable=False)
    anio_publicacion = db.Column(db.Integer)
    isbn = db.Column(db.String(20))
    stock = db.Column(db.Integer, default=1)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    telefono = db.Column(db.String(15))
    fecha_registro = db.Column(db.Date)

class EstadoLibro(enum.Enum):
    PRESTADO = 'Prestado'
    DEVUELTO = 'Devuelto'

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, nullable=False)
    libro_id = db.Column(db.Integer, nullable=False)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date)
    estado = db.Column(Enum('Prestado','Devuelto'), default='Prestado', nullable=False)