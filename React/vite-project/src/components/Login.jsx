import React from 'react'
import useInput from '../hooks/useInput'

const Login = () => {

  const username=useInput("");  //value:"abc",onChange:
  const password=useInput("");

  return (
    <div>
      {/* username= {value:"abc" onChange : 함수 */}
      <input placeholder='아이디' {...username}></input>
      <input placeholder='비밀번호' {...password}></input>

      <p>아이디: {username.value}</p>
      <p>비밀번호: {password.value}</p>
    </div>
  )
}

export default Login
