const validateMiddleware = (req, res, next)=>{
    console.log('validateMiddleware');
    // Si estamos creando un usuario tipo "admin"
    if(req.method=='POST' && req.body.rol=='admin'){
        res.json({message:"no permitido"});
    }
    next();
}

module.exports = validateMiddleware;