#초기 조건 증감
#while 조건:
#  반복할 실행코드

num=5
while num>0:
    print(num)
    num=num-1

a=['a','b','c']
while a: #리스트에 값이 있으므로 True로 인식
    print(a.pop())

#10 9 8 7 6 5 4 3 2 1
n=10
while n>0:
    print(n)
    n-=1
    if n==2:
        break #반복문 탈출

n=10
while n>0:
    print(n) #3 2 1
    n-=1
    if n==2:
        continue #제외 (n==2이면 반복문 다시 실행)
    print(n) #3 1 0

print("----------------------")

i=1
while i<=10:
    print(i) # 1 2 3 4 5
    if i==5:
        break #if i==5 끝
    i+=1 # 2 3 4 5

print("----------------------")

n=10
while n>0:
    n-=1
    print(n) #9 8 7 6 5
    if n==5:
        break
    else:
        print("final")

print("----------------------")

a1=['water', 'python', 'java', 'phone']
s1='py'
i=0

#리스트 끝까지 py랑 같은지 확인하는 코드 -> 같으면 반복문 종료시킴
#while 뒤의 else는 루프가 break없이 끝났을 때만 실행된다!
#while~else 구문 (while루프가 정상적으로 끝났을 때만 else블록 실행된다. break로 루프가 중간에 종료되면 else실행안된다)
while i < len(a1):
    if a1[i]==s1:
        break
    i+=1
else:
    print("hi")

#무한반복
# while True:
#     print("python")

li=['a','b','c']
while True: #무한루프 안에서
    if not li:  #li리스트에 값이 없으면
        break   #반복문 탈출
    print(li.pop()) #li리스트에 값있으면 끝에서부터 출력



