import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from './components/newComponents/HomePage'
import LoginPage from './components/newComponents/LoginPage'
import SinUpPage from './components/newComponents/SinUpPage'
import MemberListPage from './components/newComponents/MemberListPage'
import PostListPage from './components/newComponents/PostListPage'
import CreatePostPage from './components/newComponents/CreatePostPage'
import EditPostPage from './components/newComponents/EditPostPage'
import NaviBar from './components/newComponents/NaviBar'
import AuthContextPro from './components/newComponents/AuthContextPro'

const App = () => {
  return (
  <AuthContextPro>
    <BrowserRouter>
      <NaviBar />
        <Routes>
          <Route path="/" element={<HomePage />} />

          <Route path="/login" element={<LoginPage />} />

          <Route path="/join" element={<SinUpPage />} />

          <Route path="/memberList" element={<MemberListPage />} />

          <Route path="/boardList" element={<PostListPage />} />

          <Route path="/posts/create" element={<CreatePostPage />} />

          <Route path="/posts/edit/:id" element={<EditPostPage />} />

        </Routes>
      
    </BrowserRouter>
  </AuthContextPro>
  )
}

export default App
