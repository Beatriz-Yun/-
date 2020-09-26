def makeList(x):
    a=x.split(' ')
    return a

file=open('input.txt')
text=file.readline()
A=[]
A.extend(makeList(text))
for i in range(6):
    text = file.readline()
    A.extend(makeList(text))
print(A)