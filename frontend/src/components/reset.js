import React from 'react';

import { Link } from 'react-router-dom';

export const ResetPage = () => {
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
        <h2 classNameName='logintxt'>Reset</h2>
        <div className='paragraph'>
            <p>Create a new password that must contain 
            <br/>8 characters with combination of letters,
            <br/>numbers and special characters(@!#$.)<br/>
            </p>
        </div>
        <input type="password" name="password" placeholder="Enter the new password" />
        <input type="password" name="password" placeholder="Re-enter the new password" />
       
        <button class="log" id="resetbtn"><Link to="/login">Reset</Link></button>

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
