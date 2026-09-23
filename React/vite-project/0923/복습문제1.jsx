// 1. useState를 사용해서 버튼을 누르면 숫자가 1씩 증가하는 컴포넌트를 만든다
// 숫자 상태를 useState로 저장
// 버튼을 누르면 숫자 +1

import React, { useState } from 'react'

export const App = () => {

  const [num, setNum] = useState(0); //0이 num에 대입됨

  const onClickButton = () =>{
    setNum(num+1);
  }

  return (  //jsx문법에 js값 출력 {}
    <div>
        <button onClick={onClickButton}>버튼</button>
        <h2>{num}</h2>
    </div>
  )
}

export default App




