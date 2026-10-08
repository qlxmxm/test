import React, { useEffect, useState } from 'react'
import axios from 'axios';

const GetTest = () => {

    const [data, setData]=useState([]);
    const [loading, setLoading]=useState(true);

    useEffect(()=>{
        //axios-get방식으로 요청 후 성공하면(then) setData로 데이터 저장

        //?_limit=5 : 서버에 반환 개수 (최대 5개)
        //서버에서 데이터를 가져옴(조회- Read(get방식))
        axios.get("https://jsonplaceholder.typicode.com/posts?_limit=5")
        .then((response) =>{
            setData(response.data); //서버에서 보낸 실제 데이터
            setLoading(false);
        })
        .catch((error)=>{
            console.log("error");
            setLoading(false);
        })

    },[]);

    if(loading)
        return <p>Loading중...</p>

  return (
    <div>
      <ul>
        {data.map((post)=>(<li key={post.id}>{post.title}</li>))}
      </ul>
    </div>
  )
}

export default GetTest