const express = require("express");
const router = express.Router();
const generoController = require("../controllers/genero.controller");

router.get('/', (req, res)=>{
    generoController.listar(req, res);
});

router.post('/', (req, res)=>{
    generoController.guardar(req, res);
});

router.get('/:id', (req, res)=>{
    generoController.buscarPorId(req, res);
});

router.delete('/:id', (req, res)=>{
    generoController.eliminar(req, res);
});

module.exports = router;