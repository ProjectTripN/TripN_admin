import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { adminAPI } from 'features/admin';

const adminLoginPage = async (x) => {
  const res = await adminAPI.userLogin(x) 
  return res.data
}

export const loginPage = createAsyncThunk('admin/login', adminLoginPage)

const changeNull = ls =>{
  for(const i of ls ){
    document.getElementById(i).value = ''
  }
}
const userSlice = createSlice({
  name: 'admin',
  initialState: {
    userState: {
      username:'', password:'', email:'', name:'', regDate: ''
    },
    type: '',
    keyword: '',
    params: {}
  },
  reducers: {},
  extraReducers: {
    [loginPage.fulfilled]: ( state, {meta, payload} ) => {
      state.userState = payload
      window.localStorage.setItem('sessionUser', JSON.stringify(payload))
      if(payload.username != null){
        alert(`${payload.name}님 환영합니다`)
        window.location.href = `/common/dashboard`
      }else{
        alert('아이디, 비번 오류로 로그인 실패  ')
        changeNull(['username','password'])
      }
    }
  }
})
export const currentUserState = state => state.users.userState
export const currentUserParam = state => state.users.param
export default userSlice.reducer;
