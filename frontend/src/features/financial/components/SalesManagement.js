import React from 'react'
import { Navigation, AppAppBar } from 'features/adminCommon'
import { Chart1, Chart2, Chart3, Chart4, ChartData, ChartData2, ChartData3, ChartData4 } from 'features/financial'
import { Box, Container, Grid } from '@material-ui/core';

export default function SalesManagement () {
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
                            <Chart2 />
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart3 />
                        </Grid>
                        <Grid
                            item
                            lg={4}
                            md={6}
                            xl={3}
                            xs={12}
                        >
                            <Chart4 />
                        </Grid>
                    </Grid>
                </Container>
            </div>
        </Box>
    </>)
}
