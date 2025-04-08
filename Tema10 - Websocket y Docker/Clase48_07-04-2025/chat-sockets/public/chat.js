const socket = io();

const cajaUsuario = document.getElementById('inputUsuario');
const cajaMensaje = document.getElementById('inputMensaje');

function enviar(){
    const datos = {
        usuario: cajaUsuario.value,
        mensaje: cajaMensaje.value
    }
    console.log('enviando datos: ', datos);
    
    // Enviamos datos al servidor por medio de "canal mensaje"
    socket.emit('canal-mensaje', datos);
    cajaMensaje.value = ''; // Limpiar la caja mensaje
}

socket.on('canal-mensaje', (data)=>{
    console.log('recuperando datos: ', data);
    const areaMensajes = document.getElementById('mensajes');
    areaMensajes.innerHTML += `<p>${data.usuario}: ${data.mensaje}</p>`
});