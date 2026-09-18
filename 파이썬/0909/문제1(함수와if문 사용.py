
# calcu(이름, 시간, 개수, 가격)
# calcu("형민",15,4,20000)
# calcu("종진",12,5,50000)
# calcu("한빈",10,2,70000)
# 15시에 방문하고 3개 이상 구매시 10%할인
# 12시에 방문하고 5개 이상 구매시 20%할인
# => 형민씨는 10%할인= 18000원 형태로 출력 (format함수 . c스타일. f스트링)

def calcu(name,time,num,price):
    if (time==15 and num>=3):
        # price=price*0.9
        print(f'{name}씨는 10%할인 = {price*0.9}원')
    elif (time==12 and num>=5):
        # price=price*0.8
        print("{}씨는 20%할인 = {}원".format(name, price*0.8))
    else:
        print(f"{name}씨는 할인없음 = {price}원")

calcu("형민",15,4,20000)
calcu("종진",12,5,50000)
calcu("한빈",10,2,70000)







