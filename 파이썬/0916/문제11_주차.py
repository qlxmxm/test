class AlreadyError(Exception):
    pass

class Vehicle:
    def __init__(self,num,kind):
        self.num=num
        self.kind=kind



class Parking:
    def __init__(self):
        self.vehicles=[]

    def add(self, ve):
        #self.vehicles=[ve1,ve2,ve3]
        #맨 처음 add함수 호출할떄는 append가 된다.
        #같은 객체를 넣으면 번호가 같아지므로 예외발생시킴

        

        # 23가5678 == 23나5678
        if any(i.num == ve.num for i in self.vehicles):
            raise AlreadyError('이미 주차되어있다.')

        self.vehicles.append(ve)

    def list_car(self):
        return [i.num for i in self.vehicles if i.kind=="car" ]
        # for i in self.vehicles:
        #     if i.kind=="car":
        #         return i.num  #return: 값을반환함과 동시에 함수실행 종료시킨다.

lot=Parking()
ve1=Vehicle("12가1234","car")
ve2=Vehicle("23나5678","bike")
ve3=Vehicle("34다9101","car")

lot.add(ve1)
lot.add(ve2)
lot.add(ve3)

try:
    lot.add(ve1)
except AlreadyError as e:
    print(e)

print(lot.list_car())   #12가1234, 34다9101








