#5.
# age=20
# name="에릭"
# score='A'
# sight=0.5
# "에릭은 20살의 0.5시력이며 학점은 A이다" 라는 문자열을
# format함수, f-string 로 각각 작성해라.

age=20
name="에릭"
score='A'
sight=0.5
# "에릭은 20살의 0.5시력이며 학점은 A이다" 라는 문자열을
# format함수, f-string 로 각각 작성해라.
print('{}은 {}살의 {}시력이며 학점은 {}이다'.format(name, age, sight, score))
print(f'{name}은 {age}살의 {sight}시력이며 학점은 {score}이다')

#6.
# names 리스트에 "찰스, 스누피, 루피"를 넣는다.
# "찰스는 파이썬 배워요" 를 출력해라.

# names 리스트에 "찰스, 스누피, 루피"를 넣는다.
names = ['찰스', '스누피', '루피']
# "찰스는 파이썬 배워요" 를 출력해라.
print(f'{names[0]}는 파이썬 배워요')

