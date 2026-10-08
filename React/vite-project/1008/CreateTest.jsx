import axios from 'axios';
import React, { useState } from 'react'

//Create-Post방식
const CreateTest = () => {

    const [title, setTitle]=useState("");
    const [content,setContent]=useState("");

    const handleSubmit=()=>{
        axios.post("https://jsonplaceholder.typicode.com/posts",{
            //title:title
            title, //입력한 제목
            content, //입력한 내용
            userId:1
        })
        .then(result=>{
            alert('새 글 등록~~');
            console.log(result.data);
        })
        .catch(error=>console.log(error));
    }

  return (
    <div>
      <input value={title} onChange={(e)=>setTitle(e.target.value)} placeholder='제목'></input>
      <br />
      <textarea value={content} onChange={(e)=>setContent(e.target.value)} placeholder='내용'></textarea>
      <br />
      <button onClick={handleSubmit}>등록</button>
    </div>
  )
}

export default CreateTest