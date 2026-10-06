import React, { useState } from 'react'

const App = () => {

  const [num, setNum]=useState(0);

  //()=>ch1(10) 이거 혹은

  // function(){
  //   return ch1(10);
  // } 이거 사용(같음)

  const ch1=(n)=>{
    setNum(num+n);
  }

  return (
    <div>
      {num}
      <button onClick={()=>ch1(10)}>+10</button>
      <button onClick={()=>ch1(-5)}>-5</button>
    </div>
  )
}

export default App
