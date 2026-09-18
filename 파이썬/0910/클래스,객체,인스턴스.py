#객체(object): 파이썬에서 존재하는 모든 것
#   ex)123,"Hello", [1,2,3]

#class 설계도
#object 설계도를 바탕으로 실제 만들어진 제품

#클래스
#self, 인스턴스 메소드, 인스턴스 변수
#클래스 메소드, 클래스 변수

#객체(object): 클래스의 인스턴스를 포함한 모든 파이썬 데이터 /123, "Hello", [1,2,3]...........
#인스턴스(instance): 특정 클래스에 의해 생성된 객체를 지칭할때
class Profile:
    name="gildong"  #클래스 변수(클래스 블록 안 -모든 인스턴스 접근가능(공유))

    #초가화 함수(self:객체 자기자신)
    def __init__(self,name,age):    #인스턴스 변수:각 인스턴스마다 개별적으로 존재
        self.name=name
        self.age=age

p=Profile("gildong",13) #객체가 생성되면 __init__함수 자동 호출됨
p2=Profile("jiji",23)

#p,p2 -> Profile클래스의 인스턴스

print(p==p2)
print(id(p), id(p2))

print('{0} {1} {2} {3}'.format(p.name,p.age,p2.name,p2.age))

#p.112,114
c=p
print(p==c,id(p),id(c))

from copy import copy
c=copy(p)
print(p==c,id(p),id(c))












