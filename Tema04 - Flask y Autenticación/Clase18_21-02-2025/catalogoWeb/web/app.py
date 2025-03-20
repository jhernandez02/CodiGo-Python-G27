from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Enum

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/catalogo_db'
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
    categoria = db.relationship('Categoria')

# Rutas CRUD para Categorías
@app.route('/categorias', methods=['GET'])
def categoria_listar():
    categorias = Categoria.query.all()
    data = []
    for c in categorias:
        data.append({'id':c.id, 'nombre':c.nombre})
    return jsonify(data)

@app.route('/categorias/<int:id>', methods=['GET'])
def categoria_detalle(id):
    try:
        categoria = Categoria.query.get_or_404(id)
        data = {'id':categoria.id, 'nombre':categoria.nombre}
        return jsonify(data)
    except Exception as err:
        print(err)
        return jsonify({
            'message':'Categoría no encontrada',
            'status': 'error'
        })

@app.route('/categorias', methods=['POST'])
def categoria_crear():
    try:
        data = request.json
        nueva_categoria = Categoria(nombre=data['nombre'])
        db.session.add(nueva_categoria)
        db.session.commit()
        return jsonify({
            'message': 'Categoría creada',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message': 'No se pudo crear la categoría',
            'status': 'error'
        })

@app.route('/categorias/<int:id>', methods=['PUT'])
def categoria_editar(id):
    try:
        data = request.json
        categoria = Categoria.query.get_or_404(id)
        categoria.nombre = data['nombre']
        db.session.commit()
        return jsonify({
            'message': 'Categoría actualizada',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message': 'No se pudo editar la categoría',
            'status': 'error'
        })

@app.route('/categorias/<int:id>', methods=['DELETE'])
def categoria_eliminar(id):
    try:
        categoria = Categoria.query.get_or_404(id)
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({
            'message': 'Categoría eliminada',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message':'Producto no encontrado',
            'status': 'error'
        })

@app.route('/productos', methods=['GET'])
def producto_listar():
    productos = Producto.query.all()
    data = []
    for p in productos:
        data.append({
            'id':p.id, 
            'nombre':p.nombre,
            'descripcion':p.descripcion,
            'precio':p.precio,
            'imagen':p.imagen,
            'estado':p.estado,
            'categoria_id':p.categoria_id,
            'categoria':p.categoria.nombre
        })
    return jsonify(data)

@app.route('/productos/<int:id>', methods=['GET'])
def producto_detalle(id):
    try:
        producto = Producto.query.get_or_404(id)
        data = {
            'id':producto.id, 
            'nombre':producto.nombre,
            'descripcion':producto.descripcion,
            'precio':producto.precio,
            'imagen':producto.imagen,
            'estado':producto.estado,
            'categoria_id':producto.categoria_id,
            'categoria':producto.categoria.nombre
        }
        return jsonify(data)
    except Exception as err:
        print(err)
        return jsonify({
            'message':'Producto no encontrado',
            'status': 'error'
        })

@app.route('/productos', methods=['POST'])
def producto_crear():
    try:
        data = request.json
        nuevo_producto = Producto(
            nombre=data['nombre'],
            precio=data['precio'],
            imagen=data['imagen'],
            estado=data['estado'],
            categoria_id=data['categoria_id']
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({
            'message': 'Producto creado',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message': 'No se pudo crear el producto',
            'status': 'error'
        })

@app.route('/productos/<int:id>', methods=['PUT'])
def producto_editar(id):
    try:
        data = request.json
        producto = Producto.query.get_or_404(id)
        producto.nombre=data['nombre']
        producto.precio=data['precio']
        producto.imagen=data['imagen']
        producto.estado=data['estado']
        producto.categoria_id=data['categoria_id']
        db.session.commit()
        return jsonify({
            'message': 'Producto actualizado',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message': 'No se pudo editar el producto',
            'status': 'error'
        })

@app.route('/productos/<int:id>', methods=['DELETE'])
def producto_eliminar(id):
    try:
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return jsonify({
            'message': 'Producto eliminado',
            'status': 'ok'
        })
    except Exception as err:
        print(err)
        return jsonify({
            'message':'Producto no se puedo eliminar',
            'status': 'error'
        })