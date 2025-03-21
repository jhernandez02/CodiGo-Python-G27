let listaAutos = require('./data/auto');
const express = require('express');
const app = express();
// Permitimos el envío de datos en formato json por medio del cuerpo de la petición
app.use(express.json());

app.get('/', (req, res)=>{
    const respuesta = {
        mensaje: "Hola codigo"
    }
    res.json(respuesta);
});

app.get('/autos', (req, res)=>{
    res.json(listaAutos);
});

app.get('/autos/:cod', (req, res)=>{
    console.log(req.params);
    const { cod } = req.params;
    const auto = listaAutos.find((auto)=>auto.cod==cod);
    res.json(auto);
});

app.post('/autos', (req, res)=>{
    console.log(req.body);
    const { cod, marca, modelo, precio } = req.body;
    const nuevoAuto = { cod, marca, modelo, precio };
    listaAutos.push(nuevoAuto);
    res.json(nuevoAuto);
});

app.put('/autos/:cod', (req, res)=>{
    const { cod } = req.params;
    const { marca, modelo, precio } = req.body;
    const auto = listaAutos.find((auto)=>auto.cod==cod);
    auto.marca = marca;
    auto.modelo = modelo;
    auto.precio = precio;
    res.json(auto);
});

app.delete('/autos/:cod', (req, res)=>{
    const { cod } = req.params;
    listaAutos = listaAutos.filter((auto)=>auto.cod!=cod);
    res.sendStatus(200);
});

app.listen(3000, ()=>{
    console.log('Servidor iniciado en el puerto 3000')
});