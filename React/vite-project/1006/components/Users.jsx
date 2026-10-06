import React, { createContext, useContext } from 'react'
import { Link } from 'react-router-dom';

export const UsersContext=createContext();

export const UsersProvider=({children})=>{
    const users=[
        {id:1, name:'Alice',age:25, email:'alice@naver.com'},
        {id:2, name:'Bob',age:35, email:'bob@naver.com'},
        {id:3, name:'Juli',age:45, email:'juli@naver.com'},
    ];

    return(
        <UsersContext.Provider value={users}>
            {children} {/* App - > Users, UsersInfo 에서 value값을 가져다 쓸수있다 */}
        </UsersContext.Provider>
    )
}

export const Users = () => {

    const users=useContext(UsersContext);


  return (
    <div>
        {users.map((user)=>(<li key={user.id}>
            {/*Link to="/users/1" */}
            <Link to={`/users/${user.id}`}>{user.name}</Link> 
        </li>))}
    </div>
  )
}