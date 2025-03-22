const errorHandleMiddleware = (err, req, res, next) =>{
    console.error(err);
    res.status(500).send('Algo salió mal');
}

module.exports = errorHandleMiddleware;