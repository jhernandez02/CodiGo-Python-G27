import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { listarProductoService } from "../services/ProductoService";
import { IMG_URL } from "../utils/Config";
import Spinner from 'react-bootstrap/Spinner';
import Card from 'react-bootstrap/Card';

function PrincipalPage(){
    const [lista, setLista] = useState([]);
    const [cargando, setCargando] = useState(true);
    const listarProductos = async () =>{
        const res = await listarProductoService();
        setLista(res.data);
        setCargando(false);
    }
    useEffect(()=>{
        listarProductos();
    }, []);

    return(
        <>
            <section className="container py-5">
                <h1>Productos</h1>
                {cargando && (
                    <p className="text-center">
                        <Spinner animation="border" variant="primary" />
                        <div>Cargando...</div>
                    </p>
                )}
                <div className="mt-4 row">
                    {lista.map((producto)=>(
                        <div key={producto.id} className="col-md-3">
                            <Card className="mb-4">
                                <Card.Img variant="top" src={`${IMG_URL}${producto.imagen}`} />
                                <Card.Body>
                                    <Card.Title>{producto.nombre}</Card.Title>
                                    <Link to={`/producto/${producto.id}`} className="btn btn-primary">Ver detalle</Link>
                                </Card.Body>
                            </Card>
                        </div>
                    ))}
                </div>
            </section>
        </>
    );
}

export default PrincipalPage;