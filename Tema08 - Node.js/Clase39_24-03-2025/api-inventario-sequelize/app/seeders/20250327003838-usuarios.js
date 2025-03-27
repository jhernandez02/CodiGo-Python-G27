'use strict';
const bcrypt = require('bcryptjs');

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Usuarios', [{
      nombre: 'Carlos Linares',
      email: 'clinares@mail.com',
      password: await bcrypt.hash("123456", 10),
      createdAt: new Date(),
      updatedAt: new Date(),
    },{
      nombre: 'Karen Mendoza',
      email: 'kmendoza',
      password: await bcrypt.hash("123456", 10),
      createdAt: new Date(),
      updatedAt: new Date(),
    }], {});
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Usuarios', null, {});
  }
};
