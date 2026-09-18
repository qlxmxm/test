class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def pay(self):
        return self.salary

class Manager(Employee):
    def pay(self):
        return self.salary*1.5

class Developer(Employee):
    def __init__(self, name, salary, overtime=0):
        super().__init__(name, salary)
        self.overtime=overtime

    def pay(self):
        return self.salary + self.overtime * 30000

emp=[Employee('김사원', 3000000), Manager('이팀장', 4000000), Developer('양개발자', 5000000, overtime=10)]

for i in emp:
    print(f"이름: {i.name} - 월급 {i.pay()} 원")











    