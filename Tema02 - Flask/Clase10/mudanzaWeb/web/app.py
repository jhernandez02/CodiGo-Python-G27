# web/app.py

from flask import Flask, request, render_template

app = Flask(__name__)

# Request: http://localhost:5000 (Get)
@app.route("/")
def index():
    return render_template('index.html')

# Request: http://localhost:5000/nosotros (Get)
@app.route("/nosotros")
def nosotros():
    return render_template('nosotros.html')

# Request: http://localhost:5000/servicios (Get)
@app.route("/servicios")
def servicios():
    var_titulo = 'Nuestros Servicios'
    var_descripcion = 'Elige uno de nuestros servicios disponibles:'
    var_enlaces = {
        'Servicio de Mundaza': '/servicios/mudanza',
        'Servicio de Embalaje': '/servicios/embalaje',
        'Servicio de Estiba': '/servicios/estiba',
        'Servicio de Transporte de carga': '/servicios/transporte-carga',
        'Otro Servicio': '/servicios/otro'
    }
    return render_template('servicios.html', titulo=var_titulo, descripcion=var_descripcion, enlaces=var_enlaces)

# Request: http://localhost:5000/servicios/mudanza (Get)
# Request: http://localhost:5000/servicios/embalaje (Get)
# Request: http://localhost:5000/servicios/estiba (Get)
# Request: http://localhost:5000/servicios/transporte-carga (Get)
# Request: http://localhost:5000/servicios/limpieza (Get)
@app.route("/servicios/<urlseo>")
def servicioDetalle(urlseo):
    try:
        plantilla = 'servicio-'+urlseo+'.html'
        return render_template(plantilla)
    except:
        return render_template('404.html')

# Request: http://localhost:5000/contacto (Get)
@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

# Request: http://localhost:5000/contacto/respuesta (Post)
# en methods se indica que la ruta se ejecuta con el método POST
@app.route("/contacto/respuesta", methods=['POST'])
def respuesta():
    respuesta = {
        'nombre': request.form['nombre'],
        'telefono': request.form['telefono'],
        'email' : request.form['email'],
        'mensaje' : request.form['mensaje']
    }
    return render_template('respuesta.html', datos=respuesta)

# Manejo del error 404: Pá  gina no encontrada
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html'), 404