'use strict';
const { Model } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Producto extends Model {
    static associate(models) {
      Producto.belongsTo(models.Categoria, {
        foreignKey: 'CategoriaId', // la clave foranea
        as: 'categoria', // el nombre del alias para la relación
      });
    }
  }
  Producto.init({
    nombre: DataTypes.STRING,
    cantidad: DataTypes.INTEGER,
    precio: DataTypes.FLOAT,
    CategoriaId: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'Producto',
  });
  return Producto;
};