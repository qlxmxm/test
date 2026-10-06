import React, { useState } from 'react'

//custom hook(사용자 정의 훅)
const useInput = (initvalue) => {

  const [value, setValue]=useState(initvalue);

  const onChange=(e)=>{
    setValue(e.target.value);
  }

  return {
    value,onChange
  }
}

export default useInput
