# web/app.py

from flask import Flask, render_template

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
    return render_template('servicios.html')

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

# Manejo del error 404: Pá  gina no encontrada
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html'), 404