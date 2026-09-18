class Car:
    #p.205
    def __init__(self,make,model,year): #생성자 호출하는 인스턴스 메소드
        #객체 초기화함
        self.make=make #c1.make='tesla'
        self.model=model #c1.model='models'
        self.year=year #c1.year=2018
        self.speed=0 #Car객체의 속성 speed를 선언하여 초기화함

    #인스턴스메소드는 첫번째 인자로 항상 self가 있어야함
    def name(self):
        names=str(self.year) + " " +self.make + " "+self.model
        return names

    def speed1(self):
        print(str(self.speed) + "이다")

print("==================================")

#객체명=클래스명(init함수의 매개변수)
#객체생성코드 -> 자동으로 __init__호출
c1=Car('tesla','models',2018)
print(c1.name()) #인스턴스를 통해 호출하면 파이썬이 자동으로 인스턴스를 self에 넣어줌
c1.speed1()

#object클래스 상속받음
class Fruit:
    price=20000 #클래스 변수

    def __init__(self, title, color):
        self.title=title
        self.color=color

    def info(self):
        return "{}과일은 {}색".format(self.title, self.color)

    def buy1(self,buy1):
        return "{}과일 {}에서 사야지~".format(self.title, buy1)

print("==================================")

#인스턴스 생성 2개
f=Fruit('banana','yellow')
f2=Fruit('Apple','red')

print(f.info())
print(f.buy1('lotte'))

print(f2.info())
print(f2.buy1('hyundai'))

class A:
    def add(a,b): #클래스메소드(정적메소드)로 보고 코드를 구현하겠다.(self지정 하지 않음)
        print(a+b)

    def minus(a,b):
        print(a-b)

print("==================================")

#객체생성코드
# a=A()
# a.add(3,4) #a라는 인스턴스를 받을 self가 없음

#객체로부터 클래스메소드에 접근 불가
#클래스명으로부터는 가능
A.add(3,4)
A.minus(5,3)

print("==================================")

class Student:
    def __init__(self, id, name, score=0):
        self.id=id
        self.name=name
        self.score=score

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score=score

    def getScore(self):
        return self.score

class Cal:
    def __init__(self):
        self.stu=[]

    def add(self,student):
        self.stu.append(student)
        #self.stu에 student추가

    def avg(self):
        sum=0
        #[a,a2,a3,a4]
        # a=> 객체(id,name,score)
        for i in self.stu:
            sum+=i.getScore()
        average=sum/len(self.stu)
        return average, len(self.stu) #p.163


a=Student(1,"찬웅")
a.setScore(100)

a2=Student(2,"예진",score=90)
a3=Student(3,"우정",score=80)
a4=Student(4,"소영",score=80)

c=Cal() #self.stu=[]
c.add(a) #self.stu=[a,a2,a3,a4]
c.add(a2)
c.add(a3)
c.add(a4)

print('평균:{0}'.format(c.avg()))










