import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import React, { useState, useEffect } from 'react'

export function Navigation() {
    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true)
        }
    }, [isAuth])
    return (
        <div>
            <Navbar bg="dark" variant="dark">
                <Navbar.Brand href="/" className="navbar-brand">Link Holder</Navbar.Brand>
                <Nav className="me-auto">
                </Nav>
                <Nav>
                    {isAuth ?
                        <Nav.Link href="/logout" className="login-logout">Logout</Nav.Link> :
                        <Nav.Link href="/login" className="login-logout">Login</Nav.Link>
                    }
                </Nav>
            </Navbar>
        </div>
    )
}
