import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components';

const Navigation = () => (
    <>
    <Nav>
        <NavList>
            <NavItem><Link to = '/admin-page'>AdminPage</Link></NavItem>
            <NavItem><Link to = '/dash-board'>DashBoard</Link></NavItem>
            <NavItem><Link to = '/user-list'>UserList</Link></NavItem>
            <NavItem><Link to = '/sales-management'>SalesManagement</Link></NavItem>
            <NavItem><Link to = '/financial-reports'>FinancialReports</Link></NavItem>
        </NavList>
    </Nav>
    </>
)

export default Navigation;

const Nav = styled.div`
    text-align: center;
`

const NavList = styled.ul`
    width: 100%;
    text-align: center;
`

const NavItem = styled.li`
    line-height:60px;
    display: flex;

`