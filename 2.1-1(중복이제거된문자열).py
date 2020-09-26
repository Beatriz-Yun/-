def delDup(x):
    a=''
    for i in range(len(x)):
        if a.count(x[i])==0:
            a+=x[i]
    return a

s=input('s=')
print('중복이 제거된 문자열 :',delDup(s))