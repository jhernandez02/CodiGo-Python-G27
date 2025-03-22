let listaProyectos = require('../data/proyectos');
let nextID = 4;

const controlador = {
    listar(){
        return listaProyectos;
    },
    crear(datos){
        const { nombre } = datos;
        const proyecto = {
            id: nextID,
            nombre
        };
        listaProyectos.push(proyecto);
        nextID++;
        return proyecto;
    },
    obtenerPorId(id){
        const proyecto = listaProyectos.find(proyecto=>proyecto.id==id);
        return proyecto;
    },
    editar(id, datos){
        const { nombre } = datos;
        const proyecto = listaProyectos.find(proyecto=>proyecto.id==id);
        proyecto.nombre = nombre;
        return proyecto;
    },
    eliminar(id){
        const proyecto = listaProyectos.find(proyecto=>proyecto.id==id);
        if(proyecto){
            listaProyectos = listaProyectos.filter(proyecto=>proyecto.id!=id);
            return true;
        }else{
            return false;
        }
    },
};

module.exports = controlador;