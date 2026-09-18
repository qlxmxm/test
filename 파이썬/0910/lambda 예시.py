a=1
def vartest(a):
    a=a+1
    return a

a=vartest(3)
print(a)

#1.vartest(3) 4=4+1 -> return 4 -> a=4 -> a=1 이었지만 a=4 로 되면서

#p.170
#함수명=lambda 매개변수:실행문

add=lambda a,b:a+b
result=add(3,4)
print(result)

print("==================================")

#람다 왜 쓰냐
#가독성 좋음, 코드간결, 메모리 절약
#즉시 실행 함수 -> 정의하자마자 바로 실행됨

def multi(x,y):
    return x*y

multi=lambda x,y:x*y
print(multi(3,4))

def plus(x):
    return x+10
print(plus(1))

plus=lambda x:x+10
print(plus(1))


def multi(x,y):
    return x*y
print(multi(4,5))

a=multi #함수명을 a에 할당함(a는 alias - 별칭이 됨)
print(a(4,5))

def final(x,y,func1):   #함수를 다른 함수의 매개변수로 넘길 수 있음 -> 고차함수 -> multi가 final의 매개변수로 들어감
    print(x,y,func1(5,6))

final(1,2,multi)
