const { Categoria, Producto } = require('../models');

const controlador = {
    async listar(req, res){
        const result = await Categoria.findAll({
            include: [{
                model: Producto,
                as: 'productos'
            }]
        });
        res.json(result);
    },
    async obtnerPorId(req, res){
        const { id } = req.params;
        const result = await Categoria.findByPk(id);
        res.json(result);
    },
    async crear(req, res){
        const { nombre } = req.body;
        const data = { 
            nombre, 
            createdAt: new Date(), 
            updatedAt: new Date() 
        };
        const result = await Categoria.create(data);
        res.json(result);
    },
    async editar(req, res){
        const { id } = req.params;
        const { nombre } = req.body;
        const data = { 
            nombre, 
            updatedAt: new Date() 
        };
        const where = {
            where: { id, }, // Condición para encontrar la categoria por su id
            returning: true // Se indica que se devuelva el registro actualizado
        }
        const [updatedRows, result] = await Categoria.update(data, where);
        console.log('Registros actualizados:', updatedRows);
        res.json(result[0]);
    },
    async eliminar(req, res){
        const { id } = req.params;
        const where = {
            where: {
              id,
            },
        };
        const result = await Categoria.destroy(where);
        res.json({eliminados:result});
    },
}

module.exports = controlador;