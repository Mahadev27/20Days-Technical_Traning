n=int(input("Enter length of array:"))
arr=[]
for i in range(n):
    a=int(input())
    if a>=0:
        arr.append(a)
n=len(arr)
x=max(arr)
arr1=[]
c=0
miss=[]
for i in range(x+1):
    arr1.append(i)
for i in range(x):
    for j in range(n):
        if arr1[i]==arr[j]:
            c=0
            break
        else:
            c=1
    if c==1:
        miss.append(arr1[i])
min1=miss[0]
for i in range(len(miss)):
    if min1>miss[i]:
        min1=miss[i]
    else:
        min1=min1
print(min1)