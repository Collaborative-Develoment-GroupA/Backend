
import './App.css';
import './styles/css/login.css';
// import './styles/css/register.css'
import './styles/css/officer.css'
import './styles/css/accident.css';
import './styles/css/home.css';
import './styles/css/ticket.css';
import './styles/css/navbar.css';
import './styles/css/forgetpassword.css';
import './styles/css/department.css';
import './styles/css/code.css';
import './styles/css/reset.css';



import React from 'react';
import {
  BrowserRouter as Router,
  Routes,

  Route,

} from "react-router-dom";

import { Home } from './components/Home';

import { Accidents } from './components/Accidents';
import { Login } from './components/Login';
// import { Register } from './components/Register';

import Navbar from './components/Navbar';
import { Department } from './components/Department';
import { Tickets } from './components/Tickets';
import { Officer } from './components/Officer';
import {ForgetPage } from './components/forgetpassword';
import { CodePage } from './components/code';
import { ResetPage } from './components/reset';

function App() {
      return (
    <Router>
    
      {/* <Sidebar/> */}
      
      <Routes>
        <Route exact path="/" element={<Login />} />
        <Route exact path="/home" element={<Home />} />
        <Route exact path="/officer" element={<Officer />} />
        <Route exact path="/departments" element={<Department />} />
        <Route exact path="/tickets" element={<Tickets />} />
        <Route exact path="/accidents" element={<Accidents />} />
        <Route exact path="/login" element={<Login />} />
        <Route exact path="/forgetpassword" element={<ForgetPage />} />
        <Route exact path="/code" element={<CodePage />} />
        <Route exact path="/reset" element={<ResetPage />} />
        <Route exact path="/login" element={<Login />} />

        {/* <Route exact path="/register" element={<Register />} /> */}
      </Routes>

    </Router>


  );
}
export default App;


