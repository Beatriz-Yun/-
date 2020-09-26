def isPalindrome(s):
    j=len(s)-1
    i=0
    while i<j:
        if s[i]!=s[j]:return False
        j-=1
        i+=1
    return True

a=input('문자열 입력: ')
if isPalindrome(a): print('회문입니다.')
else: print('회문이 아닙니다.')