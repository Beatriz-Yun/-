def sum_avg(x,y,z):
    global A
    A=x+y+z
    global B
    B=A/3

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))

sum_avg(a,b,c)
print('합 :',A)
print('평균 :',B)