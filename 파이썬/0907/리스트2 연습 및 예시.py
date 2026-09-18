#파이썬 리스트
#파이썬에서는 배열 제공하지 않는다
#리스트 (순서 o, 중복 o, 수정 o, 삭제 o)

#리스트 함수
a=[5,3,2,4,1]
print("a = " , a)
a.append(6)
print("a.append(6) = " , a)

#오름차순 정렬
a.sort() 
print("a.sort() = " , a)

#거꾸로 출력
a.reverse()
print("a.reverse() = " , a)

print("a.index(5) = " , a.index(5)) #[6, 5, 4, 3, 2, 1] 의 5의 위치

a.insert(2,7) #인덱스 2에다 7삽입
print("a.insert(2,7) = ", a)

a.reverse()
print("a.reverse() = " , a)

a.remove(1) #삭제
print("a.remove(1) = ", a)

a.pop()
print("a.pop() = " , a) #[2,3,4,7,5]

#print(a.pop()) #5 삭제
print("print(a.pop()) = " , a.pop())
print("a = " , a)

print("a.count(4) = " , a.count(4))
print("a.count(1) = " , a.count(1))

ex1=[8,9]
a.extend(ex1) # [2,3,4,7] + [8,9]
print(a)

#리스트 선언
li1=[]
li2=list()
li3=[4,2,6,7,1]
li4=[3,3,'jack','tom']
li5=[1,3,['banana','apple','orange']]
li6=[2,True,False,'mango','coffee',3.43]

#li4의 tom출력
print(li4[3])

#li5의 apple출력
print(li5[2][1])

#li4
#print(li4[::-1])
li4.reverse()
print(li4)

a="abcdefg"
print(a[0:5:2])







