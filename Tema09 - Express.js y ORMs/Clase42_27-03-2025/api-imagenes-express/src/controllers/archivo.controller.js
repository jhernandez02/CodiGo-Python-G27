const fs = require('fs');
const multer = require('multer');
const config = require('../config');

const controlador = {
    subir(req, res){
        // Configurar el almacenamiento en multer
        const storage = multer.diskStorage({
            destination: (req, file, cb) => {
                const { carpeta } = req.body;
                let rutaCarpeta = config.dirUpload;
                if(carpeta!='uploads'){
                    rutaCarpeta += `/${carpeta}`;
                }
                cb(null, rutaCarpeta)
            },
            filename: (req, file, cb) => {
                cb(null, Date.now() + '-' + file.originalname);
            }
        });
        const upload = multer({ storage }).single('archivo');
        try {
            upload(req, res,  (err) => {
                if (err instanceof multer.MulterError) {
                    const message = 'Un error de Multer ocurrió durante la subida.';
                    console.log(`Error - subirArchivo:  ${message}` , err);
                    return res.status(500).json({status:'error', message});
                } else if (err) {
                    const message = 'Un error desconocido ocurrió durante la subida.';
                    console.log(`Error - subirArchivo:  ${message}` , err);
                    return res.status(500).json({status:'error', message});
                }
                res.json({status:'ok', message:'Se subió el archivo'});
            });
        } catch (error) {
            console.log('Error - subirArchivo: ', error);
            const message = "No se puede subir el archivo";
            res.status(500).json({status:'error', message});
        }
    },
    renombrar(req, res){
        const { nombre, nuevoNombre, carpeta } = req.body;
        let rutaCarpeta = config.dirUpload;
        if(carpeta!='uploads'){
            rutaCarpeta += `/${carpeta}`;
        }
        const rutaArchivo = `${rutaCarpeta}/${nombre}`;
        const rutaNuevoArchivo = `${rutaCarpeta}/${nuevoNombre}`;
        try {
            fs.renameSync(rutaArchivo, rutaNuevoArchivo);
            res.json({status:'ok', message:'Se renombró el archivo'});
        } catch (error) {
            console.log('Error - renombrarArchivo: ', error);
            const message = "No se puede renombrar el archivo";
            res.status(500).json({status:'error', message});
        }
    },
    eliminar(req, res){
        const { nombre, carpeta } = req.params;
        let rutaCarpeta = config.dirUpload;
        if(carpeta!='uploads'){
            rutaCarpeta += `/${carpeta}`;
        }
        const rutaArchivo = `${rutaCarpeta}/${nombre}`;
        try {
            fs.unlinkSync(rutaArchivo);
            res.json({status:'ok', message:'Se eliminó el archivo'});
        } catch (error) {
            console.log('Error - eliminarArchivo: ', error);
            const message = "No se puede eliminar el archivo";
            res.status(500).json({status:'error', message});
        }
    }
};

module.exports = controlador;