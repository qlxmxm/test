#if
print(type(True))
print(type(False))

if True:
    print('참')
else:
    print('거짓')

x=20
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

#참 : "javascript",["python"], (10), {a:3}, 1, {'aa'}
#거짓 : "" [] () {} 0 None

adr=""
if adr:
    print(adr)
else:
    print('주소 뭐야')

adr="seoul"
if adr:
    print(adr)
else:
    print('주소 뭐야')

a=85
b=29
c=20

print(a>b and b>c)
print(a>b or b>c)
print(not a>b)
print(not b>c)
print(not True)
print(not False)

print(3+2 > 7+3)
print(3+2==5 and not 7+3>0) #true and false

grade1=90
grade2='A'

if grade1>=90 and grade2 == 'A':
    print('합격')
    print('합격이야~~')
else:
    print('불합격')


#in, not in
#p.128
x=[10,20,30] #list
y={70,80,90,100} #set
z={"name":"Kim","city":"seoul","id":"gildong"} #dict
m=(10,20,24) #tuple

print(25 in x)
print(90 in y)
print(20 not in m)
#p.101
print("city" in z)
print("gildong" in z.values()) #값들에 gildong값이 있는지 확인


#90점 이상이면 A,
#80점 이상 B,
#70점 이상 C,
#그 외 F

score=90

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("F")

#중첩 조건문
grade='A'
total=85

if grade=='A': #선행조건이 true여야 안쪽 if문 확인가능
    if total>=90:
        print('장학생')
    elif total>=80:
        pass
    else:  #total이 80미만일때
        print('학생')
else: #grade가 A가 아닐때
    print('다시 시험봐야함')