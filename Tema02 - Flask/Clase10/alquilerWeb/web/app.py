# web/app.py

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

lista = [
    {'precio':'S/ 2,620 - USD 1,140', 'descripcion':'Departamento | Av. Juan de Arona 110','enlace':'alquiler-123'},
    {'precio':'S/ 2,100', 'descripcion':'Departamento | Av. Vivanco 248','enlace':'alquiler-237'},
    {'precio':'S/ 2,450 - USD 690', 'descripcion':'Departamento | Av. Las Flores 4856 Dpto 705','enlace':'alquiler-381'}
]

@app.route('/')
def index():
    return render_template('index.html', alquileres=lista)

@app.route('/detalle/<url_seo>')
def detalle(url_seo):
    inmueble = None
    for item in lista:
        if item['enlace']==url_seo:
            inmueble = item
            break
    return render_template('detalle.html', inmueble=inmueble)

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    # Ingresar los dato en la BD
    # Enviar un correo de confirmación
    print(nombre,email,mensaje)
    response = {'mensaje':'Hola '+nombre+', pronto nos estaremos comunicando contigo'} 
    return jsonify(response)

