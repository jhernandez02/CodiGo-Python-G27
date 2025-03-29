const dotenv = require("dotenv");

dotenv.config();

const config = {
    port: process.env.PORT,
    dirUpload: process.env.DIR_UPLOADS,
};

module.exports = config;