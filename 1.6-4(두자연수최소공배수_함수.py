def lcm(m,n):
    _m=m
    _n=n
    while _m!=_n:
        if _m<_n:
            _m+=m
        if _m>_n:
            _n+=n
    return _m

a=int(input('a='))
b=int(input('b='))
print('a,b의 최소공배수 :',lcm(a,b))