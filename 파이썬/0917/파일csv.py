#CSV(Comma seperated Values)
import csv  #csv 모듈 불러옴

with open("weather1.csv",'r') as f:
    reader=csv.reader(f) #파일 객체 f를 읽어 csv형식에 맞게 줄 단위로 읽겠다.
    print(reader)
    print(type(reader)) #<class '_csv.reader'> 반복가능한 객체

    for i in reader:
        print(i)    #리스트 구조로 출력

with open('weather1.csv','r') as f:
    reader=csv.reader(f, delimiter=",") #구분자 쉼표로 설정해서 읽어옴

    for i in reader:
        print(i)

print("======================================")

with open('weather1.csv','r') as f:
    reader=csv.DictReader(f)    #csv파일을 dict로 변환해서 읽어옴
    print(reader)

    #i={'상순':13.3, '중순':16}
    for i in reader:    #한행의 dict
        for x,y in i.items():   #속성, 데이터값이 반복해서
            print(x,y)  #딕셔너리 구조로 출력됨
        print("======================================")




