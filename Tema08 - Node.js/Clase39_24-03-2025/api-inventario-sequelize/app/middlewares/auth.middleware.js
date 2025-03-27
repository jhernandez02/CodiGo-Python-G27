const jwt = require("jsonwebtoken");
const dotenv = require("dotenv");

dotenv.config();

const verifyToken = (req, res, next)=>{
    // Obtenemos el valor del token desde el valor de authorization
    const token = req.headers.authorization?.split(' ')[1];
    if(!token){ // En caso no encuentre el token en los headers
        return res.status(403).json({error: "Acceso denegado"});
    }
    jwt.verify(token, process.env.JWT_SECRET, (err, payload)=>{
        console.log('payload: ', payload);
        if(err){
            return res.status(403).json({error: "Token inválido"});
        }
        req.usuario = payload;
        next();
    });
};

module.exports = verifyToken;