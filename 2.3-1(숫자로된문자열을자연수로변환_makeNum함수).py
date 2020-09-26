def makeNum(x):
    for i in range(len(x)):
        X=list(x)
    s=0
    for i in range(len(X)):
        A=ord(X[i])-48
        B=A*10**(len(X)-i-1)
        s+=B
    return s


a=input('a = ')
b=input('b = ')
S=makeNum(a)+makeNum(b)
print('두 수의 합 :',S)