import time
N=int(input('자연수 N 입력 :'))
start=time.time()
s=0
for i in range(1,N*N+1):
    s=s+i
end=time.time()-start
print('합계 :',s)
print('실행시간:',end)
