const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const generoRutas = require("./routes/genero.route");
const autorRutas = require("./routes/autor.route");
const libroRutas = require("./routes/libro.route");
const port = 3000;

require("dotenv").config();

const db_host = process.env.DB_HOST;
const db_user = process.env.DB_USER;
const db_pass = process.env.DB_PASS;
const db_name = process.env.DB_NAME;
const db_cluster = process.env.DB_CLUSTER;

mongoose.connect(`mongodb+srv://${db_user}:${db_pass}@${db_host}/${db_name}?retryWrites=true&w=majority&appName=${db_cluster}`)
.then(()=>{
    console.log("Conectados a la base de datos!");
})
.catch((error)=>{
    console.log("Error al conectar a la base de datos: ", error);
});

const app = express();
app.use(cors());
app.use(express.json());

app.use('/generos', generoRutas);
app.use('/autores', autorRutas);
app.use('/libros', libroRutas);

app.listen(port, ()=>{
    console.log(`Servidor iniciado en el puerto ${port}`);
});