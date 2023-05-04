import React from 'react'
import Navbar from './Navbar';
// import LineChart from './Line'
import '../styles/css/home.css';
export const Home = () => {
    return (
        <>
        <Navbar/>
        <div className='dash'>
        <h2>Dashboard</h2>
        </div>
        
        <div className='homebody'>
            <div className="dashboard">
               
                <div className="stats">
    
                    <div className="stat">
                    <h3>Total Violations</h3>
                     <p>532</p>
                    </div>
                    <div className="stat">
                        <h3>Total Violations</h3>
                        <p>234</p>
                    </div>
                    <div className="stat">
                        <h3>Total Accidents</h3>
                        <p>12</p>
                    </div>
                    <div className='graph'>
                        {/* <img src='../../public/assest/images/graphTraffic.png'></img> */}
                    </div>
                    {/* <div className='graph'>
                        <LineChart />
                    </div> */}
                </div>

            </div>
            <div className="news-container">
                <div className="paragraph">
                    <p>News and Notices</p>

                </div>
                <button className="dropdown-btn1">Recent accident in the area</button>
                <div className="accident">
                    <p>This method is often used by journalists to provide facts in their stories and it is
                        <br /> the first step in crafting a product description.</p>
                </div>

            </div>
        </div>


</>

    );
}
