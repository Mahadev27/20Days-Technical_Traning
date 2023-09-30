n=int(input())
k=int(input())
if n&1<<k-1 ==0:
    print("Not set")
else:
    print("Set")