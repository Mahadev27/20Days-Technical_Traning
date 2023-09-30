n=int(input("Enter length of array:"))
arr=[]
for i in range(n):
    a=int(input())
    if a>=0:
        arr.append(a)
miss = 0
while miss in arr:
    miss+= 1
print(miss)
