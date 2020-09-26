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


a=input('문자열 입력: ')
a=preprocessing(a)
print('변환된 문자열 :',a)