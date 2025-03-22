const express = require('express');
const router = express.Router();
const usuarioController = require('../controllers/usuario.controller');

router.get('/', (req, res)=>{
    console.log('listar usuarios');
    res.json(usuarioController.listar());
});

router.get('/:id', (req, res)=>{
    const { id } = req.params;
    res.json(usuarioController.obtenerPorId(id));
});

router.post('/', (req, res)=>{
    res.json(usuarioController.crear(req.body));
});

router.put('/:id', (req, res)=>{
    const { id } = req.params;
    res.json(usuarioController.editar(id, req.body));
});

router.delete('/:id', (req, res)=>{
    const { id } = req.params;
    const resultado = usuarioController.eliminar(id);
    res.json({eliminado: resultado});
});

module.exports = router;