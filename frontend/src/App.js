import React from 'react'
import { Route, Routes } from 'react-router-dom';
import { DashBoard } from 'features/common';
import { UserList } from 'features/user';
import { SalesManagement, FinancialReports } from 'features/financial';
import { AdminLogin } from 'features/admin';

const App = () => {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<AdminLogin />} />
        <Route path='/an/admin-login' element={<AdminLogin />} />
        <Route path='/an/dash-board' element={<DashBoard />} />
        <Route path='/an/user-list' element={<UserList />} />
        <Route path='/an/sales-management' element={<SalesManagement />} />
        <Route path='/an/financial-reports' element={<FinancialReports />} />
      </Routes>
    </div>
  );
}

export default App;
