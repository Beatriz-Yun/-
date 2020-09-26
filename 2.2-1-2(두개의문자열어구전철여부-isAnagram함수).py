def preprocessing(x):
    if x.isalpha():
        x=x.lower()
        return x
    else:
        a=x.lower()
        s=''
        for i in range(len(a)):
            if a[i].isalpha():
                s+=a[i]
        return s

def isAnagram(s1,s2):
    s1=preprocessing(s1)
    s2=preprocessing(s2)
    n1=len(s1)
    n2=len(s2)
    if n1!=n2: return False
    else:
        A=list(s1)
        B=list(s2)
        A.sort()
        B.sort()
        if A==B: return True
        else : return False

a=input('첫 번째 문자열 입력 :')
b=input('두 번째 문자열 입력 :')
if isAnagram(a,b): print('어구전철입니다.')
else : print('어구전철이 아닙니다.')