import React from 'react'
import Navbar from './Navbar'

export const Accidents = () => {
    const [city, setCity] = useState('');
    const [district, setDistrict] = useState('');
    const [date, setDate] = useState('');
    const [officer_id, setOfficerId] = useState('');
    const [department, setDepartment] = useState('');
    const [post, setPost] = useState('');
  
    const [officer, setOfficer] = useState({})
  
    const add = async (e) => {
      e.preventDefault();
      console.log(firstname, lastname, citizenship, officer_id, department, post)
      try {
        const response = await fetch("http://localhost:8000/officer/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ firstname, lastname, citizenship, officer_id, department, post }),
        });
        const data = await response.json();
        if (data['success'] === true) {
          return window.location.href = "/officer";
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
        <Navbar/>
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
                                <th>Fault Driver Vehicle Number</th>
                                <th>Fault Driver Name</th>
                                <th>Fault Driver Email</th>
                                <th>Fault Driver Phone</th>
                                <th>Fault Driver Address</th>
                                <th>Victim Vehicle Number</th>
                                <th>Victim Name</th>
                                <th>Victim Email</th>
                                <th>Victim Phone</th>
                                <th>Victim Address</th>
                                <th>Injuries</th>
                                <th>Description</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>New York</td>
                                <td>Manhattan</td>
                                <td>2023-03-23</td>
                                <td>13:45</td>
                                <td>AB1234</td>
                                <td>John Doe</td>
                                <td>johndoe@gmail.com</td>
                                <td>555-123-4567</td>
                                <td>123 Main St</td>
                                <td>CD5678</td>
                                <td>Jane Smith</td>
                                <td>janesmith@gmail.com</td>
                                <td>555-987-6543</td>
                                <td>456 Oak Ave</td>
                                <td>2</td>
                                <td>Car accident on 5th street</td>
                                <td>
                                    <button>Edit</button>
                                    <button>Delete</button>
                                </td>
                            </tr>
                            <tr>
                                <td>Los Angeles</td>
                                <td>Hollywood</td>
                                <td>2023-03-22</td>
                                <td>19:30</td>
                                <td>EF5678</td>
                                <td>Tom Smith</td>
                                <td>tomsmith@gmail.com</td>
                                <td>555-456-7890</td>
                                <td>789 Vine St</td>
                                <td>GH9012</td>
                                <td>Mary Brown</td>
                                <td>marybrown@gmail.com</td>
                                <td>555-234-5678</td>
                                <td>321 Sunset Blvd</td>
                                <td>3</td>
                                <td>Truck collision on the highway</td>
                                <td>
                                    <button>Edit</button>
                                    <button>Delete</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </>

    )
}
