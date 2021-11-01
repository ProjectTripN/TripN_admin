import React from 'react';
import styled from 'styled-components'
import { Link } from 'react-router-dom'


const Header = () => {
    return(<>
    <SideBar><Button>Login</Button></SideBar>
    <Logo><Link to='/admin-page' style={{ textDecoration: 'none', color: 'black' }}>Trip N</Link></Logo>
    </>)
}

export default Header;

const Logo = styled.h1`
    height: auto;
    width: auto;
    font-size: 80px;
    text-align: center;
    //float: left;
    font-size: 100px;
    margin: 60px 100px 10px;
    `
const SideBar = styled.div`
    display : flex;
    width: auto;
    float: right;
    margin: 40px;
    `
const Button = styled.button`
    width:70px;
    border: none;
    background-color: white;
    color: black;
    padding: 5px 0;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    margin: 4px;
    cursor: pointer;
    box-shadow:1px 1px 1px gray;
    `