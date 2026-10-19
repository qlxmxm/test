import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from './components/newComponents/HomePage'
import PostListPage from './components/newComponents/PostListPage'
import EditPostPage from './components/newComponents/EditPostPage'
import NaviBar from './components/newComponents/NaviBar'

const App = () => {
  return (
    <BrowserRouter>
      <NaviBar />
        <Routes>
          <Route path="/" element={<HomePage />} />

          <Route path="/restaurants" element={<PostListPage />} />

          <Route path="/restaurants/:id" element={<EditPostPage />} />

        </Routes>
      
    </BrowserRouter>
  )
}

export default App
