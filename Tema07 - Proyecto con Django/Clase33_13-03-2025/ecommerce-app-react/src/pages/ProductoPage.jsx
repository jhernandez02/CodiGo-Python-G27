import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import { AppContext } from "../contexts/AppContext";
import { mostrarProductoService } from "../services/ProductoService";
import { IMG_URL } from "../utils/Config";
import Spinner from 'react-bootstrap/Spinner';
import Swal from 'sweetalert2'

const initData = {
    id: 0,
    nombre: "",
    description: "",
    precio: 0,
    imagen: "",
    stock: 0,
    categoria: 0
}

function ProductoPage(){
    const { id } = useParams();
    const { carrito, setCarrito } = useContext(AppContext); 
    const [producto, setProducto] = useState(initData);
    const [cargando, setCargando] = useState(true);

    const mostrarProducto = async () => {
        const res  = await mostrarProductoService(id);
        const datos = res.data
        setProducto({
            id: datos.id,
            nombre: datos.nombre,
            description: datos.description,
            precio: datos.precio,
            imagen: datos.imagen,
            stock: datos.stock,
            categoria: datos.categoria
        });
        setCargando(false);
    }

    const agregarProduto = () => {
        const existe = carrito.find((item)=>item.id==producto.id);
        console.log(existe);
        if(!existe){
            const nuevoCarrito = [...carrito, producto];
            setCarrito(nuevoCarrito);
            console.log(nuevoCarrito);
            Swal.fire({
                icon: "success",
                title: "Producto agregado!",
                text: "El producto ha sido agregado al carrito",
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Aceptar"
            });
        }else{
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "El producto ya ha sido agregado al carrito!",
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Aceptar"
            });
        }
    }

    useEffect(()=>{
        mostrarProducto();
    }, [id]);
    
    return(
        <div className="container py-5">
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ) : (
                <div className="row">
                    <div className="col-md-6">
                        <img src={`${IMG_URL}/${producto.imagen}`} className="w-100" alt="producto" />
                    </div>
                    <div className="col-md-6">
                        <h2>{producto.nombre}</h2>
                        <p>{producto.description}</p>
                        <h1 className="text-success">S/ {producto.precio}</h1>
                        <button onClick={agregarProduto} className="btn btn-primary mt-2 fs-4 w-100">Comprar</button>
                    </div>
                </div>
            )}
        </div>
    );
}

export default ProductoPage;