N=int(input('자연수 N 입력 : '))
a=list(range(0,N+1))
s=0
for i in range(1,N):
    if N>=2**i-1:
        s=i
i=1
while i<=s:
    A=a[2**(i-1):2**i]
    for n in range(len(A)-1):
        print(A[n],end=' ')
    print(A[len(A)-1])
    i+=1

B=a[2**s:]
for n in range((len(B))):
    print(B[n],end=' ')