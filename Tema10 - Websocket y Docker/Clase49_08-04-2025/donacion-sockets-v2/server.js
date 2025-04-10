const express = require("express");
const socket = require("socket.io");
const app = express();

const PORT = 3000;

app.use(express.static('public'));

const server = app.listen(PORT, ()=>{
    console.log(`Servidor iniciado en el puerto: ${PORT}`);
});

let total = 0;
const donantes = [];
const io = socket(server);

io.on("connection", (socket)=>{
    console.log("Socket conectado:", socket.id);
    
    // Al conectarse un socket, se le envía el historial de donantes y el total
    socket.emit("historial", { total, donantes});

    socket.on("enviar-donacion", (datos)=>{
        console.log(datos);
        const persona = `${datos.nombre} ${datos.dni}`;
        donantes.push(persona);
        total += parseFloat(datos.monto);
        const mensaje = {
            persona,
            total
        }
        // Enviamos un mensaje por el canal "respuesta" 
        // a todos los sockets incluyendo al emisor
        io.sockets.emit("respuesta", mensaje);
    });
});