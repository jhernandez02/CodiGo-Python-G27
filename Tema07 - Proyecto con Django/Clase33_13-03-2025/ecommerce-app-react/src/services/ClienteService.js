import axios from "axios";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/autenticacion/api/v1`;

export const loginClienteService = async (data) => {
    const res = await axios.post(`${URL}/login`, data);
    return res;
}