from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from cryptography.fernet import Fernet
import base64
import os
import datetime

# Configuración
app = Flask(__name__)
app.config['SECRET_KEY'] = '8CFrJjebFZNzLX0Ky4vqebbpQkaIDHwt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/login_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'LqxYrxsqmVFeQIOKjESbMNGUM2CXXeqC'

# Configuración del envío de correo con los datos Mailtrap
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8e50ce09a46fcb'
app.config['MAIL_PASSWORD'] = '64adce1f46c1be'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicializamos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
mail = Mail(app)

FERNET_SECRET_KEY = Fernet.generate_key()
print('FERNET_SECRET_KEY:',FERNET_SECRET_KEY)
fernet = Fernet(FERNET_SECRET_KEY)

# Modelo Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Ruta para registrar usuarios
@app.route('/registro', methods=['POST'])
def registrar():
    data = request.json
    user = data['user']
    passwd = data['passwd']
    if not user or not passwd:
        return jsonify({
            "message": "Usuario y contraseña requeridos"
        })
    if Usuario.query.filter_by(username=user).first():
        return jsonify({
            "message": "El usuario ya existe"
        })
    nuevo_usuario = Usuario(username=user)
    nuevo_usuario.set_password(passwd)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "message": "Usuario registrado exitosamente"
    })

# Ruta para login y obtener el token
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data['user']
    passwd = data['passwd']
    usuario = Usuario.query.filter_by(username=user).first()
    # Validamos si existe el usuario o la contraseña es incorrecta
    if not usuario or not usuario.check_password(passwd):
        return({
            'message': 'Credenciales incorrectas'
        })
    # Generamos el token de acceso
    token = create_access_token(identity=str(usuario.username))
    return({
            'token': token
        })

def generate_reset_token(email, expiration=3600):
    # Obtenemos el tiempo actual en segundos
    timestamp = int(datetime.datetime.utcnow().timestamp())+expiration

    data = f"{email}|{timestamp}".encode()
    print('data:',data)
    token = fernet.encrypt(data) # Ciframos con Fernet
    return token.decode()

@app.route('/solicitud-recuperar-contrasena', methods=['POST'])
def solicitudRecuperarContrasena():
    data = request.json
    email = data['email']

    usuario = Usuario.query.filter_by(username=email).first()

    if not usuario:
        return jsonify({
            "message": "Email no encontrado"
        }), 404
    
    token = generate_reset_token(email)
    reset_url = f'http://localhost:5000/restablecer-contrasena/{token}'
    print(reset_url)

    # Envío de token por correo al usuario
    asunto = "Recuperación de contraseña"
    desde = 'noreply@codigo.edu.pe'
    destino = [email]
    mensaje = Message(asunto, sender=desde, recipients=destino)
    mensaje.body = f'Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}'
    mail.send(mensaje)

    return jsonify({
        "message": "Correo de recuperación enviado"
    })

def verify_reset_token(token):
    try:
        decrypted_data = fernet.decrypt(token.encode()).decode()
        print('decrypted_data:', decrypted_data)
        email, token_time = decrypted_data.split('|')

        token_time = int(token_time)
        current_time = int(datetime.datetime.utcnow().timestamp())
        print('token_time:',token_time)
        print('current_time:',current_time)

        if token_time < current_time:
            return None
        
        return email

    except Exception as err:
        return None
        print('Error:',err)

@app.route('/restablecer-contrasena/<token>', methods=['POST'])
def restablecerContrasena(token):
    data = request.json
    nueva_contrasena = data['password']

    email = verify_reset_token(token)
    if not email:
        return jsonify({
            "message": "Token inválido o expirado"
        })
    
    usuario = Usuario.query.filter_by(username=email).first()
    if not usuario:
        return jsonify({
            "message": "Usuario no encontrado"
        })
    
    usuario.set_password(nueva_contrasena)
    db.session.commit()

    return jsonify({
        "message": "Contraseña actualizada correctamente"
    })