n1=int(input('Enter a number:'))
n2=int(input('Enter a number:'))
x=0
y=0
if n1%4==0:
    x=n1
elif n1%4==1:
    x=1
elif n1%4==2:
    x=n1+1
elif n1%4==3:
    x=0
elif n2%4==0:
    y=n2
elif n2%4==1:
    y=1
elif n2%4==2:
    y=n2+1
elif n2%4==3:
    y=0
res=x^y
print(res)