import pickle
import os
from datetime import datetime

#데이터를 저장할 파일
DATA_FILE = "todo_data.pkl"

#User 회원정보
class User:
    def __init__(self, username, password, role="user"):
        self.username = username    #사용자 아이디
        self.password = password    #사용자 비밀번호
        self.role = role  # 권한 user or admin

#Task 할일정보
class Task:
    def __init__(self, title, owner, priority):
        self.title = title  #할 일 제목
        self.owner = owner  #작성자
        self.priority = priority  #우선순위 1(높음) 2(보통) 3(낮음)
        self.status = "진행중"  #초기 상태는 징행중
        self.created_at = datetime.now()    #생성된 날짜와 시간 자동으로 기록

    def complete(self):
        self.status = "완료"    #호출 시 상태를 완료 로 변경


class TodoSystem:
    def __init__(self):
        self.users = []
        self.tasks = []
        self.current_user = None    #세션 변수
        self.load_data()

   
    def save_data(self):
        with open(DATA_FILE, "wb") as f:
            pickle.dump((self.users, self.tasks), f)    #두 리스트를 튜플 묶음으로 저장

    def load_data(self):
        if os.path.exists(DATA_FILE):   #파일이 있을때문 읽기 시도
            with open(DATA_FILE, "rb") as f:
                self.users, self.tasks = pickle.load(f) #튜플을 각각의 리스트로 복원

   
    def register(self):
        username = input("아이디: ")
        password = input("비밀번호: ")
        self.users.append(User(username, password)) #아이디,비밀번호 self.users 리스트에 추가
        print("회원가입 완료")
        self.save_data()    #가입 후 파일 저장

    def login(self):
        username = input("아이디: ")
        password = input("비밀번호: ")

        for user in self.users: #회원 목록에 한명식 검사
            if user.username == username and user.password == password:
                self.current_user = user    #로그인한 유저 정보로 세션 유지 역할
                print("로그인 성공")
                return
        print("로그인 실패")

    
    def add_task(self):
        title = input("할 일 제목: ")
        priority = int(input("우선순위 (1높음,2보통,3낮음): "))
        task = Task(title, self.current_user.username, priority)    #(위치인자)__init__(self, title, owner, priority): 사용자 아이디를 작성자(owner)로 지정
        self.tasks.append(task) #전체 할 일 리스트에 추가
        print("할 일 등록 완료")
        self.save_data()    #추가 후 파일 저장

    def show_tasks(self):
        print("\n--- 내 할 일 목록 ---")
        for i, task in enumerate(self.tasks):   #전체 목록을 순서(i)와 함께 하나씩 꺼내기
            if task.owner == self.current_user.username:    #자신의 할일만 출력
                print(f"{i}. [{task.status}] {task.title} (우선순위:{task.priority})")

    def complete_task(self):
        self.show_tasks()   #할일 목록 화면 출력
        idx = int(input("완료할 번호 선택: "))
        self.tasks[idx].complete()  #전체 리스트중 해당 인덱스 방에 있는 할 일을 완료 상태로 변경
        print("완료 처리됨")
        self.save_data()

    # ---관리자 기능 --
    def show_statistics(self):
        total = len(self.tasks) #전체 유저의 할 일 개수
        completed = len([t for t in self.tasks if t.status == "완료"])  #전체 중 완료인것만 개수
        print(f"총 할 일: {total}")
        print(f"완료된 할 일: {completed}")

    def run(self):
        while True:
            print("\n1.회원가입 2.로그인 3.종료")
            choice = input("선택>> ")

            if choice == "1":
                self.register() #1번 회원가입
            elif choice == "2":
                self.login()    #2번 로그인
                if self.current_user:   #세션에 유저가 등록되면
                    self.user_menu()    #회원 메뉴로 이동
            elif choice == "3": #종료
                break

    def user_menu(self):
        while True:
            print("\n1.할일등록 2.목록보기 3.완료처리 4.통계 5.로그아웃")
            choice = input("선택>> ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_tasks()
            elif choice == "3":
                self.complete_task()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.current_user = None    #로그아웃 시 세션 비우기
                break   #종료하여 1차 화면으로 돌아감


if __name__ == "__main__":
    system = TodoSystem()   #시스템 객체 생성(파일 데이터 로드됨)

    # 기본 관리자 계정 생성_ admin 계정이 없다면 admin계정 생성 후 파일에 저장
    if not any(u.role == "admin" for u in system.users):
        system.users.append(User("admin", "1234", "admin"))
        system.save_data()

    system.run()    #메인 메뉴 표출





