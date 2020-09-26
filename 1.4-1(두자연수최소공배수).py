a=int(input('자연수 a 입력: '))
b=int(input('자연수 b 입력: '))
_a=a
_b=b
while _a!=_b:
    if _a<_b: _a+=a
    else : _b+=b
print('a와 b의 최소공배수 :',_a)