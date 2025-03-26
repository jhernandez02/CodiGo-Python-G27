const { Producto, Categoria } = require('../models');

const controlador = {
    async listar(req, res){
        const result = await Producto.findAll({
            //include: Categoria,   // obtenemos la relación con el modelo
            include: 'categoria',   // obtenemos la relación con el alias
        });
        res.json(result);
    },
    async obtnerPorId(req, res){
        const { id } = req.params;
        const result = await Producto.findByPk(id, {
            include: [{
                model: Categoria,
                as: 'categoria'
            }]
        });
        res.json(result);
    },
    async crear(req, res){
        const { nombre, cantidad, precio, CategoriaId } = req.body;
        const data = { 
            nombre, 
            cantidad,
            precio,
            CategoriaId,
            createdAt: new Date(), 
            updatedAt: new Date() 
        };
        const result = await Producto.create(data);
        res.json(result);
    },
    async editar(req, res){
        const { id } = req.params;
        const { nombre, cantidad, precio, CategoriaId } = req.body;
        const data = { 
            nombre, 
            cantidad,
            precio,
            CategoriaId, 
            updatedAt: new Date() 
        };
        const where = {
            where: { id, }, // Condición para encontrar la categoria por su id
            returning: true // Se indica que se devuelva el registro actualizado
        }
        const [updatedRows, result] = await Producto.update(data, where);
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
        const result = await Producto.destroy(where);
        res.json({eliminados:result});
    },
}

module.exports = controlador;