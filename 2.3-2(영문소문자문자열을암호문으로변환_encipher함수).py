def encipher(p):
    P=list(p)
    x=''
    for i in range(len(P)):
        A=ord(P[i])
        if A==32:#스페이스를 96으로(계산편의를 위해)
            A=96
        t=A+K
        if t>122:#아스키코드가 z를 넘어갈 경우
            t=t-27
        if t==96:#아스키코드가 96이면 스페이스로 출력
            t=32
        x+=chr(t)
    return x

a=input('평문 입력 :')
K=int(input('K값 입력(1~26) :'))
print('암호문 출력 :[',end='')
print(encipher(a),end='')
print(']')
