import { Fragment, StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from "./App";
import './index.css'
import { Provider } from 'react-redux';
import store from './redux/store';

//모든 컴포넌트가 store쓸수있게 해줌
createRoot(document.getElementById('root')).render(
<Provider store={store}>
    <App />
</Provider>
)
//앱 전체에서 데이터를 공유해서 사용할 수 있게끔 설정함



//export 할때, default가 아니면 import 할때 {컴포넌트}로 받아와야함
//default 면, import 컴포넌트명 from 