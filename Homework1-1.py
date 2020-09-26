def evalTerm(a, x, e):
    if e==0 and x==0 :
        return a
    else:
        res = x
        for i in range(e-1):
            res*=x
        A=res*a
        return A


a = int(input('계수 a = '))
x = int(input('x = '))
e = int(input('지수 e = '))

print('계산결과 :',evalTerm(a,x,e))