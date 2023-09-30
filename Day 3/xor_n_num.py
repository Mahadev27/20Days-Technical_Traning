n=int(input('Enter a number:'))
x=0
'''for i in range(1,n+1):
    x^=i
print(x)'''
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)