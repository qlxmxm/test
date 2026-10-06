import json


class User:
    def __init__(self, user_id, password, user_name, is_admin=False):
        self.user_id = user_id
        self.password = password
        self.user_name = user_name
        self.is_admin = is_admin


class UserManager:

    def __init__(self):
        self.users = []
        self.file_path = "[회의실_예약_시스템_MVP]/users.json"

        self.load_users()

    def register(self):
        print("\n===== 회원가입 =====")

        user_id = input("아이디 : ")

        # 아이디 중복 확인
        for user in self.users:
            if user.user_id == user_id:
                print("이미 사용 중인 아이디입니다.")
                return

        password = input("비밀번호 : ")
        user_name = input("이름 : ")

        user = User(user_id, password, user_name)

        self.users.append(user)

        self.save_users()

        print("회원가입이 완료되었습니다.")

    def save_users(self):
        data = []

        for user in self.users:
            data.append({
                "user_id": user.user_id,
                "password": user.password,
                "user_name": user.user_name,
                "is_admin": user.is_admin
            })

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_users(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for user_data in data:
                user = User(
                    user_data["user_id"],
                    user_data["password"],
                    user_data["user_name"],
                    user_data["is_admin"]
                )

                self.users.append(user)

        except FileNotFoundError:
            pass

    def login(self):
        print("\n===== 로그인 =====")

        user_id = input("아이디 : ")
        password = input("비밀번호 : ")

        for user in self.users:
            if user.user_id == user_id and user.password == password:
                print(f"{user.user_name}님 로그인되었습니다.")
                return user

        print("아이디 또는 비밀번호가 잘못되었습니다.")
        return None