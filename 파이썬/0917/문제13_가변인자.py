#가변인자
def find_max(*args):
    if not args:
        return None
    else:
        return max(args)



#최대값 반환
print(find_max(3,8,2))
print(find_max(10))
print(find_max(-3,-8))
print(find_max())