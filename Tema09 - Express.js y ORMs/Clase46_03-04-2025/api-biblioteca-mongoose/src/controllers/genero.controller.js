const generoModel = require("../models/genero.model");

const controlador = {
    async listar(req, res){
        try {
            const result = await generoModel.find(); // db.generos.find()
            res.json(result);
        } catch (error) {
            console.log('Error listar generos: ', error);
            res.sendStatus(500);
        }
    },
    async guardar(req, res){
        const { nombre } = req.body;
        try {
            const genero = new generoModel();
            genero.nombre = nombre;
            const result = await genero.save();
            res.json(result);
        } catch (error) {
            console.log('Error guadar genero: ', error);
            res.sendStatus(500);
        }
    },
    async buscarPorId(req, res){
        const { id } = req.params;
        try {
            const result = await generoModel.findById(id);
            res.json(result);
        } catch (error) {
            console.log('Error buscarPorId generos: ', error);
            res.sendStatus(500);
        }
    },
    async editar(req, res){
        const { id } = req.params;
        const { nombre, estado } = req.body;
        const updateData = { nombre, estado };
        const options = { new:true, runValidators: true };
        try {
            const result = await generoModel.findByIdAndUpdate(id, updateData, options);
            res.json(result);
        } catch (error) {
            console.log('Error editar generos: ', error);
            res.sendStatus(500);
        }
    },
    async eliminar(req, res){
        const { id } = req.params;
        try {
            await generoModel.findByIdAndDelete(id);
            const result = {
                message: "Registro eliminado"
            };
            res.json(result);
        } catch (error) {
            console.log('Error eliminar genero: ', error);
            res.sendStatus(500);
        }
    },
};

module.exports = controlador;