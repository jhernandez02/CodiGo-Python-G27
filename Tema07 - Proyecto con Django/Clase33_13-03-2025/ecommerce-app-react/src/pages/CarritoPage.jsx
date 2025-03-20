import { useContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";
import { v4 as uuidv4 } from 'uuid';
import { AppContext } from "../contexts/AppContext";
import { registrarPedidoService } from "../services/VentaService";
import PayPalButtonComponent from "../components/PayPalButtonComponent";
import Swal from 'sweetalert2';

function CarritoPage(){
    const { usuario, carrito, setCarrito, token } = useContext(AppContext);
    const [total, setTotal] = useState(0);
    
    const eliminarProducto = (id) => {
        Swal.fire({
            title: "¿Estás seguro de eliminar este producto?",
            text: "Esta acción no se puede revertir.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sí, eliminar!",
            cancelButtonText: "No, cancelar"
        }).then((result) => {
            if (result.isConfirmed) {
                const nuevoCarrito = carrito.filter((item)=>item.id!=id);
                setCarrito(nuevoCarrito);
                Swal.fire({
                    title: "Eliminado!",
                    text: "El producto ha sido eliminado del carrito",
                    icon: "success"
                });
            }
        });
    }

    const generarCodigo = () => {
        return uuidv4().replace(/-/g, '').slice(0,9);
    }

    const handleComprar = async () => {
        const decoded = jwtDecode(token);
        const detalles = carrito.map((item)=>{
            return {
                producto: item.id,
                cantidad: 1,
                precio: item.precio
            };
        })
        const pedido = {
            cliente: decoded.user_id,
            codigo : "V-"+generarCodigo(),
            total: total,
            estado: "Pendiente",
            detalles: detalles
        }
        const res = await registrarPedidoService(pedido);
        setCarrito([]);
        Swal.fire({
            title: "Compra ingresada!",
            text: "Su compra ha sido ingresada satisfactoriamente",
            icon: "success"
        });
    }

    useEffect(()=>{
        let subTotal = 0;
        carrito.forEach((item)=>{
            subTotal += item.precio
        });
        setTotal(subTotal);
    }, [carrito]);

    return(
        <div className="container py-5">
            <h2>Carrito</h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Cantidad</th>
                        <th>Precio</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                {carrito.length>0 ? (
                    carrito.map((item)=>(
                        <tr key={item.id}>
                            <td>{item.nombre}</td>
                            <td>1</td>
                            <td>{item.precio}</td>
                            <td>
                                <button onClick={()=>eliminarProducto(item.id)} className="btn btn-danger btn-sm">
                                    <i class="bi bi-trash-fill"></i>
                                </button>
                            </td>
                        </tr>
                    ))
                ):(
                    <tr>
                        <td className="text-center" colSpan={5}>No hay productos agregados al carrito</td>
                    </tr>
                )}
                </tbody>
                <tfoot>
                    <tr>
                        <td className="text-end fw-bold" colSpan={2}>Total:</td>
                        <td className="fw-bold">{total}</td>
                        <td></td>
                    </tr>
                </tfoot>
            </table>
            <div className="py-2">
                {usuario ? (
                    <div className="w-50">
                        {/*<button onClick={handleComprar} className="btn btn-success">Comprar</button>*/}
                        {carrito.length>0 && (
                            <PayPalButtonComponent comprar={handleComprar} monto={total} />
                        )}
                    </div>
                ):(
                    <p className="text-danger fw-bold">Para comprar debes loguearte primero</p>
                )}
                
            </div>
        </div>
    );
}

export default CarritoPage;