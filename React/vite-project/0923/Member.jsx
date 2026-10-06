import React, { useState } from 'react'

const App = () => {

  const [user, setUser]=useState([
    {id:1, username:'user1', email:'u1@naver.com'},
    {id:2, username:'user2', email:'u2@naver.com'},
    {id:3, username:'user3', email:'u3@naver.com'},
  ]);

  const [pickUser, setPickUser]=useState(null);

  //회원 클릭하면 상태 변경됨
  const clickUser=(user)=>{
    setPickUser(user); //클릭한 값(객체)이 pickUser 에 저장됨
  }

  return (
    <div>
      <h1>Member</h1>
      <h1>회원목록</h1>
      {user.map((i)=>{
        return(
          <div key={i.id} onClick={()=>clickUser(i)}>
            <h1>{i.username}</h1>
          </div>
        )
      })}

      {pickUser && (
        <div>
          <h2>{pickUser.username}</h2>
          <h2>{pickUser.email}</h2>
        </div>
      )}
    </div>
  )
}

export default App
