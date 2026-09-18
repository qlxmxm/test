#.130
pocket=['paper', 'cellphone']
card=True
if 'money' in pocket:
    print('택시 타고 가라')
else:   #pocket에 money가 없으면
    if card:
        print('택시 타고 가라')
    else:
        print('걸어가라')

pocket=['paper', 'cellphone']
card=True
if 'money' in pocket:
    pass    #다음 else로 넘어감
    print('택시 타고 가라')
elif card: #pocket에 money가 없고 card 가 true이면 (else if = elif)
    print('택시 타고 가라')
else:
    print('걸어가라')









