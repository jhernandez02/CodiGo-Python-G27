const productoController = require('../controllers/producto.controller');
const express = require('express');
const router = express.Router();

router.get('/', (req, res)=>{
    productoController.listar(req, res);
});

router.get('/:id', (req, res)=>{
    productoController.obtnerPorId(req, res);
});

router.post('/', (req, res)=>{
    productoController.crear(req, res);
});

router.put('/:id', (req, res)=>{
    productoController.editar(req, res);
});

router.delete('/:id', (req, res)=>{
    productoController.eliminar(req, res);
});

module.exports = router;
