class Total:
    def __init__(self):
        self.total=0

    def __iter__(self):
        return self

    def __next__(self):
        return self.total


    def add(self,n):
        self.total += n
        return self.total


gen=Total()
next(gen)
print(gen.add(10))
print(gen.add(5))
print(gen.add(20))







