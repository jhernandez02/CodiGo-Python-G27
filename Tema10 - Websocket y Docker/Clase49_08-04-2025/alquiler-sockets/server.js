const express = require("express");
const socket = require("socket.io");
const app = express();

app.use(express.static("public"));

const autos = [
    {cod:1, marca:"Toyota", modelo:"Corolla Cross 2.0 CVT",costo:70, anio:2022, caja:'Automático', combustible:"Gasolina", imagen:"toyota-corolla.jpg", estado:1},
    {cod:2, marca:"Ford", modelo:"Territory Trend 1.5 AT",costo:75, anio:2021, caja:'Automático', combustible:"Gasolina", imagen:"ford-territory.jpg", estado:1},
    {cod:3, marca:"Haval", modelo:"New H6",costo:60, anio:2022, caja:'Automático', combustible:"Gasolina", imagen:"haval-newh6.jpg", estado:1},
];

app.get('/autos', (req, res)=>{
    res.json(autos);
});

const server = app.listen(3000, ()=>{
    console.log("Servidor iniciado en el puerto 3000");
});

const io = socket(server);

io.on('connection', (socket)=>{
    console.log('Socket conectado', socket.id);
    // Ejecutamos cuando nos envian datos por el canal "alquiler"
    socket.on('alquiler', (codigo)=>{
        console.log('codigo: ', codigo);
        const auto = autos.find(auto=>auto.cod==codigo);
        auto.estado = 0;
        // Emitir a todos los demás sockets menos al que esta enviando el mensaje
        socket.broadcast.emit('respuesta', codigo);
    })
});