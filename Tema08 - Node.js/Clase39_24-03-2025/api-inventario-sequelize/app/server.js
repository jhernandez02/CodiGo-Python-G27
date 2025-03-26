const categoriaRutas = require('./routes/categoria.route');
const productoRutas = require('./routes/producto.route');
const express = require("express");
const app = express();

app.use(express.json());

// Implementamos las rutas
app.use('/categorias', categoriaRutas);
app.use('/productos', productoRutas);

const PORT = 3000;
app.listen(PORT, ()=>{
    console.log(`Servidor iniciado en el puerto ${PORT}`);
});