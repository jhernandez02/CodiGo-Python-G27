from flask import Blueprint, render_template, request, redirect
from models import db, Libro, Genero, Autor

libros_router = Blueprint('libros',__name__)

@libros_router.route('/libros')
def libros_index():
    #libros = Libro.query.all()
    libros = db.session.query(
        Libro.id, Libro.titulo, Libro.anio_publicacion, Libro.isbn, Libro.stock,
        Genero.nombre.label('genero_id'), Autor.nombre.label('autor_id')
    ).join(
        Genero, Genero.id==Libro.genero_id
    ).join(
        Autor, Autor.id==Libro.autor_id
    ).all()
    return render_template('libro/index.html', lista=libros)

@libros_router.route('/libros/nuevo')
def libro_nuevo():
    generos = Genero.query.all()
    autores = Autor.query.all()
    return render_template('libro/nuevo.html', generos=generos, autores=autores)

@libros_router.route('/libros/guardar', methods=['POST'])
def libro_guardar():
    try:
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        anioPublicacion = request.form['anioPublicacion']
        isbn = request.form['isbn']
        stock = request.form['stock']
        libro = Libro(titulo=titulo, autor_id=autor, genero_id=genero,
                      anio_publicacion=anioPublicacion, isbn=isbn, stock=stock)
        db.session.add(libro)
        db.session.commit()
        return redirect('/libros')
    except Exception as err:
        print('Error: '+str(err))
        return render_template('500.html')

@libros_router.route('/libros/detalle/<int:id>')
def genero_detalle(id):
    generos = Genero.query.all()
    autores = Autor.query.all()
    libro = Libro.query.get_or_404(id)
    return render_template('libro/detalle.html', libro=libro, generos=generos, autores=autores)

@libros_router.route('/libros/editar/<int:id>', methods=['POST'])
def libro_editar(id):
    try:
        libro = Libro.query.get_or_404(id)
        libro.titulo = request.form['titulo']
        libro.autor_id = request.form['autor']
        libro.genero_id = request.form['genero']
        libro.anio_publicacion = request.form['anioPublicacion']
        libro.isbn = request.form['isbn']
        libro.stock = request.form['stock']
        db.session.commit()
        return redirect('/libros')
    except Exception as err:
        print(err)
        return render_template('500.html')

@libros_router.route('/libros/eliminar/<int:id>')
def libro_eliminar(id):
    try:
        libro = Libro.query.get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return redirect('/libros')
    except Exception as err:
        print(err)
        return render_template('500.html')