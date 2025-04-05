const express = require("express");
const router = express.Router();
const autorController = require("../controllers/autor.controller");

router.get('/', (req, res)=>{
    autorController.listar(req, res);
});

router.post('/', (req, res)=>{
    autorController.guardar(req, res);
});

router.get('/:id', (req, res)=>{
    autorController.buscarPorId(req, res);
});

router.put('/:id', (req, res)=>{
    autorController.editar(req, res);
});

router.delete('/:id', (req, res)=>{
    autorController.eliminar(req, res);
});

module.exports = router;