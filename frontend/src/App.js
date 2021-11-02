import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom';
import { AdminLogin } from 'features/admin';
import { DashBoard } from 'features/common';
import { UserList } from 'features/user';
import { SalesManagement } from 'features/financial';
import { FinancialReports } from 'features/financial';


const App = () => (
  <>
    <Switch>
      <Route exact path='/' component={AdminLogin} />
      <Redirect from='/admin-home' to={'/'} />
      <Route exact path='/dash-board' component={DashBoard} />
      <Route exact path='/user-list' component={UserList} />
      <Route exact path='/sales-management' component={SalesManagement} />
      <Route exact path='/financial-reports' component={FinancialReports} />
    </Switch>
  </>
)

export default App;
