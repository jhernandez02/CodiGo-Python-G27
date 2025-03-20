import axios from "axios";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/almacen/api/v1/productos`;

export const listarProductoService = async () => {
    const res = await axios.get(URL);
    return res;
}

export const mostrarProductoService = async (id) => {
    const res = await axios.get(`${URL}/${id}`);
    return res;
}