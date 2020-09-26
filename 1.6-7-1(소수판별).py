def isPrime(x):
    i=1
    s=0
    while i<=x/2:
        if x%i==0:
            s+=i
        i+=1
    if s==1: return True

a=int(input('a='))
if isPrime(a): print(a,'은(는) 소수입니다.')
else : print(a,'은(는) 소수가 아닙니다.')