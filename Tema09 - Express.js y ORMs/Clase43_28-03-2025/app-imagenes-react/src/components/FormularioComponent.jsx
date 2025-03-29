import { useState } from "react";
import { subirArchivoService } from "../services/ArchivoService";
import Swal from "sweetalert2";

function FormularioComponent (){
    const [archivo, setArchivo] = useState(null);
    
    const seleccionarArchivo = (e) => {
        setArchivo(e.target.files[0]);
    };

    const subirArchivo = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('carpeta','uploads');
        formData.append('archivo', archivo);
        await subirArchivoService(formData);
        Swal.fire({
            title: "Archivo subido!",
            text: `El archivo ha sido subido satisfactoriamente!`,
            icon: "success"
        });
    };
    return (
        <div className="container mt-4">
            <form onSubmit={subirArchivo}>
                <div className="mb-3">
                    <label htmlFor="formFile" className="form-label">Subir un archivo en la carpeta principal</label>
                    <input onChange={seleccionarArchivo} className="form-control" type="file" id="formFile" />
                    <button type="submit" className="btn btn-success mt-3">Subir archivo</button>
                </div>
            </form>
        </div>
    );
}

export default FormularioComponent;