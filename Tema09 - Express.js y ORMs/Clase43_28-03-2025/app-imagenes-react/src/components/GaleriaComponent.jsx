import { useEffect, useState } from "react";
import { 
    listarContenidoService, 
    eliminarCarpetaService 
} from "../services/CarpetaService";
import { eliminarArchivoService } from "../services/ArchivoService";
import FormularioComponent from './FormularioComponent';
import { API_URL } from "../Config";
import Swal from "sweetalert2";

function GaleriaComponent (){

    const ULR_IMG = `${API_URL}/uploads`;
    const ULR_IMG_FOLDER = `${API_URL}/img/folder.jpg`;
    const [lista, setLista] = useState([]);
    const [titulo, setTitulo] = useState('');
    const [urlImg, setUrlImagen] = useState(ULR_IMG);
    const [carpetaActual, setCarpetaActual] = useState('uploads');

    const listarArchivos = async (carpeta) =>{
        try {
            const urlImagen = carpeta=='uploads' ? ULR_IMG : `${ULR_IMG}/${carpeta}`;
            const titulo = carpeta=='uploads' ? '' : carpeta;
            setCarpetaActual(carpeta);
            setUrlImagen(urlImagen);
            setTitulo(titulo);
            const result = await listarContenidoService(carpeta);
            setLista(result.data.archivos);
        } catch (error) {
            console.error('Erro al cargar la lista de archivos:', error);
        }
    }

    const eliminarCarpetaArchivo = (tipo, nombre) => {
        Swal.fire({
            title: `Estas seguro de eliminar este ${tipo}?`,
            text: "Esta acción no se puede revertir!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sí, eliminar!",
            cancelButtonText: "Cancelar"
        }).then(async (result) => {
            if (result.isConfirmed) {
                if(tipo=='folder'){
                    await eliminarCarpetaService(nombre);
                }else{ // el recurso es tipo archivo
                    await eliminarArchivoService(carpetaActual, nombre);
                }
                listarArchivos(carpetaActual);
                Swal.fire({
                    title: "Eliminado!",
                    text: `El ${tipo} ha sido eliminado!`,
                    icon: "success"
                });
            }
          });
    };

    useEffect(()=>{
        listarArchivos('uploads');
    }, []);

    return (
        <div className="container mt-4">
            <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                    <li className="breadcrumb-item"><a onClick={()=>listarArchivos('uploads')} href="#">Inicio</a></li>
                    {titulo && (
                        <li className="breadcrumb-item active" aria-current="page">{titulo}</li>
                    )}
                </ol>
            </nav>
            <FormularioComponent carpeta={carpetaActual} listar={listarArchivos} />
            <div className="row">
                {lista.map((archivo, index)=>(
                    <div key={index} className="col-md-3">
                        <div className="card">
                            {archivo.tipo=='folder' ? (
                                <a onClick={()=>listarArchivos(archivo.nombre)} href="#">
                                    <img src={ULR_IMG_FOLDER} className="card-img-top" alt="archivo" />
                                </a>
                            ) : (
                                <img src={`${urlImg}/${archivo.nombre}`} className="card-img-top" alt="archivo" />
                            )}
                            <div className="card-body">
                                <h5 className="card-title">{archivo.nombre}</h5>
                                <p className="card-text">Tipo: {archivo.tipo}</p>
                                <div className="btn-group" role="group" aria-label="Basic example">
                                    <button type="button" className="btn btn-primary">Renombrar</button>
                                    <button onClick={()=>eliminarCarpetaArchivo(archivo.tipo,archivo.nombre)} type="button" className="btn btn-danger">Eliminar</button>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default GaleriaComponent;