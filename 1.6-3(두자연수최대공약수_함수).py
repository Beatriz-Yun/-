def gcd(m,n):
    if m<n: m,n=n,m
    for i in range(1,n+1):
        if m%i==0 and n%i==0 : gcd=i
    return gcd

a=int(input('a='))
b=int(input('b='))

print('a,b의 최대공약수 :',gcd(a,b))