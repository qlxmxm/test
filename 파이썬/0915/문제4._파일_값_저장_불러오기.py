# 파일에 값 저장해서
# 점수 불러와서 평균 구함 -> 파일이 없으면 "파일이 없습니다" 예외처리

#p.175
def score1(name,score):
    with open('score1.txt','a',encoding='utf-8') as f:
        f.write(f"{name},{score}\n")


#p.179
def average():
    sum=0
    cnt=0
    try:
        with open('score1.txt','r',encoding='utf-8') as f:
            for i in f:
                i=i.strip()
                name,score=i.split(",")
                sum+=int(score) #0+100 #100+90=190
                cnt+=1  #1 #2
        return sum/cnt

    except FileNotFoundError:
        print("파일이 없습니다")


score1('홍길동',100)
score1('김길동',90)

avg=average()
print(avg)



