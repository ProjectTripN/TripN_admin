import { Header, Navigation } from 'features/common/index'
import styled from 'styled-components'
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { list } from 'features/user/reducer/userSlice'

export default function UserList () {
    const dispatch = useDispatch()

    const users = useSelector(state => state.user.usersState);
    const type = useSelector(state => state.user.type)
    const keyword = useSelector( state => state.user.keyword)
    const page = 1;
    
    useEffect(() => {
      const param = {type: type, keyword: keyword, page: page}
      dispatch(list(param))
    },[]);

    return(<>
    <Header/>
    <Table>
        <Tr>
            <td rowspan="2" style={{width: "15%",border: "1px solid black"}}><Navigation/></td>
            <td colSpan="2" style={{border: '1px solid black'}}>
                <label>이름:<input type="text" title="search"/></label><br/><br/>
                <label>생년월일:<input type="text" title="search" placeholder="No Hyphen"/></label><br/><br/>
                <label>휴대폰번호:<input type="tel" id="phone" pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}" placeholder="No Hyphen"/></label>
                <p><input type="submit" value="search"/></p>
            </td>
        </Tr>
        <Tr>
            <Chartth>회원 기본정보</Chartth>
            <Chartth>회원 상세정보</Chartth>
        </Tr>
    </Table>
    </>)
}

const Table = styled.table`
    width: 98%;
    height:781px;
`

const Tr = styled.tr`
    height:50%;
`

const Chartth = styled.th`
    border: 1px solid black;
`
