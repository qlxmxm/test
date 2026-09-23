import React from 'react'

//props: 부모컴포넌트로 부터 전달 받은 객체들
//{color:'pink',msg:"너무 재밌어"}
//{color:'blue',msg:"안녕"}
//{color:'red',children:"오늘은 수요일"}

const ColorPro = (props) => {
    console.log(props);

    const colorStyle={
        color:props.color
    }

  return (
    <div>
      <p style={colorStyle}>{props.msg}</p>
      <p style={{color:props.color}}>{props.childen}</p>
    </div>
  )
}

export default ColorPro
