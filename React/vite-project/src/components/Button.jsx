import React from 'react';

const Button = (props) => {    //props 값은 컴포넌트 함수의 파라미터로 받아와 사용 할 수 있다.
    console.log(props);
    return (
        <div>
            <button style={{color:props.color}}>{props.message}</button>
        </div>
    );
};

export default Button;