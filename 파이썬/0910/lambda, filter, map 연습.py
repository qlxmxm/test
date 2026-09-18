#1~5까지 list로 표현 (list comprehension)
li=[i for i in range(1,6)]
li2=list(range(1,6))
print(li)
print(li2)

re=list() #re=[1,2,3,4,5]
for i in li2:
    re.append(i)
print(re)

print("==================================")

def positive(x):
    return x>0

#for- if문 기능이 있음

print(list(filter(positive, [1,-3,2,0,-5,6])))



def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))

print("==================================")

#map(f, iterable) : 함수와 반복가능한 자료형을 입력으로 받는다.
def pp(x):
    return x+20

print(pp(4))
print(list(map(pp,[1,2,3])))

def one(i):
    return i

#리스트 요소를 하나한 one의 매개변수로 받아 리턴한다
re2=list(map(one,[1,2,3,4,5]))
print(re2)

one=list(map(lambda i:i, [1,2,3,4,5]))
print(one)

list1=[1,2,3,4,5]

print("==================================")

#list comprehension
#map,fliter (lambda) 같이 활용높음
#lambda

li1=[i for i in range(1,6)]

map1=list(map(lambda i:i, range(1,6)))
print(map1)

#3보다 작은값들만 출력 -> filter
fil1=list(filter(lambda i:i<3,range(1,6)))
print(fil1)

#1부터 10까지 수를 다 100씩 더한다(map)
map2=list(map(lambda i:i+100, range(1,11)))
print(map2)

print("==================================")

def square(x):
    return x**2

list1=[1,2,3,4,5]
re1=list(map(square,list1))
print(re1)

#lambda로 변경
re2=list(map(lambda x:x**2,list1))
print(re2)
# re3=list(map(lambda i:i**2,range(1,6)))
# print(re3)

#list comprehension으로 변경
re3=[x**2 for x in list1]
print(re3)

#1~20까지 수 중의 2의 배수만 출력(list comprehension)
re4=[i for i in range(1,21) if i%2==0]
print(re4)

#re4를 filter로 변경
re5=list(filter(lambda i:i%2==0, range(1,21)))
print(re5)




