const bcrypt = require('bcryptjs');
const dotenv = require("dotenv");
const jwt = require("jsonwebtoken");
const { Usuario } = require('../models');

dotenv.config();

const controlador = {
    async login(req, res){
        const { email, password } = req.body;
        try {
            const usuario = await Usuario.findOne({where: { email }});
            if(!usuario){ // Usuario no encontrado
                return res.status(404).json({error: 'Credenciales incorrectas'});
            }
            // Verificamos la contraseña
            const validPassword = bcrypt.compareSync(password, usuario.password);

            if(!validPassword){ // El password no es válido
                return res.status(404).json({error: 'Credenciales incorrectas'});
            }

            // Generamos el JWT
            const token = jwt.sign(
                {id: usuario.id}, // payload
                process.env.JWT_SECRET,
                { expiresIn: '4h' }
            )

            res.json({ token }); // output => {"token": "..."}
            
        } catch (error) {
            console.error(error);
            res.status(500).json({error: "Error al iniciar sesión"});
        }
    },
}

module.exports = controlador;