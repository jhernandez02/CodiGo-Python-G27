# web/app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<strong>Pagina inicio</strong>"

@app.route("/hola")
def hola():
    return "<strong>Hola!</strong>"

@app.route("/saludar/<alumno>")
def saludar(alumno):
    return f"<strong>Hola! {alumno}</strong>"

@app.route("/sumar/n1/<num1>/n2/<num2>")
def sumar(num2,num1):
    total = int(num1) + int(num2)
    return f"<strong>{num1} + {num2} = {total}</strong>"

@app.route("/restar/n1/<int:num1>/n2/<int:num2>")
def restar(num2,num1):
    total = num1 - num2
    return f"<strong>{num1} - {num2} = {total}</strong>"