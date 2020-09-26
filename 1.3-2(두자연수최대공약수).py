a=int(input('a = '))
b=int(input('b = '))
i=1
while i<=a:
    if a%i==0 and b%i==0:
        s=i
    i+=1
print('a와 b의 최대공약수 : ',s)