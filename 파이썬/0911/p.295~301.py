#1.
class Calculator:
    def __init__(self):
        self.value=0

    def add(self, val):
        self.value+=val

class UpgradeCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def minus(self, num):
        self.value-=num

cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#2
class Calculator:
    def __init__(self):
        self.value=0

    def add(self, val):
        self.value+=val

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def add(self, val):
        self.value+=val
        if self.value >100:
            self.value=100

cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#6

x=list(map(lambda i : i*3, [1,2,3,4]))
print(x)