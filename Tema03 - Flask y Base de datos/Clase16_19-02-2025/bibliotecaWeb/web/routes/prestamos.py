from flask import Blueprint, render_template, request, redirect
from models import db, Prestamo, Libro, Usuario

prestamos_router = Blueprint('prestamos',__name__)

@prestamos_router.route('/prestamos')
def prestamo_index():
    #prestamos = Prestamo.query.all()
    prestamos = db.session.query(
        Prestamo.id, Prestamo.fecha_prestamo, Prestamo.fecha_devolucion, Prestamo.estado,
        Usuario.nombre.label('usuario_id'), Libro.titulo.label('libro_id')
    ).join(
        Usuario, Usuario.id==Prestamo.usuario_id
    ).join(
        Libro, Libro.id==Prestamo.libro_id
    ).all()
    return render_template('prestamo/index.html', lista=prestamos)