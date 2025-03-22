const express = require('express');
const loggerMiddleware = require('./middlewares/logger.middleware');
const validateMiddleware = require('./middlewares/validate.middleware');
const errorHandleMiddleware = require('./middlewares/error.middleware');
const proyectoRutas = require('./routes/proyecto.route');
const usuarioRutas = require('./routes/usuario.route');

const app = express();
app.use(express.json());

// Middleware de aplicación
app.use(loggerMiddleware);

// Implementamos las rutas
app.use('/proyectos', proyectoRutas);
// Middleware específico para rutas
app.use('/usuarios', validateMiddleware, usuarioRutas);

app.get('/error', (req, res)=>{
    throw new Error('!Ha ocurrido un error!');
});

// Middleware de manejo de errores
app.use(errorHandleMiddleware);

app.listen(3000, ()=>{
    console.log('Servidor iniciado en el puerto 3000');
});