import sys

#sys.exit() : 정상종료
#sys.exit(1) : 비정상/오류 종료

def main():
    #python test3.py add 3 5
    #sys.argv=["test3.py" "add" "3" "5"]
    if len(sys.argv) < 4:
        sys.exit(1) #프로그램 종료

    op=sys.argv[1]
    a=int(sys.argv[2])
    b=int(sys.argv[3])

    if op=="add":
        print(a+b)

    elif op=="sub":
        print(a-b)

    else:
        sys.exit(1)

main()

# PS C:\Users\hi\Desktop\test2\0916> python unit0916.py add 3 5
# 8
# PS C:\Users\hi\Desktop\test2\0916> python unit0916.py sub 3 5
# -2





