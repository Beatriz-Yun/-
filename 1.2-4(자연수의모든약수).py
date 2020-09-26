N=int(input('자연수 N : '))
while N<=0:
    print(N,'은(는) 자연수가 아닙니다.')
    N=int(input('자연수 N : '))
print(N, '의 모든 자연수 :', end=' ')
i=1
while i<=N/2:
    if N%i==0: print(i,end=' ')
    i+=1
print(N, end=' ')