// import React, { useState } from 'react'

// //rfc
// //rfce
// //rafce -> 기억하기!!!!

// //useState : 화면에 보여주는 값이 바뀔 때, react가 그걸 알고
// //            자동으로 다시 렌더링 하게 만들기 위해서 쓴다.

// //컴포넌트 : html태그를 반환하는 함수



// export default function App(){

//   return (
//     <div>
//       <h1>header</h1>
      
//     </div>
//   )
// }

//11
// import React from 'react'
// import Header from './Hearder'

// function App() {
//   return (
//     <>
//       <Header />
//       <h1>리엑트</h1>
//     </>
//   )
// }

// export default App

import React, { useState } from 'react'

export const App = () => {

  const [num, setNum] = useState(0); //0이 num에 대입됨

  return (
    <>
        <h2>{num}</h2>
    </>
  )
}

export default App
