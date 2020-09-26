a=int(input('자연수 a 입력 : '))
b=int(input('자연수 b 입력 : '))
c=int(input('자연수 c 입력 : '))
_a=a
_b=b
_c=c
while _a!=_b:
    if _a<_b: _a+=a
    else : _b+=b
_b=_b
while _b!=_c:
    if _b<_c: _b+=b
    else : _c+=c
while _a!=_c:
    if _a<_c: _a+=a
    else : _c+=c
print('자연수 a와 b와 c의 최소공배수 :',_a)