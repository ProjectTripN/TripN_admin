import React from 'react';
import { useDispatch } from 'react-redux';
import * as Yup from 'yup';
import { Formik } from 'formik';
import { useForm } from "react-hook-form";
import { Link as useNavigate } from 'react-router-dom';
import { Box, Button, Container, Grid, TextField, Typography } from '@material-ui/core';
import { Navigation } from 'features/common';
import { loginPage } from '../reducers/adminSlice';

export default function AdminLogin() {
  // const navigate = useNavigate()
  const dispatch = useDispatch()
  const { handleSubmit, formState: { errors } } = useForm();

  return (<>
      <title>Login | Admin Page</title>
    <Box
      sx={{
        backgroundColor: 'background.default',
        display: 'flex',
        flexDirection: 'column',
        height: 'center',
        justifyContent: 'center'
      }}>
      <Container maxWidth="sm">
        <Formik
          initialValues={{
            email: 'demo@devias.io',
            password: 'Password123'
          }}
          validationSchema={Yup.object().shape({
            email: Yup.string().email('Must be a valid email').max(50).required('Email is required'),
            password: Yup.string().max(15).required('Password is required')
          })}
          onSubmit={() => {
            Navigation('/', { replace: true });
          }}>
          {({
            errors,
            handleBlur,
            handleChange,
            handleSubmit,
            isSubmitting,
            touched,
            values
          }) => (
            <form method='POST'
              onSubmit={handleSubmit(async (data) => {await dispatch(loginPage(data))})}>
              <Box sx={{ mb: 3 }}>
                <Typography
                  color="textPrimary"
                  variant="h3"
                  align="center">
                  Admin Page
                </Typography>
              </Box>
              <Box
                sx={{
                  pb: 1,
                  pt: 3
                }}>
                <Typography
                  align="center"
                  color="textSecondary"
                  variant="body1">
                  Sign in with email address
                </Typography>
              </Box>
              <Grid
                container
                spacing={3}
              >
                <Grid
                  item
                  xs={12}
                  md={6}
                >
                </Grid>
                <Grid
                  item
                  xs={12}
                  md={6}
                >
                </Grid>
              </Grid>
              <TextField
                error={Boolean(touched.email && errors.email)}
                fullWidth
                helperText={touched.email && errors.email}
                label="Email Address"
                margin="normal"
                name="email"
                onBlur={handleBlur}
                onChange={handleChange}
                type="email"
                value={values.email}
                variant="outlined" />
              <TextField
                error={Boolean(touched.password && errors.password)}
                fullWidth
                helperText={touched.password && errors.password}
                label="Password"
                margin="normal"
                name="password"
                onBlur={handleBlur}
                onChange={handleChange}
                type="password"
                value={values.password}
                variant="outlined" />
              <Box sx={{ py: 2 }}>
                <Button
                  color="primary"
                  disabled={isSubmitting}
                  fullWidth
                  size="large"
                  type="submit"
                  variant="contained">
                  Sign in
                </Button>
              </Box>
            </form>
          )}
        </Formik>
      </Container>
    </Box>
  </>);
};
