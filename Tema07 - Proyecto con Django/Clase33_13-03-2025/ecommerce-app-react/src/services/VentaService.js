import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL = `${API_URL}/ventas/api/v1/pedidos/`;

export const registrarPedidoService = async (data) => {
    const res = await Api().post(URL, data);
    return res;
}

export const listarPedidoService = async () => {
    const res = await Api().get(URL);
    return res;
}

export const mostrarPedidoService = async (id) => {
    const res = await Api().get(`${URL}/${id}`);
    return res;
}