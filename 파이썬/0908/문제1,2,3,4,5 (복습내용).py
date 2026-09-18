
#1. 1~10 까지 수 중 짝수만 출력 (반복문 활용)

n=1
while n<11:
    if n%2==0:
        print(n)
    n+=1

#2. dic={'name':'tom','age':'11'} 
# subject를 python으로 추가한다
# name 을 삭제한다

dic={'name':'tom','age':'11'} 
# subject를 python으로 추가한다
dic['subject']='python'
print(dic)
# name 을 삭제한다
print(dic.pop('name')) #키값 넣어서 삭제 -> 값도 같이 삭제됨
print(dic)

#3. [1,2,3]을 집합자료형으로 바꾼다
s1=set()
s2=set([1,2,3]) #리스트 자료형을 집합 자료형으로 변환
#s=set([1,2,3])
print(s2)

#4. 문자열 python을 list자료형으로 바꾼다
s3=set('python')
li3=list(s3)
#list=list('python')
print(li3)

#5. 
# s4=set([1,2,3,4,5])
# s5=set([6,7,3,4,10])
# 교집합, 합집합을 구해라

s4=set([1,2,3,4,5])
s5=set([6,7,3,4,10])

# 교집합
print(s4&s5)
# 합집합
print(s4|s5)




