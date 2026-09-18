#문제3
# invite 리스트를 만들어 "찰스, 스누피, 루피"를 넣는다.
# insert()를 써서 "둘리" 를 맨 앞에 추가해라.
# append()를 써서 "토심이" 를 리스트 마지막에 추가해라.
# 리스트에 친구가 두명만 남을때까지 pop()을 써서 제거해라.

invite=["찰스","스누피","루피"]

invite.insert(0,"둘리");
invite.append("토심이")

print(invite)

invite.pop()
invite.pop()
invite.pop()

print(invite)

# while len(invite) !=2:
#     invite.pop()
# print(invite)












