N=int(input('자연수 입력 : '))
i=1
s=0
while i<=N/2:
    if N%i==0:
        s+=i
    i+=1
if s==N:
    print('완전수 입니다.')
else : print('완전수가 아닙니다.')