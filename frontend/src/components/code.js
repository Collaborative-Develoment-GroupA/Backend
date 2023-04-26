import React from 'react';
import Navbar from './Navbar';

import { Link } from 'react-router-dom';

export const CodePage = () => {
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
        <h2 classNameName='logintxt'>Code Verification</h2>
        <div className='paragraph'>
            <p>Enter the code sent to your provided <br/> email.If you didn't get the code<br/>please check your spam folder.</p>
        </div>
        <input type="text" name="code" placeholder="Enter OTP Code" />
       
        <button class="log" id="codebtn"><Link to="/reset">Verify</Link></button>

        <br />
        {/* <div className="reset-container">
         <Link to="/login">Back login
          </Link>
        </div> */}
        

      

      </div>
    </div>
    </>
  )
}
