a=list(map(int,input().split()))
c=a[0]
for i in a:
    c^=i
print(c)