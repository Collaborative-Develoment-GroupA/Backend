import React from 'react'
import { Link } from 'react-router-dom'

export const Register = () => {
  return (
    <div class="contentreg">
      <div className='regtxtcontainer'>

      <h1>
        TRAFFIC <br /><span>MANAGEMENT</span> <br />SYSTEM
      </h1>
      <p class="par">Welcome to the Traffic Management System (TMS). As a traffic officer you play a
        <br /> critical role in ensuring the safety and smooth flow of traffic on our roads.
        <br />We understand that your job can be challenging and stressful at times,
        <br /> which is why we have developed this system to support you in your duties.</p>
      </div>

      <div class="formreg">
        <h2>R E G I S T E R</h2>
        <input type="email" name="email" placeholder="E-mail" />
        <input type="password" name="" placeholder="Password" />
        <input type="confirmpassword" name="" placeholder="Conform Password" />
        <button class="signup"><Link to ="">Register</Link></button>

        <p class="link">Already have an account?<br /><br />


          <Link to="/login"> LOGIN </Link>

        </p>
        <br/>
        <label for="othersign"><p className="othersignoptreg">
          ________________Or sign Up Using_______________
        </p>
        </label>

        <div class="icons">
          <Link to="" ><ion-icon name="logo-facebook"></ion-icon></Link>
          <Link to="/"><ion-icon name="logo-instagram"></ion-icon></Link>
          <Link to=""><ion-icon name="logo-google"></ion-icon></Link>

        </div>


      </div>
    </div>
  )
}
