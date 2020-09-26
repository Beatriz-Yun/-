N=int(input('2이상의 자연수 N 입력 : '))
def isPrime(x):
    i=1
    s=0
    while i<=x/2:
        if x%i==0:
            s+=i
        i+=1
    if s==1: return True

for i in range(2,N+1):
    if isPrime(i): print(i,end=' ')