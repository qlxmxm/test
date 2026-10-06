import React, { useState } from "react";

const LiveInput = () => {
  // 상태 선언
  //  -> text에 값을 쓸때마다 input이 공백 -> 쓴 값으로 변경하고싶음
  const [input, setInput] = useState('')

  const handleChange = (e) => {
    // 입력값 상태에 저장
    setInput(e.target.value)  //text에 값을 쓸떄마다 input이 공백 -> 쓴 값으로 변경이 됨 -> input에 저장됨
  };

  return (  //jsx 문법
    <div>
      <input type="text" onChange={handleChange} />
      <p>입력한 값: {input}{/* 상태값 출력 */}</p>
    </div>
  );
};

export default LiveInput;