// const li = ['리액트', 'DB', '딥러닝']을 ul li 형태로 
// map함수를 사용해 출력한다.
import React, { useState } from 'react'

const App = () => {

  const li = ['리액트', 'DB', '딥러닝'];

  return (
    <div>
      <ul>
        {li.map((i)=>{
          return(
            <li>{i}</li>
          )
        })}
      </ul>
      
    </div>
  )
}

export default App;
