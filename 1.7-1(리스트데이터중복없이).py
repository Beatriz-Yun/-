a=[]
N = int(input('정수 입력 (종료시는 999):'))
while N!=999:
    N = int(input('정수 입력 (종료시는 999):'))
    if a.count(N)==0: a.append(N)
print(a)