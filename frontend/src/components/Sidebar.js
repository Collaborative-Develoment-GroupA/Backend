
import React from 'react';
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';

export const Sidebar = [
  {
    title: 'Home',
    path: '/home',
    icon: <AiIcons.AiFillHome />,
    cName: 'nav-text'
  },
  {
    title: 'Officer',
    path: '/officer',
    icon: <IoIcons.IoIosPaper />,
    cName: 'nav-text'
  },
  {
    title: 'Department',
    path: '/departments',
    icon: <FaIcons.FaCartPlus />,
    cName: 'nav-text'
  },
  {
    title: 'Ticket',
    path: '/tickets',
    icon: <IoIcons.IoMdPeople />,
    cName: 'nav-text'
  },
  {
    title: 'Accident',
    path: '/accidents',
    icon: <FaIcons.FaEnvelopeOpenText />,
    cName: 'nav-text'
  },
  {
    title: 'Logout',
    path: '/login',
    icon: <FaIcons.FaSignOutAlt />,
    cName: 'logoutbtn'
  }
];// import React from 'react'
// import { Link } from 'react-router-dom'

// export const Sidebar = () => {
//   return (
//     <div className="navbar">
//         <div class="profile">
//           <div class="profile-image">
//             <Link to="">

//               <img src="assest/images/profile.png" alt="Profile Picture" width={150} height={250} />
//             </Link>
//           </div>
//           <h3 class="profile-name">Admin</h3>
//         </div>

//         <div className="menulist">
//           <ul>

//             <li><Link to='/home'>DashBoard</Link></li><br></br>
//             <li><Link to="/officer">Officer</Link></li><br></br>
//             <li><Link to="/departments">Departments</Link></li><br></br>
//             <li><Link to="/tickets">Ticket</Link></li><br></br>
//             <li><Link to="/accidents">Accidents</Link></li><br></br>


//           </ul>

//           <br></br>
//           <div className='logoutbtn'><Link to="/logout">LOG OUT</Link></div>

//         </div>
//         <br />


//       </div>

// )

// }
