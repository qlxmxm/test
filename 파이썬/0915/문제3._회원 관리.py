# 회원 관리
# 요구사항:
# User 클래스
# id
# name
# email​

# UserManager 클래스
# 회원 추가
# 회원 삭제
# (id로 검색)
# 전체 출력
# 리스트로 관리.

class User:
    def __init__(self, id, name, email):
        self.id=id
        self.name=name
        self.email=email

    #객체 출력시, 자동으로 호출되면서 -> 객체가 문자열로 변경되서 출력됨 (__str__)
    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}"
    

class UserManager:
    def __init__(self):
        self.user=[]

    def add_user(self,user):
        self.user.append(user)

    def li_user(self):
        for i in self.user:
            print(i) #User 객체를 출력하기 때문에, User클래스에 __str__이 있어야함

    def delete_user(self, user_id):
        #리스트에 세명 회원(self.user=[user1,user2,user3])
        #i-> user1 , user2, user3
        self.user=[i for i in self.user if i.id!=user_id]

    def find_user(self,user_id):
        #self.user=[user1,user2,user3]
        for i in self.user:
            if user_id==i.id:
                return i
        return None


#객체 세개 생성하기
user1=User(1,"홍길동","hong@aa.com")
user2=User(2,"김길동","kim@aa.com")
user3=User(3,"이길동","lee@aa.com")

#UserManager 객체 한개 생성
manager=UserManager()
manager.add_user(user1) #self.user=[user1,user2,user3]
manager.add_user(user2)
manager.add_user(user3)

#li_user함수호출
manager.li_user()
print("===================")

manager.delete_user(1)
manager.li_user()

#상속:부모클래스에 있는 함수, 변수에 직접 접근하고플때는 상속 클래스 형태로 만들어야함
a=manager.find_user(2)
print("찾는 사람 : ")
if a: #return None -> false
    print(a)
else:
    print('id에 맞는 user가 없음')

