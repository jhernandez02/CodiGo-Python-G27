import axios from "axios";
import { API_URL } from "../Config";

const URL = `${API_URL}/archivos`;

export const subirArchivoService = async(data) => {
    const  headers = {
        'Content-Type': 'multipart/fomr-data'
    }
    const result = await axios.post(`${URL}`, data, { headers });
    return result;
};

export const renombrarArchivoService = async(data) => {
    const result = await axios.put(`${URL}`, data);
    return result;
};

export const eliminarArchivoService = async(directorio, archivo) => {
    const result = await axios.delete(`${URL}/${directorio}/${archivo}`);
    return result;
};