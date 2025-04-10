const express = require("express");
const socket = require("socket.io");
const app = express();

app.use(express.static('public'));

const server = app.listen(3000, ()=>{
    console.log("Servidor iniciado en el puerto: 3000");
});

const io = socket(server);
// Cuando alguien se conecta
io.on("connection", (socket)=> {
    console.log("Socket conectado:", socket.id);

    // Esperando a que le envien datos desde el cliente por "canal-mensaje",
    // y esos datos los recupera en la variable "data"
    socket.on("canal-mensaje", (data)=>{
        console.log(data);
        // El servidor envia la data recuperda a todos (incluyendo al emisor)
        // los clientes que estan a la escucha de ese canal
        io.sockets.emit('canal-mensaje', data);
    });

    // Cuando el socket se desconecta
    socket.on("disconnect", ()=>{
        console.log("Usuario se acabo de desconectar:", socket.id);
    });
});