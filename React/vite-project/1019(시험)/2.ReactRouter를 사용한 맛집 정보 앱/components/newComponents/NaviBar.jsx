import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

const NaviBar = () => {

  //AuthContextPro 에 적은 currentUser, logout 가져오기
  const navigate=useNavigate(); //페이지 이동시키는 훅

  //<Link to ..>: 클릭해서 이동
  //navigate :  직접이동(강제이동)






  return (
    <nav className="bg-orange-200 shadow-md">
      <div className='max-w-5xl mx-auto flex justify-between items-center p-4'>
        <div className='flex gap-6 font-semibold'>
          <Link to="/">홈</Link>
          <Link to="/restaurants">맛집 목록</Link>
        </div>




      </div>
    </nav>
   
  )
}

export default NaviBar
