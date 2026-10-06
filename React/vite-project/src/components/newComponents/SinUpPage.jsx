import React from 'react'
import { useNavigate } from 'react-router-dom';

const SignUpPage = () => {

    const [userId, setUserId]=useState("");
    const [password, setPassword]=useState("");

    const navigate=useNavigate();


    const onSubmit1=(e)=>{
      e.preventDefault();

      //ex) const user={userId:"abc", password:"1234"};
      //입력창에 적은 값으로 객체 만듬
      //변수이름과 속성이름이 같아야지 줄일수있음
      const user={userId, password};  // const user2={userId:userId, password:password}; 

      //회원가입한 사람들을 localStorage에서 꺼내온다!!!!
      //이미 가입한 사람이 있으면 회원 배열을 가져오고, 없으면 빈배열을 가져온다!!!!

      // 1번째                           [ ]       
      // 2번째 => 가입한사람했음           [{tom}]              
      // 3번째 => 가입두사람했음           [{tom},{jack}]
      let users=JSON.parse(localStorage.getItem("users")) || [] ;

      users.push(user); //배열에 회원 정보객체를 삽입

      //로컬스토리지에 저장한다.(회원가입한 사람들을)
      //p.558
      localStorage.setItem("users", JSON.stringify(users));

      setUserId("");
      setPassword("");

      //로그인페이지로 강제이동
      navigate("/login");

    }


  return (
    <div className='flex justify-center items-center h-screen bg-gray-100'>
      <form onSubmit={onSubmit1} className='bg-white p-8 rounded shadow w-80'>
        <h1 className='text-xl font-bold mb-4 text-center'>회원가입</h1>

        <input className='border w-full p-2 mb-3 rounded' 
        placeholder='아이디'
        value={userId}
        onChange={(e)=>setUserId(e.target.value)}  />


        <input type="password" className='border w-full p-2 mb-3 rounded' 
        placeholder='비밀번호'
        value={password}
        onChange={(e)=>setPassword(e.target.value)}  />

        <button className='bg-green-500 text-white w-full py-2 rounded'>회원가입</button>

      </form>
      
    </div>
  )
}

export default SignUpPage