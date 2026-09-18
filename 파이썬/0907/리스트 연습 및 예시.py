#파이썬 리스트
#파이썬에서는 배열 제공하지 않는다
#리스트 (순서 o, 중복 o, 수정 o, 삭제 o)

#p.77
list1=[]
list2=list()
print(list1, list2)
print(type(list1), type(list2))

list3=[60,100,98,95]
list4=[1000,1000,'Tom','Juli',"Jack"]
list5=[1000,1000,['Tom','Juli',"Jack"]]
list6=[3.42,'python',3,1,False,3.2212]

print("list3 = " , list3)
print("list6 = " , list6)

#인덱싱
print("list4 = " , list4[1])
print("list4 = " , list4[0] + list4[1] + list4[1])
print("list4 = " , list4[-1])    #뒤에서 첫번째 값
print("list5 = " , list5[-1][1]) #뒤에서 첫번째 값중 ['Tom','Juli',"Jack"] 인덱스 1값

#슬라이싱
print("list4[0:3]   = " , list4[0:3])       #[1000, 1000, 'Tom']
print("list4[2:]    = " , list4[2:])        #인덱스 2부터 끝까지
print("list5[2][1:3] = " , list5[2][1:3])    #['Tom', 'Juli', 'Jack'] 에서 인덱스 1부터 2까지

#연산
print("list3+list4 = " , list3+list4)  #리스트 합치기
print("list3*3 = " , list3*3)          #리스트 반복
#print(list3[0] + "hi")
print("str(list3[0]) + 'hi' = " , str(list3[0]) + "hi") #"60" + "hi"
print('list4[2]+"hi" = ' , list4[2]+"hi")

#수정
list3[0]=4  #4를 list3[0]자리에 넣어
print("list3[0]=4 수정 " , list3)

list3[1:2]=[1,2,3]
print("list3[1:2]=[1,2,3] 수정 " , list3)

list3[1:2]=[]
print("list3[1:2]=[] = " , list3)
#삭제
del list3[3]
print("del list3[3] = " , list3)
#중복
print(list4)









