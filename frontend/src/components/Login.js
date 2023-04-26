import React,{useState} from 'react';

import { Link } from 'react-router-dom';

export const Login = () => {
  const[email,setEmail]=useState('');
  const[password,setPassword]=useState('');

  const login=async(e)=>{
    e.preventDefault();
    console.log(email,password)
    try {
      const response = await fetch("http://localhost:8000/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({email, password}),
      });
      const data = await response.json();
      if(data['success']===true){
         return window.location.href = "/home";
      }
      else{
          alert("Invalid Credentials");
      }

    } catch (error) {
      console.log(error);
      // Handle the error
    }
  }

  function ForgetPasswordForm() {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');
  
    function handleSubmit(event) {
      event.preventDefault();
      fetch('http://127.0.0.1:8000/forget_password/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      })
        .then(response => response.json())
        .then(data => setMessage(data.success || data.error));
    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email address:</label>
        <input type="email" id="email" value={email} onChange={event => setEmail(event.target.value)} required />
        <button type="submit">Reset Password</button>
        {message && <p>{message}</p>}
      </form>
    );
  }
  
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
  
          

      <div className="formlog" >
        <h2 classNameName='logintxt'>Log In</h2>
        <input type="email" name="email" placeholder="Enter the email" id='email' value={email} onChange={(e)=>setEmail(e.target.value)}/>
        <input type="password" name="password" placeholder="Enter the password" id='password' value={password} onChange={(e)=>setPassword(e.target.value)}/>
        <button className="log" id="log" onClick={login}>Login</button>

        <br /><br />
       <hr/>
        <div classNameName="forget-container">
              <Link to="/forgetpassword" onClick={ForgetPasswordForm}> Forget Password ?</Link>
        </div>
      </div>
    </div>
    </>
  )
}