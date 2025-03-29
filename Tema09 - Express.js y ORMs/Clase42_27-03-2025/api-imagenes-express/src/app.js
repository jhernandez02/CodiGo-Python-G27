const express = require("express");
const cors = require("cors");
const config = require("./config");
const carpetaRutas = require("./routes/carpeta.route"); 
const archivoRutas = require("./routes/archivo.route"); 

const app = express();

app.use(express.static('./public'));
app.use(cors());
app.use(express.json());

// Implementamos las rutas
app.use('/carpetas', carpetaRutas);
app.use('/archivos', archivoRutas);

app.listen(config.port, ()=>{
    console.log(`Servidor iniciado en el puerto ${config.port}`);
});