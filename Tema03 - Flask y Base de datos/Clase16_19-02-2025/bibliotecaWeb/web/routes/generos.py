from flask import Blueprint, render_template, request, redirect
from models import db, Genero

generos_router = Blueprint('generos',__name__)

@generos_router.route('/generos')
def genero_index():
    generos = Genero.query.all() # SELECT * FROM generos
    return render_template('genero/index.html', lista=generos)

@generos_router.route('/generos/nuevo')
def genero_nuevo():
    return render_template('genero/nuevo.html')

@generos_router.route('/generos/guardar', methods=['POST'])
def genero_guardar():
    try:
        nombre = request.form['nombre']
        genero = Genero(nombre=nombre)
        db.session.add(genero)
        db.session.commit()
        return redirect('/generos')
    except Exception as err:
        print(err)
        return render_template('500.html')

@generos_router.route('/generos/detalle/<int:id>')
def genero_detalle(id):
    # SELECT * FROM generos WHERE id=<id>
    genero = Genero.query.get_or_404(id) # Si no existe el id, devuelve un error de 404
    return render_template('genero/detalle.html', genero=genero)

@generos_router.route('/generos/editar/<int:id>', methods=['POST'])
def genero_editar(id):
    try:
        genero = Genero.query.get_or_404(id)
        genero.nombre = request.form['nombre']
        db.session.commit()
        return redirect('/generos')
    except Exception as err:
        print(err)
        return render_template('500.html')

@generos_router.route('/generos/eliminar/<int:id>')
def genero_eliminar(id):
    try:
        genero = Genero.query.get_or_404(id)
        db.session.delete(genero)
        db.session.commit()
        return redirect('/generos')
    except Exception as err:
        print(err)
        return render_template('500.html')