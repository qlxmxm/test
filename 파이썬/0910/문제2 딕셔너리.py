
# 2. 빈 딕셔너리를 선언하고
# 무한루프로 이름과 tv보는것을 좋아하는지 입력받는다
# 입력 후, 이름과 tv보는것 좋아하는지에 대한 대답을
# 딕셔너리에 추가한다.
# 친구한테도 물어볼까?라는 질문에 no 를 받으면 무한루프를 종료시킨다.
# 그 후 딕셔너리 데이터를 items함수를 사용해 다 출력한다.

dict={}
#dict={'홍길동':'tv좋아함','김길동':'tv싫어함',........}

while True:
    name=input('이름은?')
    tv=input('tv좋아해?')
    dict[name]=tv

    ans=input('친구한테도 물어볼까?')
    if ans=='no':
        break
    print(dict.items())






