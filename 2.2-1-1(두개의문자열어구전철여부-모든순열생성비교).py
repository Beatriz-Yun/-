def perm(i):
    global isAnagram
    if i==n1-1:
        if l1==l2:
            isAnagram=True
    else:
            for j in range(i,n1):
                l1[i],l1[j]=l1[j],l1[i]
                perm(i+1)
                l1[i],l1[j]=l1[j],l1[i]

def preprocessing(s):
    i=0
    j=0
    t=''
    while i<len(s):
        if s[i].isalpha():
            t+=s[i]
            i+=1
        else : i+=1
    t=t.lower()
    return t

isAnagram=False
s1=input('첫 번째 문자열 입력 :')
s2=input('두 번째 문자열 입력 :')
s1=preprocessing(s1)
s2=preprocessing(s2)
n1=len(s1)
n2=len(s2)
if n1==n2:
    l1=list(s1)
    l2=list(s2)
    perm(0)

if isAnagram:
    print('어구전철입니다.')
else:
    print('어구전철이 아닙니다.')