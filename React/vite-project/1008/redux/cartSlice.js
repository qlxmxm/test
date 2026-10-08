import { configureStore } from "@reduxjs/toolkit";
import cartReducer from "./cartSlice";


//store.js: reducer를 등록해서 상태 보관소를 만드는 파일
//store안에 state = {cart :{items:[]}}
//state값은 configureStore가 실행될 때 store내부에 보관하는 값
const store=configureStore({
    reducer:{
        cart:cartReducer,
    },
});

console.log(store.getState());


export default store;

//cartSlice.js에서 export내면 store.js에서 등록한 후 store만듬 -> 다른컴포넌트에서 store의 값을 읽고ㅡ 요청을 보낼수있음