login_state=False

def login(func):
    def wrapper():
        if not login_state:
            print('로그인')
            return
        return func()
    return wrapper

@login  #데코레이터함수 #login(wriet_post)
def write_post():
    print('글 작성 완료')

write_post()    #로그인
login_state=True    #return func()
write_post()    #글 작성 완료

#write_post 함수에 @login 데코레이터를 적용시킴 -> wrapper()실행됨


