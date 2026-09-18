#클로저
#함수 안의 함수를 결과로 반환할때(콜백함수, 데코레이터 함수에 사용)

#add바깥함수 안에 wrapper라는 함수가 안에 있다.(inner function)
#내부함수가 바깥함수의 n1을 기억하고 사용할 수 있는 구조로 되어있다(클로저의 특징)
def add(n1):
    def wrapper(n):
        return n1+n
    return wrapper

a1=add(10)  #a1=wrapper
print(a1(10))   #wrapper(10)

# a1=add(10) => n1=10 저장 -> wrapper함수 반환 -> a1에는 wrapper들어감
# print(a1(10)) => print(wrapper(10)) 실행 -> n1(기억된 10)+10 = 20

a2=add(20)
print(a2(10))

print("=================================")

#데코레이터 = 장식하는 도구(기능 확장o)
#함수에 @기능을 붙인다

# #클로저를 사용해 데코레이터 구현함
# def trace(func):
#     def wrapper():
#         print('시작')
#         func()
#         print('끝')
#     return wrapper #함수반환

# def hi():
#     print('hi')

# def hello():
#     print('hello')

# t1=trace(hi)
# t1()

# t2=trace(hello)
# t2()

#클로저를 사용해 데코레이터 구현함
def trace(func):
    def wrapper():
        print('시작')
        func()
        print('끝')
    return wrapper #함수반환

@trace  #hi=trace(hi)
def hi():
    print('hi')

@trace
def hello():
    print('hello')

hi()    #hi = trace(hi) 를 자동으로, 함수 정의 시점에 실행해준다. hi=wrapper
hello() #hello=trace(hello)

print("=================================")

def trace(func):
    def wrapper(*args, **kwargs):
        result=func(*args, **kwargs)
        print(args, kwargs, result)
        return result
    return wrapper

@trace  #trace(big) #1. 데코레이터 호출되면 wrapper실행됨
def big(*args): #2. wrapper(10,20) 실행 -> result = max(10.20) => 20반환
    return max(args)

@trace
def mini(**kwargs):
    return min(kwargs.values())

print(big(10,20))
print(mini(x=20, y=30, z=40))

print("=================================")

class Tr:
    def __init__(self, func):
        self.func=func

    def __call__(self):
        print(self.func.__name__, "시작")
        self.func()
        print(self.func.__name__, "끝")

#클래스형 데코레이터 :
#@데코레이터 :함수, 인스턴스로 바꿔주는 문법

#객체명=클래스명()
# hi2=Tr(hi)

#Tr(hi)
@Tr #Tr클래스의 __init__에 hi를 전달해줘..->func값이 hi가 되면서 hi는 함수가 아니라 Tr의 인스턴스
def hi():
    print("hi")

hi()    #hi는 인스턴스가 되었다. 인스턴스를 함수처럼 썼기때문에 __call__ 자동호출됨