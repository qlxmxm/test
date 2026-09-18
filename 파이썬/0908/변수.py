#a=[1,2,3]
#a는 리스트[1,2,3]이 저장되어있는 메모리 주소값 가지고 있다(reference)
#print(id(a))

n=100
print(type(n))
print(id(n))

#동시 변수 선언가능
a=b=c=d=100

n=50 #값 덮어씀
print(n)

#p.247
a=3
print(id(3))
print(id(a))
b=a
print(id(b))

x=3
y=5
x,y=(y,x) #언팩킹
print(x)
print(y)

#p.114
#from 모듈명 import 함수
from copy import copy
a2=[1,2,3] #복사를 했지만 요소만 복사 / 주소값은 복사하지 않음
b2=copy(a2) #b2는 a2를 복사해서 새로운 객체가 생성됨

print(a2)
print(b2)

print(b2 is a)
print(id(a2))
print(id(b2))