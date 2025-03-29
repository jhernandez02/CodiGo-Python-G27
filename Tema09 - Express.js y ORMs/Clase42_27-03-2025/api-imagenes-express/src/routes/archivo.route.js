const archivoController = require("../controllers/archivo.controller");
const express = require("express");
const router = express.Router();

router.post('/', (req, res)=>{
    archivoController.subir(req, res);
});

router.put('/', (req, res)=>{
    archivoController.renombrar(req, res);
});

router.delete('/:carpeta/:nombre', (req, res)=>{
    archivoController.eliminar(req, res);
});

module.exports = router;