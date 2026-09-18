#함수
#개발자가 함수명 통해서 정의한 후에 필요할 때마다 호출
#반복되는 코드를 한번 구현 한 후 재사용 가능하도록 만든 코드의 집합
#함수구현 후 -> 재사용

#매개변수가 있는함수
#매개변수가 없는함수
#결과값 반환하는 함수(return)
#결과값 반환 안하는 함수

def func1():    #매개변수가 없는함수
    print("함수1")  #결과값 반환 안하는 함수

#함수호출
func1()

def func2(a,b): #매개변수가 있는함수
    print(a,b)  #결과값 반환 안하는 함수

func2(1,2)

def func3(a,b): #매개변수가 있는함수
    return a+b  #결과값 반환하는 함수(return)

print(func3(10,20))

#함수정의
#def 함수명(aprameter)
#   함수정의코드

def name(word):
    print(word)

a="python"
name(a)

print("==================================")

def name2(word):
    n='Hi'+(word)
    return n

x=name2('good')
print(x)

def qq(a,b):
    for i in range(a,b):
        print(i, end=" ")
    print()

qq(1,10) #1~9까지 출력
qq(4,6) #4~5까지 출력

print("==================================")

def func1(*args):
    for i in args:
        print(i)

func1('gildong')
func1('gildong','tom','juli')
func1('gildong','tom','juli','jack')

print("==================================")

## **kwargs
def func2(**kwargs):
    for i in kwargs.keys():
        print(i, kwargs[i], type(i), kwargs, type(kwargs))

func2(name1='철수')
func2(name1='영수', name2='영희', name3='철희')
func2(name1='바보', name2='영미')

print("==================================")

# *args : 반환 tuple
# **kwargs : 반환 dick
def func3(arg1, arg2, *args , **kwargs):
    print(arg1, arg2, args , kwargs)

func3(10,40,'kim','lee','park',age=10,adr='seoul')

print("==================================")

#매개변수 순서 규칙(일반 인자, *args, **kwargs)
#def func3(arg1, arg2, *args, **kwargs)

#p.185
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False

print(is_odd(4))

def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))









