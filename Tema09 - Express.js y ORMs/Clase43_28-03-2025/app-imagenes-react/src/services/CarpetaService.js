import axios from "axios";
import { API_URL } from "../Config";

const URL = `${API_URL}/carpetas`;

export const listarContenidoService = async(directorio) => {
    const result = await axios.get(`${URL}/${directorio}`);
    return result;
};

export const crearCarpetaService = async(data) => {
    const result = await axios.post(`${URL}`, data);
    return result;
};

export const renombrarCarpetaService = async(data) => {
    const result = await axios.put(`${URL}`, data);
    return result;
};

export const eliminarCarpetaService = async(directorio) => {
    const result = await axios.delete(`${URL}/${directorio}`);
    return result;
};