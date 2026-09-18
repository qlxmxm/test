
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

print("==================================")

class Person:
    def __init__(self):
        print('안녕')

#p.208 
#class 자식클래스명=서브클래스명(부모클래스= 슈퍼클래스 명)
class Student(Person):
    def __init__(self):
        print('학생은 공부해')
        super().__init__()

p=Person() 
s=Student()

class Super:
    def a(self):
        print('super')

    
class Sub(Super):
    def a(self):
        print('자식클래스') #오버라이딩

    def b(self):
        print('sub')

s=Sub()
s.a()
s.b()

s1=Super()
s1.a()
# s1.b()

print("==================================")

class Car:
    #p.205
    def __init__(self,make,model,year): #생성자 호출하는 인스턴스 메소드
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

#p.208
class CampingCar(Car):
    def __init__(self,make,model,year,bed):
        super().__init__(make,model,year)   #부모클래스에 있는 __init __ 호출
        self.bed=bed

#객체 생성
camp1=CampingCar('tesla','models',2017,2)
print(camp1.name())
camp1.speed1()

c1=Car('audi','mo',2010)
print(c1.name())
c1.speed1()









#객체명=클래스명(init함수의 매개변수)
#객체생성코드 -> 자동으로 __init__호출
c1=Car('tesla','models',2018)
print(c1.name()) #인스턴스를 통해 호출하면 파이썬이 자동으로 인스턴스를 self에 넣어줌
c1.speed1()



