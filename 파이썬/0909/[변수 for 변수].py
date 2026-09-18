
a=[1,2,3,4]
#[변수 for 변수 in collection]
result=[num*3 for num in a if num%2==0] #짝수(2,4) 뽑아서 num*3 실행
print(result)

#3~30출력 ->list
#[3,4,5,6......30]
for i in range(3,31):
    print(i)

b=[i for i in range(3,31)]
print(b)

#3~30출력 3의 배수만 ->list
b2=[i for i in range(3,31) if i%3==0]
print(b2)
#for i in range(3,31):
#   if i%3==0:
#       print(i)

#1~10까지 ->list
print([i for i in range(1,11)])

#p.148 마지막박스코드
result=[x*y for x in range(2,10) for y in range(1,10)]
print(result)


#3의 배수의 합 구하기
result = 0
i=1
while i<=1000:
    if i%3==0:
        result +=i
    i+=1
print(result)







