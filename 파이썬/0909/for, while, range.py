
test_list=['one','two','three']

for i in test_list:
    print("test_list = ", i)

#for i in test_list:

names=['kim','lee','park','choi']
for i in names:
    print("names = ",i)

word="python"
for i in word:
    print("word = ", i)

profile={
    "name":'hong',
    "age":33
}

for i in profile:
    print("profile = " , i)    #키값
    print(profile[i])  #키에 대응되는 값

print("==================================")

for i in profile.values():
    print("profile.values() = ", i)

fruit='PineApplE'
for i in fruit:
    if i.isupper(): #대문자인지 확인
        print(i)
    else:
        print(i.upper()) #대문자로 변환

num=[34,62,63,1,35,6,2]
for i in num:
    if i==35:
        print("35!")
        break
    else:
        print(i)

print("==================================")

#is : 두 객체가 같은 다입객체(메모리 주소가 같은지) 인지 비교하는 연산자!
#== : 값이 같은지 비교
#type : 하나의 고정된 타입 객체반환

li=["3",1,2,True,4.5]

for i in li:
    if type(i) is str:
        continue    # "3" 제외
    print(i, type(i))

#for~else 구문
#else블록은 for문이 break로 중간에 끊기지 않고 끝까지 실행되었을때만 실행됨
num=[34,62,63,1,35,6,2]
for i in num:
    if i==35:
        print("35!")
        break
else:
    print("hihi")

fruit2="Mango"
print(reversed(fruit2))
print(list(reversed(fruit2)))
print(tuple(reversed(fruit2)))
print(tuple((fruit2)))
print(set(fruit2))

#1~10까지 #range
for i1 in range(10):    #0~10미만
    print(i1)

#while문 바꾸기
i=1
while(i<=10):
    print(i)
    i+=1
print()

for i3 in range(1,11,2):    #1~10 수 중 2씩 증가
    print(i3, end='')
print()

#1~10까지 합
#p.145
sum1=0
for i in range(1,11):
    sum1+=i
print(sum1)

for i in range(2,10): #2~9
    for j in range(1,10): #1~9
        print(i*j, end=" ")
    print('') #단 출력 후 줄바꿈(enter)







