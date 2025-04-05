const libroModel = require("../models/libro.model");

const controlador = {
    async listar(req, res){
        try {
            const result = await libroModel.find()
                            .populate({path:"genero_id", select:['nombre']})
                            .populate({path:"autor_id", select:['nombres','apellidos']});
            res.json(result);
        } catch (error) {
            console.log('Error listar libros: ', error);
            res.sendStatus(500);
        }
    },
    async guardar(req, res){
        const { genero_id, autor_id, titulo, resumen, isbn } = req.body;
        try {
            const libro = new libroModel();
            libro.genero_id = genero_id;
            libro.autor_id = autor_id;
            libro.titulo = titulo;
            libro.resumen = resumen;
            libro.isbn = isbn;
            const result = await libro.save();
            res.json(result);
        } catch (error) {
            console.log('Error guadar libro: ', error);
            res.sendStatus(500);
        }
    },
    async buscarPorId(req, res){
        const { id } = req.params;
        try {
            const result = await libroModel.findById(id)
                                .populate({path:"genero_id", select:['nombre']})
                                .populate({path:"autor_id", select:['nombres','apellidos']});;
            res.json(result);
        } catch (error) {
            console.log('Error buscarPorId libros: ', error);
            res.sendStatus(500);
        }
    },
    async editar(req, res){
        const { id } = req.params;
        const { genero_id, autor_id, titulo, resumen, isbn, estado } = req.body;
        const updateData = { genero_id, autor_id, titulo, resumen, isbn, estado };
        const options = { new:true, runValidators: true };
        try {
            const result = await libroModel.findByIdAndUpdate(id, updateData, options);
            res.json(result);
        } catch (error) {
            console.log('Error editar libros: ', error);
            res.sendStatus(500);
        }
    },
    async eliminar(req, res){
        const { id } = req.params;
        try {
            await libroModel.findByIdAndDelete(id);
            const result = {
                message: "Registro eliminado"
            };
            res.json(result);
        } catch (error) {
            console.log('Error eliminar libro: ', error);
            res.sendStatus(500);
        }
    },
};

module.exports = controlador;