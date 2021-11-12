import { Box, Container } from '@mui/material';
import { UserListResults, UserListToolbar } from 'features/adminUser';
import { customers } from '../__mocks__/customers';

export default function Customers() {
  return (
    <>
        <title>
          Customers | Material Kit
        </title>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8
        }}
      >
        <Container maxWidth={false}>
          <UserListToolbar />
          <Box sx={{ mt: 3 }}>
            <UserListResults customers={customers} />
          </Box>
        </Container>
      </Box>
    </>
  )
}