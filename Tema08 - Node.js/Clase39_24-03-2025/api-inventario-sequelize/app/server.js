const authRutas = require('./routes/auth.route');
const categoriaRutas = require('./routes/categoria.route');
const productoRutas = require('./routes/producto.route');
const authMiddleware = require('./middlewares/auth.middleware');
const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const app = express();

dotenv.config();
app.use(cors());
app.use(express.json());

// Implementamos las rutas
app.use('/auth', authRutas);

app.use(authMiddleware);
app.use('/categorias', categoriaRutas);
app.use('/productos', productoRutas);

const PORT = process.env.PORT;
app.listen(PORT, ()=>{
    console.log(`Servidor iniciado en el puerto ${PORT}`);
});