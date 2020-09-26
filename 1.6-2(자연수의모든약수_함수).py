def isDivision(m,n):
    if m%n==0:return True

a=int(input('a='))
for i in range(1,a+1):
    if isDivision(a,i) : print(i,end=' ')