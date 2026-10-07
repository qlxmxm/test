import React, { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom';

const EditPostPage = () => {

  // /posts/edit/${post.id}
  // 수정링크 클릭하면 글 id로 게시글 찾아서 폼에 채우고, 수정한 내용 저장할 거임
  const {id}=useParams(); //문자열로 반환됨

  const [post, setPost]=useState({title:"", content:""});

  const navigate=useNavigate();

  useEffect(()=>{

    const posts=JSON.parse(localStorage.getItem("posts")) || [];

    //로컬스토리지에 저장된 글 목록에서 id가 같은 글을 찾는다.
    const currentPost=posts.find((p) => p.id === parseInt(id));

    //찾으면 setPost로 state에 넣어서 입력창에 기존 제목/내용이 채워지게 하려고
    if(currentPost){
      setPost(currentPost);
    }

  },[id]);

  const onSubmit1=(e)=>{
    e.preventDefault();

    const posts=JSON.parse(localStorage.getItem("posts")) || [];

    //수정할 수 있는 글인지 확인-> 수정한 내용으로 교체함 : p
    //수정한 값이 posts안에 있으니까..
    //{id:1, title:"A"}  => {id:1, title:"수정됨" , content:"내용수정", writeId:"aa"}
    const newPosts=posts.map((p)=> p.id === parseInt(id) ? {...post, writeId : p.writeId} : p,
  );

  //수정한 값을 로컬스토리지에 반영(저장)
  localStorage.setItem("posts", JSON.stringify(newPosts));

  navigate("/boardList");

  }

  return (
     <div className='max-w-wl mx-auto mt-10 bg-white p-6 rounded shadow'>
      <h1 className='text-xl font-bold mb-4'>게시글 수정</h1>

      <form onSubmit={onSubmit1}>
        <input className='border w-full p-2 mb-3 rounded'
        value={post.title}
        onChange={(e)=> setPost({...post, title:e.target.value})} />


      <textarea className='border w-full p-2 mb-3 rounded h-40'
        value={post.content} onChange={(e)=>setPost({...post, content:e.target.value})} />
      
      <button className='bg-green-500 text-white px-4 py-2 rounded'>수정</button>

      </form>
      
    </div>
  )
}

export default EditPostPage
