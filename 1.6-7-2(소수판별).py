a=int(input('a='))
isPrime=True
i=2
while i<=a/2:
    if a%i==0: isPrime=False
    i+=1
if isPrime==True:
    print(a,'은(는) 소수입니다.')
else : print(a,'은(는) 소수가 아닙니다.')