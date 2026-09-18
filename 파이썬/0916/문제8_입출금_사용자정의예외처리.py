#사용자 정의 예외 -> 우리가 만드는 예외 -> Exception클래스를 상속받아서 만든다.
class BankError(Exception):
    pass

class InvalidBankError(BankError):
    pass

class InsufficientBankError(BankError):
    pass

class Bank:
    def __init__(self, balance=0):
        self.balance=balance

    def withdraw(self, amount):
        if amount<=0:
            raise InvalidBankError("출금액은 0보다 커야한다")  # InvalidBankError 의 __init__호출 -> Exception 의 __init__호출
       
        if amount > self.balance:
            raise InsufficientBankError("잔액이 부족하다")

        self.balance-=amount  #balance:잔고 amount:출금액
        return self.balance

#객체생성 -> 클래스명()
acc=Bank(10000) #잔액(balance) 이 10000원있음

print(acc.withdraw(3000)) #7000

try:
    acc.withdraw(30000)
except InsufficientBankError as e:
    print("출금 실패:", e)

try:
    acc.withdraw(-8000)
except BankError as e:
    print("출금 실패:", e)