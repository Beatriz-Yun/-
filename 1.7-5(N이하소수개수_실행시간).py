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
s=0
for i in range(N+1):
    if a[i]!=0: s+=1
end=time.time()-start

print(s,'개의 소수발견')
print('\n실행시간 :',end)