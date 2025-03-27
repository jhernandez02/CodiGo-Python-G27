const authController = require('../controllers/auth.controller');
const express = require('express');
const router = express.Router();

router.post('/', (req, res)=>{
    authController.login(req, res);
});

module.exports = router;