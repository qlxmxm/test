// //useState : 화면에 보여주는 값이 바뀔 때, react가 그걸 알고
// //            자동으로 다시 렌더링 하게 만들기 위해서 쓴다.

// //컴포넌트 : html태그를 반환하는 함수

import React, { useState } from 'react'

//함수형 컴포넌트
export const App = () => {

  const [num, setNum] = useState(0); //0이 num에 대입됨

  const [opinion, setOpinion] = useState(false);

  const onClickButton = () =>{
    setNum(num+1);
  }

  const onOpinion=()=>{
    setOpinion(!opinion);
  }

  //객체타임
  const con1={
    color:"red",
    fontSize:"2em",
    border:"3px solid red"
  }

  return (  //jsx문법에 js값 출력 {}
    <div>
        <h1 style={con1}>Hi</h1>
        <button onClick={onClickButton}>좋아요</button>
        <h2>👍{num}</h2>{/* 윈도우키 + . */}
        <button onClick={onOpinion}>찬성/반대</button>
        <h2>{opinion ? '찬성' : '반대'}</h2>
    </div>
  )
}

export default App










