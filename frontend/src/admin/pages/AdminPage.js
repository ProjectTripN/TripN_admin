import React from 'react'
import { Navigation } from 'common/index'
import styled from 'styled-components'
import { Header } from 'common/index'

const AdminPage = () => {
    return(<>
    <Header/>
    <ChartTable>
        <Charttr>
            <td style={{width:'15%', border: "1px solid black"}}><Navigation/></td>
            <Charttd>
                <p>ID:<input type="text" title="id"/></p>
                <p>Password:<input type="text" title="password"/></p>
                <p><input type="submit" value="login"/></p>
            </Charttd>
        </Charttr>
    </ChartTable>
    </>)
}

export default AdminPage


const ChartTable = styled.table`
    width: 98%;
    height:700px;
`

const Charttr = styled.tr`
    width:100%;
    height:100%;
    margin:auto;
    border:1px solid black;
`

const Charttd = styled.td`
    padding:2%;
    width:80%;
    height:700px;
    border: 1px solid black;
`