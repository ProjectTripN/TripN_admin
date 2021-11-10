import { Helmet } from 'react-helmet';
import { Box, Container } from '@material-ui/core';
import users from '__mocks__/users';
import {UserList, UserListToolbar} from 'features/adminUser'

export default function CustomerList (){
  return(
    <>
      <Helmet>
        <title>users | TripN</title>
      </Helmet>
      <Box
        sx={{
          backgroundColor: 'background.default',
          minHeight: '100%',
          py: 3
        }}
      >
        <Container maxWidth={false}>
          <UserListToolbar />
          <Box sx={{ pt: 3 }}>
            <UserList users={users} />
          </Box>
        </Container>
      </Box>
    </>
  );
} 

