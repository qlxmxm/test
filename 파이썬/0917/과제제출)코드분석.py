import pickle
import os
from datetime import datetime

#데이터를 저장할 파일
DATA_FILE = "todo_data.pkl"


class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role  # user or admin


class Task:
    def __init__(self, title, owner, priority):
        self.title = title
        self.owner = owner
        self.priority = priority  # 1(높음) 2(보통) 3(낮음)
        self.status = "진행중"
        self.created_at = datetime.now()

    def complete(self):
        self.status = "완료"


class TodoSystem:
    def __init__(self):
        self.users = []
        self.tasks = []
        self.current_user = None
        self.load_data()

   
    def save_data(self):
        with open(DATA_FILE, "wb") as f:
            pickle.dump((self.users, self.tasks), f)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "rb") as f:
                self.users, self.tasks = pickle.load(f)

   
    def register(self):
        username = input("아이디: ")
        password = input("비밀번호: ")
        self.users.append(User(username, password))
        print("회원가입 완료")
        self.save_data()

    def login(self):
        username = input("아이디: ")
        password = input("비밀번호: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print("로그인 성공")
                return
        print("로그인 실패")

    
    def add_task(self):
        title = input("할 일 제목: ")
        priority = int(input("우선순위 (1높음,2보통,3낮음): "))
        task = Task(title, self.current_user.username, priority)
        self.tasks.append(task)
        print("할 일 등록 완료")
        self.save_data()

    def show_tasks(self):
        print("\n--- 내 할 일 목록 ---")
        for i, task in enumerate(self.tasks):
            if task.owner == self.current_user.username:
                print(f"{i}. [{task.status}] {task.title} (우선순위:{task.priority})")

    def complete_task(self):
        self.show_tasks()
        idx = int(input("완료할 번호 선택: "))
        self.tasks[idx].complete()
        print("완료 처리됨")
        self.save_data()

    # ---관리자 기능 --
    def show_statistics(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == "완료"])
        print(f"총 할 일: {total}")
        print(f"완료된 할 일: {completed}")

    def run(self):
        while True:
            print("\n1.회원가입 2.로그인 3.종료")
            choice = input("선택>> ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
                if self.current_user:
                    self.user_menu()
            elif choice == "3":
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
                self.current_user = None
                break


if __name__ == "__main__":
    system = TodoSystem()

    # 기본 관리자 계정 생성
    if not any(u.role == "admin" for u in system.users):
        system.users.append(User("admin", "1234", "admin"))
        system.save_data()

    system.run()





