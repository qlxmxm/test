//1초마다 움직이는 시계

function updateClock(){
    let now=new Date();

    //시분초 알아내기
    let hours=now.getHours();
    let min=now.getMinutes();
    let sec=now.getSeconds();

    if(hours<10){
        hours='0'+hours;        
    }
    if(min<10){
        min='0'+min;
    }
    if(sec<10){
        sec='0'+sec;
    }
    //div태그객체 사이에 텍스트 띄운다 시:분:초
    document.getElementById("clock").textContent=`${hours}:${min}:${sec}`;
}

//1초마다 updateClock함수 실행해줘
setInterval(updateClock, 1000);