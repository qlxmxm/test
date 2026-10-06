function Item(name, kor, eng, math){
            this.name=name; 
            this.kor=kor;
            this.eng=eng;
            this.math=math;

            let a=(kor+eng+math)/3;

            this.show=function(){
                console.log(`${name} 님의 평균은 ${a} 입니다`);
            }
        }

        let item1=new Item('김길동',95,85,85);
        let item2=new Item('이길동',88,77,90);
        let item3=new Item('박길동',66,76,79);

        item1.show();
        item2.show();
        item3.show();