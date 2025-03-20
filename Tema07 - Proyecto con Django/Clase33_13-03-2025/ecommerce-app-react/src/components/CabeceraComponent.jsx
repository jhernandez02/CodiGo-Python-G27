import { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AppContext } from "../contexts/AppContext";
import { loginClienteService } from "../services/ClienteService";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Swal from 'sweetalert2'

function CabeceraComponent() {
  const navigate = useNavigate();
  const {carrito, usuario, login, logout} = useContext(AppContext);
  const [credenciales, setCredenciales] = useState({username:"", password:""});

  const handleChange = (e) => {
    // name => username | password
    const { name, value } = e.target;
    const nuevoDato = {...credenciales, [name]: value};
    //console.log('nuevoDato:', nuevoDato);
    setCredenciales(nuevoDato);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await loginClienteService(credenciales);
      console.log(res);
      login(credenciales.username, res.data.access);
    } catch (error) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Credenciales incorrectas!",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "Aceptar"
      });
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand href="#home">Ecommerce</Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse className="justify-content-end">
          <Nav className="me-auto">
              <li className="nav-item">
                  <Link to="/" className="nav-link">Inicio</Link>
              </li>
          </Nav>
          <Navbar.Text>
            {usuario ? (
              <div className="me-3">
                Bienvenido {usuario} | <a onClick={handleLogout} href="#" className="text-secondary">Salir</a>
              </div>
            ):(
              <form onSubmit={handleSubmit} className="row g-3 me-1">
                <div className="col-auto">
                  <label className="visually-hidden">Usuario</label>
                  <input type="text" onChange={handleChange} className="form-control" name="username" placeholder="Usuario" required />
                </div>
                <div className="col-auto">
                  <label className="visually-hidden">Contraseña</label>
                  <input type="password" onChange={handleChange} className="form-control" name="password" placeholder="Contraseña" required />
                </div>
                <div className="col-auto">
                  <button type="submit" className="btn btn-primary">Ingresar</button>
                </div>
              </form>
            )}
          </Navbar.Text>
          <Link className="btn btn-secondary position-relative" to="/carrito">
            <i className="bi bi-cart-fill"></i>
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
              {carrito.length}
            </span>
          </Link>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default CabeceraComponent;