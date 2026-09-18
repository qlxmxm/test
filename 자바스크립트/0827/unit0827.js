let n=2;
        while(true){
            if(n%2==0){
                for(let m=1;m<=9;m++){
                    console.log(n + "*" + m + "=" +(n*m) +"<br>");
                }
            }
            else if (n>=9){
                break;
            }
            n++;
        }