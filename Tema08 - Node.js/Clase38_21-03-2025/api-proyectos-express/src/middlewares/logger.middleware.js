const loggerMiddleware = (req, res, next)=>{
    console.log(`Solicitado ${req.method} en ${req.url}`);
    next();
};

module.exports = loggerMiddleware;