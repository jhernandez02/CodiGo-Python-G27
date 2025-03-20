# models.py

from flask_sqlalchemy import SQLAlchemy

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Genero(db.Model):
    __tablename__ = 'generos'
    id = db.Column(db.Integer, primary_key=True) # Indicamos la clave primaria
    nombre = db.Column(db.String(50),nullable=False)

class Autor(db.Model):
    __tablename__ = 'autores'
    id = db.Column(db.Integer, primary_key=True) # Indicamos la clave primaria
    nombre = db.Column(db.String(100),nullable=False)
    nacionalidad = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.Date)