const express = require("express");
const socket = require("socket.io");
const app = express();

app.use(express.static('public'));

const server = app.listen(3000, ()=>{
    console.log("Servidor iniciado en el puerto 3000");
});

let total = 0;
const donantes = [];
const io = socket(server);

io.on("connection", (socket)=>{
    console.log("Socket conectado:", socket.id);
    socket.on("enviar-donacion", (datos)=>{
        console.log(datos);
        const persona = `${datos.nombre} ${datos.dni}`;
        donantes.push(persona);
        total += parseFloat(datos.monto);
        const mensaje = {
            persona,
            total
        }
        io.sockets.emit("respuesta", mensaje);
    });
});