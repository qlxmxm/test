import React from 'react'
import { useDispatch } from 'react-redux'

const Cart = () => {

  //redux store에 "이런일해줘~" 요청(액션) 보낼 수 있는 함수꺼내주는 hook
  const dispatch=useDispatch();

  return (
    <div>
       <button onClick={()=>dispatch(addItem({id:1, name:딸기}))}>딸기추가</button><br></br>
    </div>
  )
}

export default Cart
