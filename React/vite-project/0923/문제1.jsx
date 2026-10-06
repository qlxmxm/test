//문제 1 
import React, { useState } from 'react'

export const App = () => {

  const [msg, setMsg] = useState(false);

  const on1=()=>{
    setMsg('안녕');
  }

  const on2=()=>{
    setMsg('bye');
  }

  return (  //jsx
    <div>
        <button onClick={on1}>들어온다</button>
        <button onClick={on2}>나간다</button>
        {msg}
    </div>
  )
}

export default App












