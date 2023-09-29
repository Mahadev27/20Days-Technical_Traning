a=list(map(int,input("Enter the array:").split()))
n=len(a)
lower_limit=int(input("Enter lower limit:"))
higher_limit=int(input("Enter higher limit:"))
even_num=[]
power=[]
for i in range(n):
    if a[i]>=lower_limit and a[i]<=higher_limit:
        if a[i]%2==0:
            even_num.append(a[i])
        if a[i] & (a[i]-1)==0:
            power.append(a[i])
print(even_num)
print(power)
        