'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Productos', [
      {
        nombre: 'PC Lenovo 456',
        cantidad: 10,
        precio: 850,
        CategoriaId: 1,
        createdAt: new Date(), 
        updatedAt: new Date()
      },
      {
        nombre: 'Escritorio de madera',
        cantidad: 20,
        precio: 1800,
        CategoriaId: 2,
        createdAt: new Date(), 
        updatedAt: new Date()
      },
      {
        nombre: 'Silla ergonomicas',
        cantidad: 20,
        precio: 2600,
        CategoriaId: 3,
        createdAt: new Date(), 
        updatedAt: new Date()
      }
    ], {});
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Productos', null, {});
  }
};
