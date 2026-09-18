#딕셔너리
#순서 x, 키 중복 x, 수정 o, 삭제 o
#{key:value}
dic1={'name':'Lee', 'phone':'010-1234-5555', 'birth':'000211'}
dic2={0:'python'}
dic3={'ary':[1,2,3,4]}
dic4={
    'name':'tom',
    'addr':'seoul',
    'age':'22',
    'grade':'A',
    'status':True
}
dic5=dict()  #{}
dic6=dict([('name','tom'),('addr','seoul'),('age','22'),('grade','A'),('status',True)])

#기존 값 덮어씀(키값 중복되면)
a={1:'c',1:'a',1:'b',1:'d'}
print(a)

#딕셔너리 값 추가(p.94)
#dic1={'name':'Lee', 'phone':'010-1234-5555', 'birth':'000211'}
dic1['address']='yongsan'
print(dic1)

dic1['score']=[90,30,40]
print(dic1)

print(len(dic1), len(dic2), len(dic3), len(dic4))

#딕셔너리 함수들
print(dic1.keys()) #키들의 집합
print(dic2.keys())

print(list(dic1.keys())) #리스트형으로 변환해서 출력
print(list(dic3.keys()))

print(dic1.values()) #값(value)들의 집합
print(list(dic1.values()))  #리스트형으로 변환해서 출력

print(dic3.items()) #키, 값 쌍 다 출력
print(list(dic3.items()))

print(dic1.pop('name')) #키값 넣어서 삭제 -> 값도 같이 삭제됨
print(dic1)

print(dic4.pop('addr'))
print(dic4)

#dic1에 'name' 키 속성이 있는지 확인(in)
#p.101
print('name' in dic1)