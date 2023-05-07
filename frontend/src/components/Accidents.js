import React from 'react'
import Navbar from './Navbar'
import { useEffect, useState } from 'react';


export const Accidents = () => {
    const [city, setCity] = useState('');
    const [district, setDistrict] = useState('');
    const [date, setDate] = useState('');
    const [time, setTiime] = useState('');
    const [fault_vehicle_number, setFault_Driver_Vehicle_Number] = useState('');
    const [fault_driver_name, setFault_Driver_Name] = useState('');
    const [fault_driver_email, setFault_Driver_Email] = useState('');
    const [fault_driver_phone, setFault_Driver_Phone] = useState('');
    const [fault_driver_address, setFault_Driver_Address] = useState('');
    const [victim_vehicle_number, setVictim_Vehicle_Number] = useState('');
    const [victim_name, setVictim_Name] = useState('');
    const [victim_email, setVictim_Email] = useState('');
    const [victim_phone, setVictim_Phone] = useState('');
    const [victim_address, setVictimr_Address] = useState('');


    const [officer, setOfficer] = useState({})
    const [accidentdata, accidentdatachange] = useState(null);

    useEffect(() => {
        fetch("https://simonpradhan.pythonanywhere.com/accidents/").then((res) => {
            return res.json();
        }).then((resp) => {
            accidentdatachange(resp);
            console.log(resp);
        }).catch((err) => {
            console.log(err.message);
        })
    }, [])

    const add = async (e) => {
        e.preventDefault();
        console.log(city, district, date, time, fault_vehicle_number, fault_driver_name, fault_driver_email, fault_driver_phone, fault_driver_address, victim_vehicle_number, victim_name, victim_email, victim_phone, victim_address)

        try {
            const response = await fetch("https://simonpradhan.pythonanywhere.com/accident", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ city, district, date, time, fault_vehicle_number, fault_driver_name, fault_driver_email, fault_driver_phone, fault_driver_address, victim_vehicle_number, victim_name, victim_email, victim_phone, victim_address }),
            });
            const data = await response.json();
            if (data['success'] === true) {
                return window.location.href = "/accidents";
            }
            else {
                alert("Invalid Credentials");
            }

        } catch (error) {
            console.log(error);
            // Handle the error
        }
    }
    return (
        <>
            <Navbar />
            <div className='officer-heading'>
                <h2 className='text'>ADD OR REMOVE ACCIDENT DETAILS </h2>
            </div>
            <div className='accidentbody'>

                <form className='accidentform'>
                    <div className="form-section">
                        <div className="form-sectionlocation">


                            <input type="text" id="city" placeholder="City" name="city" required />
                            <input type="text" id="district" name="district" placeholder="District" required />
                            <input type="date" id="date" name="date" placeholder="Date" required />
                            <label className='violationlabel' htmlFor="vehicle">Time:</label>
                            <input type="time" id="time" name="time" placeholder="Time" required />
                        </div>

                    </div>
                    <div className='accidentuser'>




                        <div className="form-sectionfalut">
                            <div className='falutdriverheading'>

                                <h3 className='accidenth3'>AT-FALUT DRIVER DETAILS</h3>
                                <br />
                            </div>
                            <div className='falutdriverinputcontainer'>

                                <input type="text" id="falutvehicleNumber" name="falutvehicleNumber" placeholder="Vehicle Number" required />

                                <input type="text" id="falutName" name="falutName" placeholder="Name " required />
                                <input type="email" id="falutEmail" name="falutEmail" placeholder="Email" required />

                                <input type="tel" id="falutPhone" name="falutPhone" placeholder='Contact Number' pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required />
                                <input type="text" id="falutAddress" name="falutAddress" placeholder="Address" required></input>
                            </div>
                        </div>


                        <div className="form-sectionvictim">
                            <div className='victimheading'>
                                <h3 className='accidenth3' >VICTIM DETAILS</h3>
                            </div>
                            <br />
                            <div className='victiminputcontainer'>

                                <input type="text" id="victimvehicleNumber" name="victimvehicleNumber" placeholder="Vehicle Number" required />

                                <input type="text" id="victimName" name="victimName" placeholder="Name " required />
                                <input type="email" id="victimEmail" name="victimEmail" placeholder="Email" required />

                                <input type="tel" id="victimPhone" name="victimPhone" placeholder='Contact Number' pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required />
                                <input type="text" id="victimAddress" name="victimAddress" placeholder="Address" required></input>
                            </div>


                        </div>

                    </div>
                    <div className="form-section">
                        <input type="number" id="injuries" name="injuries" placeholder='Number of Injuries' required />

                    </div>
                    <div className="form-section">
                        <textarea id="description" name="description" rows="5" placeholder="Description" required></textarea>
                    </div>

                    <div className='savebtn'>
                        <button className="savebutton">ADD</button>
                        <br />
                        <button className="removebutton">REMOVE</button>

                    </div>

                </form>


                <div className='accident-table'>

                    <table>
                        <thead>
                            <tr>
                                <th>City</th>
                                <th>District</th>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Fault_Driver_Vehicle_Number</th>
                                <th>Fault_Driver_Name</th>
                                <th>Fault_Driver_Email</th>
                                <th>Fault_Driver_Phone</th>
                                <th>Fault_Driver_Address</th>
                                <th>Victim_Vehicle_Number</th>
                                <th>Victim_Name</th>
                                <th>Victim_Email</th>
                                <th>Victim_Phone</th>
                                <th>Victim_Address</th>
                                <th>Injuries</th>
                                <th>Description</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {accidentdata &&
                                accidentdata.map(item => (
                                    <tr key={item.id}>
                                        <td>{item.id}</td>
                                        <td>{item.city}</td>
                                        <td>{item.district}</td>
                                        <td>{item.date}</td>
                                        <td>{item.time}</td>
                                        <td>{item.fault_vehicle_number}</td>
                                        <td>{item.fault_driver_name}</td>
                                        <td>{item.fault_driver_email}</td>
                                        <td>{item.fault_driver_phone}</td>
                                        <td>{item.fault_driver_address}</td>
                                        <td>{item.fault_driver_number}</td>
                                        <td>{item.victim_name}</td>
                                        <td>{item.victim_email}</td>
                                        <td>{item.victim_phone}</td>

                                        <td>{item.injuries}</td>
                                        <td>{item.descriptions}</td>



                                        <td><a className="btn btn-success">Add</a>
                                            <a className="btn btn-danger">Remove</a>

                                        </td>
                                    </tr>
                                ))
                            }

                        </tbody>
                    </table>
                </div>
            </div>
        </>

    )
}