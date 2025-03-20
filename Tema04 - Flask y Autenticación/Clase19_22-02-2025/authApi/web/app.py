from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración
app = Flask(__name__)
app.config['SECRET_KEY'] = '8CFrJjebFZNzLX0Ky4vqebbpQkaIDHwt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/auth_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'LqxYrxsqmVFeQIOKjESbMNGUM2CXXeqC'

# Inicializamos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

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

# Ruta protegida
@app.route('/protegida', methods=['GET'])
@jwt_required()
def protegida():
    # Accedemos al valor añadido en el token
    usuario = get_jwt_identity()
    return({
        'message': f'Bienvenido, usuario {usuario}'
    })