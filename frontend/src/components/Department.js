import React, {useState} from 'react'
import Navbar from './Navbar';

export const Department = ({  onSelect }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState('');
  const options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'];
  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  const handleSelect = (option) => {
    setSelectedOption(option);
    onSelect(option);
    toggleMenu();
  };
  return (
    <>
    <Navbar/>
    <div className="dropdown">
      <button className="dropdown-toggle" onClick={toggleMenu}>
        {selectedOption ? selectedOption : 'Select an option'}
      </button>
      {isOpen && (
        <ul className="dropdown-menu">
          {options.map((option) => (
            <li key={option} onClick={() => handleSelect(option)}>
              {option}
            </li>
          ))}
        </ul>
      )}
    </div>
    </>
  )
}
