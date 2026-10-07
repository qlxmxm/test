import { configureStore } from "@reduxjs/toolkit"
import cartReducer from "./cartSlice"

//{cart : {item:[]}}
const store=configureStore({
  reducer:{
    //state이름 : state담당하는 reducer
    cart:cartReducer,
  },
});

export default store

