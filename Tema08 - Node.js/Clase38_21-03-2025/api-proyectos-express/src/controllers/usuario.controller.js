let listaUsuarios = require('../data/usuarios');
let nextID = 4;

const controlador = {
    listar(){
        return listaUsuarios;
    },
    crear(datos){
        const { nombres, rol, email } = datos;
        const usuario = {
            id: nextID,
            nombres,
            rol,
            email
        };
        listaUsuarios.push(usuario);
        nextID++;
        return usuario;
    },
    obtenerPorId(id){
        const usuario = listaUsuarios.find(usuario=>usuario.id==id);
        return usuario;
    },
    editar(id, datos){
        const { nombres, rol, email } = datos;
        const usuario = listaUsuarios.find(usuario=>usuario.id==id);
        usuario.nombres = nombres;
        usuario.rol = rol;
        usuario.email = email;
        return usuario;
    },
    eliminar(id){
        const usuario = listaUsuarios.find(usuario=>usuario.id==id);
        if(usuario){
            listaUsuarios = listaUsuarios.filter(usuario=>usuario.id!=id);
            return true;
        }else{
            return false;
        }
    },
};

module.exports = controlador;