from flask import Blueprint, render_template, request, redirect
from models import db, Prestamo, Libro, Usuario
from datetime import date

prestamos_router = Blueprint('prestamos',__name__)

@prestamos_router.route('/prestamos')
def prestamo_index():
    prestamos = Prestamo.query.all()
    return render_template('prestamo/index.html', lista=prestamos)

@prestamos_router.route('/prestamos/nuevo')
def prestamo_nuevo():
    libros = Libro.query.all()
    usuarios = Usuario.query.all()
    return render_template('prestamo/nuevo.html', libros=libros, usuarios=usuarios)

@prestamos_router.route('/prestamos/guardar', methods=['POST'])
def prestamo_guardar():
    try:
        usuario = request.form['usuario']
        libro = request.form['libro']
        prestamo = Prestamo(
            usuario_id=usuario, 
            libro_id=libro,
            fecha_prestamo=date.today()
        )
        db.session.add(prestamo)
        db.session.commit()
        return redirect('/prestamos')
    except Exception as err:
        print(err)
        return render_template('500.html')

@prestamos_router.route('/prestamos/devolver/<int:id>')
def prestamo_devolver(id):
    prestamo = Prestamo.query.get_or_404(id)
    prestamo.estado = 'Devuelto'
    prestamo.fecha_devolucion = date.today()
    db.session.commit()
    return redirect('/prestamos')

@prestamos_router.route('/prestamos/detalle/<int:id>')
def prestamo_detalle(id):
    prestamo = Prestamo.query.get_or_404(id)
    libros = Libro.query.all()
    usuarios = Usuario.query.all()
    return render_template('prestamo/detalle.html', prestamo=prestamo, libros=libros, usuarios=usuarios)

@prestamos_router.route('/prestamos/editar/<int:id>', methods=['POST'])
def prestamo_editar(id):
    try:
        prestamo = Prestamo.query.get_or_404(id)
        prestamo.usuario_id = request.form['usuario']
        prestamo.libro_id = request.form['libro']
        prestamo.fecha_prestamo = request.form['fechaPrestamo']
        prestamo.fecha_devolucion = request.form['fechaDevolucion'] or None
        prestamo.estado = request.form['estado']
        db.session.commit()
        return redirect('/prestamos')
    except Exception as err:
        print(err)
        return render_template('500.html')