const express = require("express");
const router = express.Router();
const libroController = require("../controllers/libro.controller");

router.get('/', (req, res)=>{
    libroController.listar(req, res);
});

router.post('/', (req, res)=>{
    libroController.guardar(req, res);
});

router.get('/:id', (req, res)=>{
    libroController.buscarPorId(req, res);
});

router.put('/:id', (req, res)=>{
    libroController.editar(req, res);
});

router.delete('/:id', (req, res)=>{
    libroController.eliminar(req, res);
});

module.exports = router;