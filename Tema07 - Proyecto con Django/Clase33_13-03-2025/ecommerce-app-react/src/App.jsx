import  { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AppProvider } from './contexts/AppContext';
import CabeceraComponent from './components/CabeceraComponent';
import PrincipalPage from './pages/PrincipalPage';
import ProductoPage from './pages/ProductoPage';
import CarritoPage from './pages/CarritoPage';
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <AppProvider>
        <CabeceraComponent />
        <Routes>
          <Route path='/' element={<PrincipalPage />} />
          <Route path='/producto/:id' element={<ProductoPage />} />
          <Route path='/carrito' element={<CarritoPage />} />
        </Routes>
      </AppProvider>
    </BrowserRouter>
  )
}

export default App;
