const express = require('express');
const router = express.Router();
const proyectoController = require('../controllers/proyecto.controller');

router.get('/', (req, res)=>{
    res.json(proyectoController.listar());
});

router.get('/:id', (req, res)=>{
    const { id } = req.params;
    res.json(proyectoController.obtenerPorId(id));
});

router.post('/', (req, res)=>{
    res.json(proyectoController.crear(req.body));
});

router.put('/:id', (req, res)=>{
    const { id } = req.params;
    res.json(proyectoController.editar(id, req.body));
});

router.delete('/:id', (req, res)=>{
    const { id } = req.params;
    const resultado = proyectoController.eliminar(id);
    res.json({eliminado: resultado});
});

module.exports = router;