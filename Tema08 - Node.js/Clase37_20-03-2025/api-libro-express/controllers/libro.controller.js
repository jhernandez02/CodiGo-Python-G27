let listaLibros = require('../data/libros');
let nextID = 4;

const controlador = {
    listar(){
        return listaLibros
    },
    crear(datos){
        const { titulo, autor } = datos;
        const libro = {
            id: nextID,
            titulo,
            autor
        }
        listaLibros.push(libro);
        nextID++;
        return libro;
    },
    obtenerPorId(id){
        const libro = listaLibros.find(libro=>libro.id==id);
        return libro;
    },
    editar(id, datos){
        const { titulo, autor } = datos;
        const libro = listaLibros.find(libro=>libro.id==id);
        libro.titulo = titulo;
        libro.autor = autor;
        return libro;
    },
    eliminar(id){
        listaLibros = listaLibros.filter(libro=>libro.id!=id);
        return true;
    }
}

module.exports = controlador;