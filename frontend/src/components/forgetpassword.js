import React from 'react';
import Navbar from './Navbar';
import { Link } from 'react-router-dom';

export const ForgetPage = () => {
  return (
    <>
     <div className="log-icon">
          <img src="assest/images/logo.png" alt="TMS" />
          <h2 className="text">TRAFFIC MANAGEMENT SYSTEM</h2>
        </div>

      <div className="contentlog">
        <div classNameName='logtxtcontainer'>
  
  
        <h1>
          TRAFFIC <br /><span>MANAGEMENT</span> <br />SYSTEM
        </h1>
        <p className="par">Welcome to the Traffic Management System (TMS). As a 
          <br /> traffic officer you play a critical role in ensuring the safety
          <br /> and smooth flow of traffic on our roads. We understand that your 
      
          <br/>job can be challenging and stressful at times,  which 
          <br />is why we have developed this system to support you in your duties.</p>
        </div>
    
            
  
        <div className="formlog">
          <h2 classNameName='logintxt'>Forget Password</h2>
        <div className='paragraph'>
            <p>Please enter the valid email to get the <br/>verification code for password reset.</p>
        </div>
        <input type="email" name="email" placeholder="E-mail" />
       
        <button class="log" id="forgetbtn"><Link to="/code">Send</Link></button>

        <br />
        <div className="forget-container">
         <Link to="/login">Back login
          </Link>
        </div>
        

      

      </div>
    </div>
    </>
  )
}
