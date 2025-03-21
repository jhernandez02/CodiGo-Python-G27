const express = require('express');
const app = express();
app.use(express.json());

const libroController = require('./controllers/libro.controller');

app.get('/', (req, res)=>{
    res.json({mensaje:'hola codigo'});
});

app.get('/libros', (req, res)=>{
    res.json(libroController.listar());
});

app.post('/libros', (req, res)=>{
    res.json(libroController.crear(req.body));
});

app.get('/libros/:id', (req, res)=>{
    const { id } = req.params;
    res.json(libroController.obtenerPorId(id));
});

app.put('/libros/:id', (req, res)=>{
    const { id } = req.params;
    res.json(libroController.editar(id, req.body));
});

app.delete('/libros/:id', (req, res)=>{
    const { id } = req.params;
    res.json(libroController.eliminar(id, req.body));
});

app.listen(3000, ()=>{
    console.log('Servidor iniciado en el puerto 3000');
});