import React from 'react'
import { Helmet } from 'react-helmet';
import { Box, Container, Grid } from '@material-ui/core';
import { Budget, DashboardLayout, LatestOrders, LatestSales, TotalCustomers, TotalProfit, TrafficByDevice } from 'features/adminCommon'

const Dashboard = () => (
    <>
      <DashboardLayout/>
      <Helmet>
        <title>Dashboard | TripN Admin</title>
      </Helmet>
      <Box
        sx={{
          backgroundColor: 'background.default',
          minHeight: '100%',
          py: 3
        }}
      >
        <Container maxWidth={false}>
          <Grid
            container
            spacing={3}
          >
            <Grid
              item
              lg={4}
              sm={8}
              xl={4}
              xs={16}
            >
              <Budget />
            </Grid>
            <Grid
              item
              lg={4}
              sm={8}
              xl={4}
              xs={16}
            >
              <TotalCustomers />
            </Grid>
            <Grid
              item
              lg={4}
              sm={8}
              xl={4}
              xs={16}
            >
              <TotalProfit sx={{ height: '100%' }} />
            </Grid>
            <Grid
              item
              lg={8}
              md={12}
              xl={9}
              xs={12}
            >
              <LatestSales />
            </Grid>
            <Grid
              item
              lg={4}
              md={6}
              xl={3}
              xs={12}
            >
              <TrafficByDevice sx={{ height: '100%' }} />
            </Grid>
            <Grid
              item
              lg={12}
              md={18}
              xl={12}
              xs={24}
            >
              <LatestOrders />
            </Grid>
          </Grid>
        </Container>
      </Box>
    </>
  );
  
  export default Dashboard;