from flask import Blueprint, render_template, request, redirect
from models import db, Autor

autores_router = Blueprint('autores',__name__)

@autores_router.route('/autores')
def autor_index():
    autores = Autor.query.all()
    return render_template('autor/index.html', lista=autores)