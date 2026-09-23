// //useState : 화면에 보여주는 값이 바뀔 때, react가 그걸 알고
// //            자동으로 다시 렌더링 하게 만들기 위해서 쓴다.

// //컴포넌트 : html태그를 반환하는 함수

// import React, { useState } from 'react'

// //함수형 컴포넌트
// export const App = () => {

//   const [num, setNum] = useState(0); //0이 num에 대입됨

//   const [opinion, setOpinion] = useState(false);

//   const onClickButton = () =>{
//     setNum(num+1);
//   }

//   const onOpinion=()=>{
//     setOpinion(!opinion);
//   }

//   //객체타임
//   const con1={
//     color:"red",
//     fontSize:"2em",
//     border:"3px solid red"
//   }

//   return (  //jsx문법에 js값 출력 {}
//     <div>
//         <h1 style={con1}>Hi</h1>
//         <button onClick={onClickButton}>좋아요</button>
//         <h2>👍{num}</h2>{/* 윈도우키 + . */}
//         <button onClick={onOpinion}>찬성/반대</button>
//         <h2>{opinion ? '찬성' : '반대'}</h2>
//     </div>
//   )
// }

// export default App

// //문제 1 
// import React, { useState } from 'react'

// export const App = () => {

//   const [msg, setMsg] = useState(false);

//   const on1=()=>{
//     setMsg('안녕');
//   }

//   const on2=()=>{
//     setMsg('bye');
//   }

//   return (  //jsx
//     <div>
//         <button onClick={on1}>들어온다</button>
//         <button onClick={on2}>나간다</button>
//         {msg}
//     </div>
//   )
// }

// export default App

// import React, { useState } from 'react'

// const App = () => {

//   const [name, setName]=useState(''); //상태변화 감지 훅
//   const [nickname, setNickname]=useState('');

//   //화살표함수(즉식 실행함수)
//   const onChangeName=(e)=>{
//     setName(e.target.value);  //이벤트가 일어난 타켓의 실제데이터 -> text에 입력 한 값 -> name 변수에 저장됨
//   }
  
//   const onChangeNickname=(e)=>{
//     setNickname(e.target.value);
//   }

//   return (
//     <div>
//       <input type='text' onChange={onChangeName} />
//       <input type='text' onChange={onChangeNickname} />
//       이름 : {name}
//       닉네임 : {nickname}
//     </div>
//   )
// }

// export default App

// import React, { useState } from 'react'

// const App = () => {

//   const [msg, setMsg]=useState('');

//   const clickIn=()=>setMsg('안녕'); //안녕으로 state값이 바뀐 후 msg에 저장

//   const clickOut=()=>setMsg('bye');

//   const [color, setColor]=useState('black');

//   return (
//     <div>
//       <button onClick={clickIn}>들어온다</button>
//       <button onClick={clickOut}>나간다</button>
//       <h1>{msg}</h1>
//       <button style={{color:color}} onClick={()=>setColor('red')}>빨강</button>
//       {/*빨강 버튼 클릭하면 black -> red로 변경이 됨
//         상태변화 값 red가 color라는 변수에 저장됨*/}
//     </div>
//   )
// }

// export default App

//문제2
// import React, { useState } from 'react'

// const App = () => {

//   const user={
//     name:"홍길동",
//     isLogin:true,
//   }
//   return (
//     <div>
//       {/*isLogin이 true면 <div>로그인</div> false면 <div>로그아웃</div> 이라고 브라우저 출력*/}
//       {user.isLogin == true ? "로그인" : "로그아웃"}
//     </div>
//   );
// };

// export default App;

// import React, { useState } from 'react'

// const App = () => {

//   const [posts, setPosts]=useState([
//     {id:1, title:"첫번째 제목", content: "첫번째 내용"},
//     {id:2, title:"두번째 제목", content: "두번째 내용"},
//     {id:3, title:"세번째 제목", content: "세번째 내용"}
//   ])

//   //리엑트에서는 이전 렌더링 결과 / 새롭게 렌더링 된 결과값을 비교해서
//   //바뀐부분만 업데이트한다.

//   return (
//     <div>
//       <h1>Board</h1>
//       {posts.map((i) => {
//         return(
//           <div key={i.id}>
//             <h2>{i.title}</h2>
//           </div>
//         )
//       })}
      
//     </div>
//   )
// }

// export default App;

// import React, { useState } from 'react'

// const App = () => {

//   const [name, setName]=useState([
//     {id:1, text:"java"},
//     {id:2, text:"react"},
//     {id:3, text:"deep learning"}
//   ])

//   //화살표 함수의 return생략함
//   // const show=()=>{
//   //   console.log("show");
//   //   return n;
//   // }
//   const show=(n)=>n;

//   //객체배열을 순회하면서 각각 name1에 저장된다. name1에 저장된 객체를 하나하나 꺼내 text를 출력한다 (li형태로)
//   const nameList=name.map((name1 => <li key={name1.id}>{name1.text}</li>))

//   //input 을 공백으로 초기화
//   const [input, setInput]=useState('')

//   //nextId를 숫자 4로 초기화
//   const [nextId, setNextId]=useState(4)

//   //윈래 input 창 비어있다. -> 내가 입력할때마다 입력한 값으로 텍스트 창에 넣음
//   //내가 입련한 값(setInput 메소드로 인해) 이 input에 저장됨
//   const onChange=(e)=>setInput(e.target.value)


//   return (
//     <div>
//       <input onChange={onChange} value={input} />
//       <div>{input}</div>
//       <div>{nextId}</div>

//       <ul>
//         {nameList}
//       </ul>
      
//     </div>
//   )
// }

// export default App;

// import React from 'react'

// const App = () => {

//   const name='리엑트';

//   return (
//     //삼항연산자 ? :
//     //AND 연산자 A&&B
//     //OR 연산자 ||
//     <div>
//       {name === '리엑트' ? (<h1>리엑트이다1</h1>) : (<h1>리엑트아니다</h1>)}

//       {name === '리엑트' && (<h1>리엑트이다2</h1>)}

//       {name === '리엑트' || (<h1>리엑트이다3</h1>)}
//     </div>
//   )
// }

// export default App

import React from 'react'
//자식컴포넌트 import해야 사용가능함
import ColorPro from "./components/ColorPro"

const App = () => {

  const Style1={
    color:'green',
    backgroundColor:'yellow'
  }

  const Style2={
    color:'green',
    backgroundColor:'hotpink',
    fontSize:'3em'
  }

  const onClickBt=()=>alert('버튼')

  return (
    <div>
      <p style={{color:'red', backgroundColor:'black'}}>리엑트1</p>
      <p style={Style1}>리엑트2</p>
      <p style={Style2}>넘나 재밌는것</p>
      <button onClick={onClickBt}>버튼</button>
      {/* "버튼" 이라는 이름의 버튼을 만들어서
        버튼을 클릭하면 alert로 버튼 이라고 출력 */}

      <ColorPro color="pink" msg="너무 재밌어" />
      <ColorPro color="blue" msg="안녕" />
      <ColorPro color="red">오늘은 수요일</ColorPro>

    </div>
  )
}

export default App






