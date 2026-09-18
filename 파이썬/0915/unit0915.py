#파이썬 클래스
#OOP (객체 지향 프로그래밍)
#클래스 변수 vs 인스턴스 변수

class Dog: #object 상속
    species='firstdog'

    #초기화
    def __init__(self,name,age):
        self.name=name  #a.name='mikky
        self.age=age    #a.age=2

a=Dog("mikky",2)
b=Dog("baby",3)

print(Dog.species)
print(a.species)
print(b.species)

print("=================================")

class SelfTest:
    def func1():    #self 인자가 없는 일반함수
        print('Func1 called')

    def func2(self):    #인스턴스 메소드로 호출 시 자동으로 self(인스턴스 자신)이 전달됨
        print(id(self))
        print('Func2 called')

f=SelfTest()
#f.func1()   #func1()에 self가 없는데, f.func1()호출 시 파이썬이 func1(f) 호출하려함..
f.func2()   #func2(self)에 self=f 가 자동 전달됨
SelfTest.func1()    #func1()은 클래스메소드이므로 클래스에 직접 호출가능
#SelfTest.func2()    #func2(self)인데 인자 없이 호출해서 self가 없어 예외..
SelfTest.func2(f)   #직접 인스턴스 f를 self로 넘겨 호출








