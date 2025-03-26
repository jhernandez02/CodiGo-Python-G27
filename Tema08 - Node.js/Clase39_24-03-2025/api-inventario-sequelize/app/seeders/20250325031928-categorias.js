'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Categoria', [
      { nombre: 'Computadoras', createdAt: new Date(), updatedAt: new Date() },
      { nombre: 'Escritorios', createdAt: new Date(), updatedAt: new Date() },
      { nombre: 'Sillas', createdAt: new Date(), updatedAt: new Date() },
    ], {});
  },
  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Categoria', null, {});
  }
};
