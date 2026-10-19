import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom';

const PostListPage = () => {

  const posts=JSON.parse(localStorage.getItem("posts")) || [
      { id: 1, name: "맛있는 집", location: "서울", rating: 4.5, 
      menu: "김치찌개, 불고기", phone: "010-1111-2222" },
      { id: 2, name: "행복한 밥상", location: "부산", rating: 4.2, 
        menu: "비빔밥, 된장찌개", phone: "010-3333-4444" },
      { id: 3, name: "즐거운 식탁", location: "대구", rating: 4.8, 
        menu: "삼겹살, 냉면",phone: "010-5555-6666" }, ];

     //localStorage에 저장
     localStorage.setItem("posts", JSON.stringify(posts));

  return (
    <div className='max-w-3xl mx-auto mt-10'>
      <div className='flex justify-between mb-4'>
        <h1 className='text-2xl font-bold'>맛집 목록</h1>

        
      </div>
  

      <div className='space-y-3'>
        {posts.length > 0 ? (
          posts.map((post) => (
            <div key={post.id} className='border p-4 rounded shadow flex justify-between'>
              <Link to={`/restaurants/${post.id}`}   className="text-blue-500">
                  {post.name}
              </Link>
            </div>
          ))
        
        ):(
            <div>맛집 없음</div>
        )}
      </div>
    </div>
  )
};

export default PostListPage
