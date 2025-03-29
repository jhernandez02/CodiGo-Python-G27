const fs = require('fs');
const config = require('../config');

const controlador = {
    listarContenido(req, res){
        const { carpeta } = req.params;
        let rutaCarpeta = config.dirUpload;
        if(carpeta!='uploads'){
            rutaCarpeta += `/${carpeta}`;
        }
        console.log('rutaCarpeta: ',rutaCarpeta);
        try {
            const contenido = fs.readdirSync(rutaCarpeta);
            const archivos = contenido.map((elem)=>{
                if(fs.lstatSync(`${rutaCarpeta}/${elem}`).isDirectory()){
                    return {
                        tipo: "folder",
                        nombre: elem,
                    }
                }else{
                    return {
                        tipo: "archivo",
                        nombre: elem
                    }
                }
            });
            res.json({status:'ok', archivos});
        } catch (error) {
            console.log('Error - listarContenido: ', error);
            const message = "No se puede leer el contenido de la carpeta";
            res.status(500).json({status:'error', message});
        }    
    },
    crearCarpeta(req, res){
        const { nombre } = req.body;
        const rutaCarpeta = `${config.dirUpload}/${nombre}`;
        try {
            fs.mkdirSync(rutaCarpeta);
            res.json({status:'ok', message:'Se creó la carpeta'});
        } catch (error) {
            console.log('Error - crearCarpeta: ', error);
            const message = "No se puede crear la carpeta";
            res.status(500).json({status:'error', message});
        }
    },
    renombrarCarpeta(req, res){
        const { nombre, nuevoNombre } = req.body;
        const rutaCarpeta = `${config.dirUpload}/${nombre}`;
        const rutaNuevaCarpeta = `${config.dirUpload}/${nuevoNombre}`;
        try {
            fs.renameSync(rutaCarpeta, rutaNuevaCarpeta);
            res.json({status:'ok', message:'Se renombró la carpeta'});
        } catch (error) {
            console.log('Error - renombrarCarpeta: ', error);
            const message = "No se puede renombrar la carpeta";
            res.status(500).json({status:'error', message});
        }
    },
    eliminarCarpeta(req, res){
        const { nombre } = req.params;
        const rutaCarpeta = `${config.dirUpload}/${nombre}`;
        try {
            fs.rmdirSync(rutaCarpeta);
            res.json({status:'ok', message:'Se eliminó la carpeta'});
        } catch (error) {
            console.log('Error - eliminarCarpeta: ', error);
            const message = "No se puede eliminar la carpeta";
            res.status(500).json({status:'error', message});
        }
    },
}

module.exports = controlador;