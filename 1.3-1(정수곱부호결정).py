a=int(input('a='))
b=int(input('b='))
if a*b==0:
    print('0이 아닌 두 정수 a와 b를 입력하세요.')
    a = int(input('a='))
    b = int(input('b='))
if a*b>0:
    print('양수')
else: print('음수')