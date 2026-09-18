class AgeError(Exception):
    pass

#나이 19세 미만이면 AgeError 오류발생 (raise) ->19세 미만은 입장할 수 없다
def check_age():
    while True:
        age=int(input("나이 입력: "))
        try:
            if age<19:
                raise AgeError("19세 미만은 입장할 수 없다") #오류나면 바로 except절로 넘어감
            print("입장 가능~")
            return age
        except AgeError as e:
            print(e)
        except ValueError:
            print("숫자만 입력해라")


result=check_age()
print(result)