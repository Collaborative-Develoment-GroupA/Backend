import React from 'react'
import Navbar from './Navbar';
export const Tickets = () => {
  return (
    <>
    <Navbar/>
    <div className= 'voilation-para'>
    <h2 className='text'>ADD OR REMOVE TICKET DETAILS </h2>
    </div>
      

      <div className='violationdiv'>

        <form className='violation'>
          <div className="addform-section">
            
            <div className="addform-sectionticketinfo">

              
              <select id="type" name="type">
                <option value="Speeding Ticket">Speeding Ticket</option>
                <option value="Red Light Violation">Red Light Violation</option>
                <option value="Parking Violation">Parking Violation</option>
              </select>
              

              <input type="text" id="ticketvehicleNumber" name="ticketvehicleNumber" placeholder="Vehicle Number" required />

              <input type="text" id="ticketName" name="ticketName" placeholder="Name " required />
              <input type="text" id="ticketEmail" name="ticketEmail" placeholder="Email" required />

              <input type="text" id="ticketPhone" name="ticketPhone" placeholder='Contact Number' pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required />
              <input type="text" id="ticketAddress" name="ticketAddress" placeholder="Address" required></input>
            </div>
          </div>
          <div className="form-section">


            <div className="addform-sectionticketlocation">
              

              <input type="text" id="city" placeholder="City" name="city" required />


              <input type="text" id="district" name="district" placeholder="District" required />
              <input type="date" id="date" name="date" placeholder="Date" required />
              <label htmlFor="vehicle">Time:</label>
              <input type="time" id="time" name="time" placeholder="Time" required />
            </div>
          </div>





          <div className='addsavebtn'>

            <button className="savebutton">SAVE</button>
            <br />
            <button className="removebutton">REMOVE</button>
          </div>
        </form>
        <div className='ticket-table'>
          <table>
            <thead>
              <tr>
                <th>Ticket Type</th>
                <th>Vehicle Number</th>
                <th>Name</th>
                <th>Email</th>
                <th>Contact Number</th>
                <th>Address</th>
                <th>City</th>
                <th>District</th>
                <th>Date</th>
                <th>Time</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Speeding Ticket</td>
                <td>ABC-123</td>
                <td>John Doe</td>
                <td>johndoe@example.com</td>
                <td>123-456-7890</td>
                <td>123 Main St</td>
                <td>Los Angeles</td>
                <td>CA</td>
                <td>2023-03-23</td>
                <td>09:00 AM</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

