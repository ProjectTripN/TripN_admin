import React from 'react'
import styled from 'styled-components'
import { Header, Navigation } from 'features/common/index'

export default function FinancialReports () {
    return(<>
    <Header/>
    <ChartTable>
        <Charttr>
            <td style={{width:'15%', border: "1px solid black"}}><Navigation/></td>
            <Charttd>
            
            </Charttd>
        </Charttr>
    </ChartTable>
    </>)
}

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

