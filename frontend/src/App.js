import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom';
import { AdminLogin } from 'features/admin';
import { DashBoard } from 'features/common';
import { UserList } from 'features/user';
import { SalesManagement, FinancialReports } from 'features/financial';
import { BrowserRouter as Router } from 'react-router-dom'


const App = () => {
  return (<>
  <div className="App">
    <Router>
      <Switch>
        <Route exact path='/' component={AdminLogin} />
        <Redirect from='/admin-home' to={'/'} />
        <Route exact path='/dash-board' component={DashBoard} />
        <Route exact path='/user-list' component={UserList} />
        <Route exact path='/sales-management' component={SalesManagement} />
        <Route exact path='/financial-reports' component={FinancialReports} />
      </Switch>
    </Router>
  </div>
</>)
}

export default App;
