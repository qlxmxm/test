# 생성자: 이름, 초기금액
# deposit() : 입금
# withdraw() :출금
# show_balance() : 현재 잔액 보이기
# 출금 시 잔액 부족 시 "잔액이 부족하다" 출력​

# 객체 생성코드 참고
# acc1 = Account("홍길동", 10000)
# acc1.show_balance() -> 홍길동님의 현재 잔액 10000원
# acc1.deposit(5000) -> 현재 금액+5000 원 더하기
# acc1.withdraw(3000) -> 현재 금액 - 3000
# acc1.withdraw(20000) # 잔액 부족
# acc1.show_balance() -> 홍길동님의 현재 잔액 {}원

class Account:
    def __init__(self, name, money):
        self.name=name
        self.money=money
        self.balance=money

        print("이름 = {} 현재 잔역 = {}".format(name,money)) #홍길동, 10000

    def show_balance(self):
        print('{}님의 현재 잔액 {}원'.format(self.name,self.balance))

    def deposit(self, money):
        self.balance+=money        
        print('{}님의 입금 금액 {}원 잔액 {}원'.format(self.name,money,self.balance))

    def withdraw(self, money):
        if self.balance<money:
            print("잔액부족 출금 금액 {}원 현재 잔액 {}원".format(money,self.balance))
        else:
            self.balance-=money
            print('{}님의 출금 금액 {}원 잔액 {}원'.format(self.name,money,self.balance))
    
acc1 = Account("홍길동", 10000)
acc1.show_balance() #-> 홍길동님의 현재 잔액 10000원
acc1.deposit(5000) #-> 현재 금액+5000 원 더하기
acc1.withdraw(3000) #-> 현재 금액 - 3000
acc1.withdraw(20000) # 잔액 부족
acc1.show_balance() #-> 홍길동님의 현재 잔액 {}원
