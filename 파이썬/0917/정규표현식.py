import re

def email(text):
    pattern=r'^[\w+]+@[\w]+\.[\w.]+$'
    return re.match(pattern, text)

print(email("test@naver.com")) #매치됨  @기호들어가야함
print(email("test-naver-com")) #매치안됨

# #010-1234-5678
# #p.358,361
# def phone_number(text):
#     pattern=r'010-\d{3,4}-\d{4}'
#     return re.findall(pattern,text)


# text="내 연락처는 010-1234-5678이고 동생 연락처는 010-994-3433입니다"
# print(phone_number(text))

#p.376
# p=re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m=p.search("park 010-1234-1234")
# print(m.group("name"))
# print(m.group(2))
# print(m.group(3))