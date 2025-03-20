import axios from "axios";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/almacen/api/v1/categorias`;

export const listarCategoriaService = async () => {
    const res = await axios.get(URL);
    return res;
}

export const mostrarCategoriaService = async (id) => {
    const res = await axios.get(`${URL}/${id}`);
    return res;
}