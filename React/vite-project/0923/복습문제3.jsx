// 다음 코드를 보고 필요한 부분을 구현해라.
// name2에는 msg가 다 출력된다.
// input창에는 입력한 값이 출력된다.
import { useState } from "react";

const Sub = () => {

    const [name, setName]=useState([
        {id:1, msg:'tom'},
        {id:2, msg:'juli'},
        {id:3, msg:'jack'},
    ])

    const [inText, setInText] = useState("")

    const on=(e)=>{
      //inText가 원래는 공백인데, input 창에 값을 쓸떄마다 상태변경해서
      //inText에 저장하고픔
      setInText(e.target.value)
    }

    //inText -> 공백으로 초기화
    //on함수
    //map으로 msg출력

  return (
   <>
   <input onChange={on} value={inText} />
   <ul>
        {name.map((i)=>{
          return<li key={i.id}>{i.msg}</li>
        })}
   </ul>
    {inText}
   </>
  )
};

export default Sub;

