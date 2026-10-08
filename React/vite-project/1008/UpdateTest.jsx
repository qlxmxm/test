import axios from 'axios'
import React from 'react'

const UpdateTest = () => {
    const updatePost=()=>{

        axios.put("https://jsonplaceholder.typicode.com/posts/1",{
            title:"Updated Title",
            body:"Updated Content",
        })
        //요청이 성공하면
        .then((response)=>{
            console.log(response.data);
        })
    }
  return (
    <div>
      <button onClick={updatePost}>수정</button>
    </div>
  )
}

export default UpdateTest