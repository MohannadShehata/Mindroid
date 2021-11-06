import React, {useState} from 'react';
import './Navbar.css';
function Navbar() {
    return (
        <>
            <nav className="navbar">
                <div className="navbar-container">
                    <img src="/img/MINDROID1.png" alt="MINDROID" className="logo-desktop"/>
                    <img src="/img/MINDROID3.png" alt="MINDROID" className="logo-mobile"/>
                    <h2 className="name">MINDROID</h2>
                </div>
            </nav>      
        </>
    )
}

export default Navbar
