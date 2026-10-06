import React from 'react'
import { useAuth } from '../hooks/useAuth'

const Profile = () => {

    const {user,login,logout}=useAuth();

  return (
    <div>
      {user ? <p>{user.name}님 환영합니다.</p> : <p>로그인해라</p>}
      <button onClick={logout}>로그아웃</button>
    </div>
  )
}

export default Profile
