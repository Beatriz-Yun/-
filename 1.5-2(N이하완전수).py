N=int(input('2보다 큰 자연수 N 입력 : '))
while N<=2:
    print('N은 2보다 큰 자연수')
    N=int(input('2보다 큰 자연수 N 입력 : '))

for r in range(3,N+1):
    i=1
    s=0
    while i<=r/2: #i<r이라고 해도 무관 but 루프횟수 차이
        if r%i==0:
            s+=i
        i+=1
    if s==r:print(r,end=' ')
