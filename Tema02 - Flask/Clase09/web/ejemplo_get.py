# web/ejemplo_get.py

from flask import Flask

app = Flask(__name__)

# Request: http://localhost:5000 (Get)
@app.route("/")
def index():
    return "<p>Página Inicio</p>"

# Request: http://localhost:5000/operacion/sumar/48/17 (GET)
# Request: http://localhost:5000/operacion/restar/48/17 (GET)
@app.route("/operacion/<nombre>/<int:num1>/<int:num2>")
def operacion(nombre, num1, num2):
    html = f"<p>Operacion: {nombre}</p>"
    if nombre == 'sumar':
        resultado = num1 + num2
        html += f"<p>Resultado: {num1} + {num2} = {resultado}</p>"
    elif nombre == 'restar':
        resultado = num1 - num2
        html += f"<p>Resultado: {num1} - {num2} = {resultado}</p>"
    return html

# Request: http://localhost:5000/noticias/caene (Get)
# Request: http://localhost:5000/noticias/donald-trump (Get)
# Request: http://localhost:5000/noticias/caso-andrea-vidal (Get)
@app.route("/noticias/<categoria>")
def noticias(categoria):
    try:
        dict = {
            'caene': 'Caene',
            'donald-trump': 'Donald Trump',
            'caso-andrea-vidal': 'Caso Andrea Vidal'
        }
        return f"<p>Noticias: {dict[categoria]}</p>"
    except:
        return f"<p>Noticia no encontrada.</p>"