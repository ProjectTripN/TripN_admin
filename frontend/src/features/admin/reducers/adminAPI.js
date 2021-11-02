import axios from 'axios';

const SERVER = 'http://localhost:8080'
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'JWT fefege..'
}

const adminList = () => axios.get(`${SERVER}/users`)
const adminLogin = x => axios.post(`${SERVER}/users/login`, JSON.stringify(x), { headers })

export default {
  adminList,
  adminLogin
}
