def stringSearch(t,p):
    i=0
    j=0
    N=len(t)
    M=len(p)
    while i<N and j<M:
        if t[i]!=p[j]:
            i-=j
            j=-1
        i+=1
        j+=1
    if j==M:
        return i-M
    else:
        return i

file=open('input.txt')
text=file.read()
print('텍스트 :',text)
pattern=input('패턴 입력 :')
if stringSearch(text,pattern)==len(text):
    print('패턴을 발견하지 못함.')
else:
    print('처음 발견한 위치 :',stringSearch(text,pattern))