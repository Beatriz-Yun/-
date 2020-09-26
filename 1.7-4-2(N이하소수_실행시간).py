import time
N=int(input('2이상의 자연수 입력 :'))
start=time.time()
a=list(range(N+1))
a[1]=0
i=2
while i<=N/2:
    j=2
    while i*j<=N and a[i]!=0:
        a[i*j]=0
        j+=1
    i+=1
for i in range(N+1):
    if a[i]!=0: print(i,end=' ')
end=time.time()-start
print('\n실행시간 :',end)