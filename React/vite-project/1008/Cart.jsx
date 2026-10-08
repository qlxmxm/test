import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { addItem, removeItem, clearItem } from '../redux/cartSlice';

const Cart = () => {

    //items=[]
    //store에 보관된 state에서 필요한 값을 읽어오는 hook
    const items=useSelector((state)=>state.cart.items);

    //redux store에 "이런일해줘~" 요청(액션) 보낼 수 있는 함수꺼내주는 hook
    const dispatch=useDispatch();


  return (
    <div>
        <button onClick={()=>dispatch(addItem({id:1, name:"딸기"}))}>딸기 추가</button><br></br>
        <button onClick={()=>dispatch(addItem({id:2, name:"새우"}))}>새우 추가</button><br></br>
        <button onClick={()=>dispatch(addItem({id:3, name:"꽃게"}))}>꽃게 추가</button><br></br>

        <button onClick={()=>dispatch(clearItem())}>장바구니 비우기</button>

        <ul>
          {items.map((item)=>(
            <li key={item.id}>
              {item.name}
              <button onClick={()=> dispatch(removeItem(item.id))} 
              style={{marginLeft:"10px"}}>삭제</button>
            </li>
          ))}


        </ul>
    </div>
  )
}

export default Cart