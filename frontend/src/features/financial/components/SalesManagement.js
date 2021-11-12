import React from 'react'
import { Navigation, AppAppBar } from 'features/adminCommon'
import styled from 'styled-components'
import { Chart1, Chart2, Chart3, Chart4, ChartData, ChartData2, ChartData3, ChartData4 } from 'features/financial'
import { Box, Container, Grid } from '@material-ui/core';

const SalesManagement = () => {
    return (<>
        <AppAppBar />
        <Box
            sx={{
                backgroundColor: 'background.default',
                minHeight: '100%',
                py: 3
            }}
        >
            <div className='container' >
                <Navigation className='navi' />
                <Container maxWidth={false} className='item1' >
                    <Grid
                        container
                        spacing={1}
                    >
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart1 />
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart1 />
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart1 />
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart1 />
                        </Grid>
                    </Grid>
                </Container>
            </div>
        </Box>
    </>)
}

export default SalesManagement

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
    padding:1%;
    margin:auto;
    border: 1px solid black;
`

const Chartdiv = styled.div`
    display:block;
    margin:auto;
    width:500px;
    height:348px;
`