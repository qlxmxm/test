#파이썬 자료형
# '''
# int 정수
# float 실수
# complex 복소수
# bool 불린
# str 문자열
# list 리스트
# tuple 튜플
# set 집한
# dict 사전(딕셔너리)
# '''

#데이터 타입
str1="Python"
bool1=True
float1=10.4
int1=3
list=[str1]
dict1={"name":"gildong","id":3}
tuple1=4,2,4
set1={1,2,3,4}

#데이터 타비 출력
#파이썬은 모든 것이 객체이다.
print(type(str1))   #<class 'str'>
print(type(bool1))  #<class 'bool'>
print(type(float1)) #<class 'float'>
print(type(int1))   #<class 'int'>
print(type(list))   #<class 'list'>
print(type(dict1))  #<class 'dict'>
print(type(tuple1)) #<class 'tuple'>
print(type(set1))   #<class 'set'>

#str1="Python"
#str1이라는 문자자체를 객처로 만들고 다양한 속성(변수), 행동(함수)을 넣을 수 있다.

#숫자형 연산자
#+,-,*,/,%
i1=30
i2=944
big_int1=123123123123123123123123123123123123123123123213
big_int2=999999999999999999999999999999999999999999999999
print(i1+i2) #974 정상출력
print(big_int1+big_int2) #메모리 허용범위에서 무한대 사용가능 (정수 크기 제한 없음 정상출력)

print(3**4) #81 3의 4승

f1=1.234
f2=3.458
print(f1+f2)
print(f1-f2)
print(f1/f2)
print(f1*f2)
print(f1%f2)

#형 변환
a=3.
b=10
c=.5
d=12.5
print(type(a), type(b), type(c), type(d))

#정수 -> 실수
print(float(b)) #10.0

#실수 -> 정수
print(int(c)) #0

#bool True -> 정수
print(int(True))    #1
print(float(True))  #1.0
print(int(False))   #0
print(float(False)) #0.0
print(complex(3))   #정수 -> 복소수 (3+0j)

#수치 함수
print(abs(-42)) #절대값함수  42
print(pow(3,4)) #3**4  81










