nums=[1,2,3,4,5,6,7,8]

#짝수만 출력-filter/lambda
evens=list(filter(lambda x:x%2==0, nums))
print(evens)

#제곱해서 출력- map/lambda
squre=list(map(lambda x:x**2, nums))
print(squre)