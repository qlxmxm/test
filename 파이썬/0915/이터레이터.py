# it=[1,2,3,4,5]
# it2=iter(it)
# print(next(it2))
# print(next(it2))
# print(next(it2))

# it=[1,2,3,4,5].__iter__()
# #iter객체를 얻은 후 next
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

it=[1,2,3,4,5].__iter__()
print(next(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
#print(it.__next__()) #StopIteration

print(("hello").__iter__())
print(({'a':1,'b':3}).__iter__())
print(({1,2,3}).__iter__())


class Cnt:
    def __init__(self,stop):
        self.current=0
        self.stop=stop

    def __iter__(self):  #iter(Cnt(5)) -> 이터레이터 객체 만듬
        return self

    def __next__(self):  #next(obj) -> 반환된 이터레이터 객체에 next()반복호출
        if self.current < self.stop:
            result=self.current
            self.current+=1
            return result
        else:
            raise StopIteration #예외 강제발생!

c=Cnt(5)
#객체 생성시 자동으로 __init__호출
#for문이 자동으로 __next__호출
for i in Cnt(5):
    print(i)