from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/categorias_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)

@app.route('/categorias', methods=['GET'])
def categoria_index():
    categorias = Categoria.query.all()
    # Creamos el contenido mediante una Lista por compresión
    data = [{'id':categoria.id, 'nombre':categoria.nombre} for categoria in categorias]
    return jsonify(data)
    
@app.route('/categorias', methods=['POST'])
def categoria_guardar():
    data = request.json
    nombre = data['nombre']
    categoria = Categoria(nombre=nombre)
    db.session.add(categoria)
    db.session.commit()
    return jsonify({
        "message": "Categoria creada"
    })

@app.route('/categorias/<int:id>', methods=['GET'])
def categoria_detalle(id):
    categoria = Categoria.query.get_or_404(id)
    return jsonify({
        "id": categoria.id,
        "nombre": categoria.nombre
    })

@app.route('/categorias/<int:id>', methods=['PUT'])
def categoria_editar(id):
    data = request.json
    categoria = Categoria.query.get_or_404(id)
    categoria.nombre = data['nombre']
    db.session.commit()
    return jsonify({
        "message": "Categoria actualizada"
    })

@app.route('/categorias/<int:id>', methods=['DELETE'])
def categoria_eliminar(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({
        "message": "Categoria eliminada"
    })