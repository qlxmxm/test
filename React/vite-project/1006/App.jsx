import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Users, UsersProvider } from './components/Users'
import UsersInfo from './components/UsersInfo'

const App = () => {
  return (
    <div>
      <UsersProvider>
        <BrowserRouter>
          <Routes>
            <Route path='/users' element={<Users />}></Route>
            <Route path='/users/:id' element={<UsersInfo />}></Route>
          </Routes>
        </BrowserRouter>
      </UsersProvider>
      
    </div>
  )
}

export default App