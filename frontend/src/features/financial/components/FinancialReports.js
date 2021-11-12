import React from 'react'
import styled from 'styled-components'
import { AppAppBar, Navigation } from 'features/adminCommon'
import { Box, Container, Grid } from '@material-ui/core';

const FinancialReports = () => {
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
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                        </Grid>
                    </Grid>
                </Container>
            </div>
        </Box>
    </>)
}

export default FinancialReports

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