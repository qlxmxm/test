class Vehicle:
    #변수에 처음 값을 대입 -> 초기화
    def __init__(self, name, speed):
        self.name=name 
        self.speed=speed

    def move(self):
        return f"{self.name}은 시속{self.speed} 이다"

#Vehicle 상속받아서 Car, Bicycle 클래스 만들기
class Car(Vehicle):
    def move(self):
        return super().move() +"소나타 자동차"

class Bicycle(Vehicle):
    def move(self):
        return super().move() +"자전거"


car=Car("소나타",120) # __init__함수호출 -> Vechicle의 __init__호출 -> 초기화 -> move()
bike=Bicycle("자전거",20)
print(car.move())
print(bike.move())

#객체 : car, bike
#car : move()
#bike : move()