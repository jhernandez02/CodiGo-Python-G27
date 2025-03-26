const categoriaController = require('../controllers/categoria.controller');
const express = require('express');
const router = express.Router();

router.get('/', (req, res)=>{
    categoriaController.listar(req, res);
});

router.get('/:id', (req, res)=>{
    categoriaController.obtnerPorId(req, res);
});

router.post('/', (req, res)=>{
    categoriaController.crear(req, res);
});

router.put('/:id', (req, res)=>{
    categoriaController.editar(req, res);
});

router.delete('/:id', (req, res)=>{
    categoriaController.eliminar(req, res);
});

module.exports = router;