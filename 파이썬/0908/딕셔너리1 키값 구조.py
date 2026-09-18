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
#가장 안쪽 구조 : 튜플 구조
#안쪽을 감싸는 구조 : 리스트 구조(여러 개의 튜플을 하나로 묶음 -> 튜플의 리스트)
#가장 바깥쪽 구조: 딕셔너리 구조로 변환해줘

#(키,값) 튜플 -> 튜플들의 리스트 [()]-> dict() -> 딕셔너리 {키:값}
print(dic6)

#dict()객체는 인자를 1개만 받는 구조!!!!!!!!
print(type(dic1),type(dic2),type(dic3),type(dic4),type(dic5),type(dic6))

#p.96
#Key를 이용해 Value값 추출
#딕셔너리명['키명']
#print(dic1['name1']) => KeyError
print(dic1['name']) #키값이 있으면 출력, 없으면 KeyError

#p.100
print(dic1.get('name1')) #키값 없으면 None
print(dic1.get('name'))

print(dic2[0])
print(dic2.get(0))

print(dic3['ary'])
print(dic3.get('ary'))

print(dic4.get('age'))