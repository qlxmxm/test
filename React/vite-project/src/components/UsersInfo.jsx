import React, { useContext } from 'react'
import { UsersContext } from './Users'
import { useParams } from 'react-router-dom';

const UsersInfo = () => {

    const users=useContext(UsersContext); //users배열 가져옴
    const userId=parseInt(useParams().id); //:id읽어오기 (동적경로로 준 파라미터 읽어오는 hook) "2"
    const currUser=users.find((user)=>user.id === userId);


  return (
    <div>
        {/*id, name, age, email 출력 */}
        <li>id: {currUser.id}</li>
        <li>name: {currUser.name}</li>
        <li>age: {currUser.age}</li>
        <li>email: {currUser.email}</li>
    </div>
  )
}

export default UsersInfo