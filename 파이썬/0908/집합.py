#집합
#순서(x), 중복(x)

s1=set()
s2=set([1,2,3,4]) #리스트 자료형을 집합 자료형으로 변환
s3=set([1,4,6,7])
s4=set([1,2,'apple','mango','python'])
s5={'phone','computer','notebook','water','phone'}
s6={12,'mouse',(1,2,3),3.14}

print(type(s1), type(s2), type(s3), type(s4), type(s5), type(s6))

#s2를 튜플로 변환
t=tuple(s2)
print(t, type(t))

#튜플로 변경했기 때문에 인덱스 사용가능
print(t[0], t[1:3])

#s3,s4 list로 변경
#리스트로 변경했기 때문에 인덱스 사용가능
li=list(s3)
li2=list(s4)
print(li[0], li2[1:3])

set1=set([1,2,3,4,5,6])
set2=set([4,5,6,7,8,9])

print(set1&set2)
print(set1.intersection(set2))

print(set1|set2) #요소 중복제거되면서 합쳐짐
print(set1.union(set2))

print(set1-set2) #{1,2,3} set1에는 있지만 set2에 없는 요소들
print(set1.difference(set2))

#중복 요소 확인(두 집합에 공통 요소 없으면 true, 있으면 false)
print(set1.isdisjoint(set2)) #공통요소 4,5,6있음

#부분집합 - set1의 모든 요소가 set2에 있는지 확인(set1이 set2의 부분집합이냐?)
print(set1.issubset(set2))

#set1이 set2의 모든 요소를 포함하냐(set1이 set2를 포함하는가?)
print(set1.issuperset(set2))

a=set([1,2,3,4]) # a={1,2,3,4}
a.add(5)
print(a)

a.remove(2)
print(a)

#a.remove(6) #없는 값 삭제 -> KeyError
#print(a)

a.discard(3)
print(a)

a.clear() #다 제거(요소만 사라진다. 구조는 남아있음)
print(a)

a.update([1,2]) #값 여러개추가
print(a)