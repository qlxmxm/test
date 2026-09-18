#문제1. "에릭" 이라는 이름을 변수에 저장하고 
# "안녕 에릭 좋은아침이네"
# c스타일, format함수, f-string으로 각각 작성해라.

name="에릭"

#c스타일
ct='안녕 %s 좋은아침이네' %(name)
print(ct)

#format함수
formatt='안녕 {s} 좋은아침이네'.format(s=name)
print(formatt)

#f-string
fst=f'안녕 {name} 좋은아침이네'
print(fst)


