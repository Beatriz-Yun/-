def stringSearch(t,p,i):
    j=0
    N=len(t)
    M=len(p)
    while i<N and j<M:
        if t[i]!=p[j]:
            i-=j
            j=-1
        i+=1
        j+=1
    if j==M: return i-M
    else: return i

file=open('input.txt')
text=file.read()
print('텍스트: ',text)
file.close()
pattern=input('패턴 입력 :')
i=0
while len(pattern)>0:
    l=stringSearch(text,pattern,i)
    i=l+len(pattern)
    if i<len(text):
        print('패턴을 발견한 위치 :',l)
    else: break
print('문자열 탐색 완료.')