
# 8. msg="It is Time" 설정하고 
# for문 range함수를 사용하여 문자열 길이까지 다 출력
# 대문자인것만 뽑아서 출력

msg = "It is Time"

for i in range(len(msg)):
    print(msg[i], end=' ')

print("==================================")

for i in msg:
    if i.isupper():
        print(i, end= ' ')

#9. 1~10까지 수 중 홀수만 출력 (range, continue사용)
#range 사용
for i in range(1,11,2):
    print(i)
#continue 사용
i=1
while(i<=10):
    if i%2==1 :
        print(i)
    i+=1

#10. 3~32까지 수 중 3의 배수만 출력
for i in range(3,33,3):
    print(i)


