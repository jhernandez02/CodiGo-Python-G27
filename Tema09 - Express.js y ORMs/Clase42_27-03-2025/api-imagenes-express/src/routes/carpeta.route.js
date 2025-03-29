const carpetaController = require("../controllers/carpeta.controller");
const express = require("express");
const router = express.Router();

router.get('/:carpeta', (req, res)=>{
    carpetaController.listarContenido(req, res);
});

router.post('/', (req, res)=>{
    carpetaController.crearCarpeta(req, res);
});

router.put('/', (req, res)=>{
    carpetaController.renombrarCarpeta(req, res);
});

router.delete('/:nombre', (req, res)=>{
    carpetaController.eliminarCarpeta(req, res);
});

module.exports = router;