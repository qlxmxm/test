#인스턴스 메소드, 인스턴스 변수
#클래스 메소드, 클래스 변수

class Test:
    def func1():    #self 인자가 없는 함수 -> 클래스 안에 있지만 인스턴스 메소드 아님
        print("Func1!!")

    def func2(self):    #인스턴스 메소드로 호출시 자동으로 self(인스턴스 객체 자신)가 전달됨
        print(id(self))
        print("Func2!!")

t=Test()
#t.func1()   #예외 -> func1()에 self가 없는데, t.func1()호출시 파이썬 내부저그로 func1(t)호출하려한다
t.func2()

Test.func1()    #클래스에서 직접호출
#Test.func2()    #예외 -> func2(self)인데 인자 없이 호출해서 self(Test의 인스턴스)가 없어 예외
Test.func2(t)   #직접 인스턴스 t를 self로 넘겨 호출



