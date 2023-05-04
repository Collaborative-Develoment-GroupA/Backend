import React, { useState, useEffect } from 'react'
import Navbar from './Navbar';


export const Officer = () => {
  const [firstname, setFirstName] = useState('');
  const [lastname, setLastName] = useState('');
  const [citizenship, setCitizenship] = useState('');
  const [officer_id, setOfficerId] = useState('');
  const [department, setDepartment] = useState('');
  const [post, setPost] = useState('');

  const [officers, setOfficers] = useState([])

  useEffect(() => {
    const fetchOfficers = async () => {
      try {
        const response = await fetch("http://localhost:8000/officers/");
        const data = await response.json();
        setOfficers(data);
      } catch (error) {
        console.log(error);
        // Handle the error
      }
    };
    fetchOfficers();
  }, []);

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
      <Navbar />
      <div className='officer-heading'>
        <h2 className='text'>ADD OR REMOVE OFFICER DETAILS</h2>
      </div>

      <div className='traffic'>

        <form className='addTraffic'>
          <div className="form-section">

            <div className="form-sectionbasicinfo">

              <input placeholder='First Name' type="text" id="firstname" name="name" required value={firstname} onChange={(e) => setFirstName(e.target.value)} />
              <input placeholder="Last Name" type="text" id="lastname" name="name" required value={lastname} onChange={(e) => setLastName(e.target.value)} />
              <input placeholder="Citizenship Number" type="text" id="citizenship" name="citizenship" required value={citizenship} onChange={(e) => setCitizenship(e.target.value)} />

            </div>
          </div>
          <div className="form-section">
            <div className="form-sectionjobinfo">

              <input type="text" placeholder="ID" id="id" name="id" required value={officer_id} onChange={(e) => setOfficerId(e.target.value)} />
              <input placeholder="Department" type="text" id="department" name="department" required value={department} onChange={(e) => setDepartment(e.target.value)} />
              <input placeholder="Post" type="text" id="post" name="post" required value={post} onChange={(e) => setPost(e.target.value)} />
            </div>
          </div>
          <br />

          <div className='savebtn'>

            <button className="savebutton" onClick={add}>ADD</button>
            <br />
            <button className="removebutton">REMOVE</button>
          </div>

        </form>

        <div className='officer-table '>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>

                <th>Citizenship Number</th>
                <th>Department</th>
                <th>Post</th>
              </tr>
            </thead>
            <tbody>
              {officers.map((officer) => (
                <tr key={officer.name}>
                  <td>{officer.id}</td>
                  <td>{officer.firstname}</td>
                  <td>{officer.lastname}</td>
                  <td>{officer.citizenship}</td>
                  <td>{officer.department}</td>
                  <td>{officer.post}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );

}
export default Officer;