def Linear_search(a):
    s=int(input('Enter the search element:'))
    n=len(a)
    found=0
    for i in range(n):
        if s==a[i]:
            found=1
    if found==1:
        return 'Element is Found' 
    else:
        return 'Element is not Found'
arr=list(map(int,input('Enter a array:').split()))
print(Linear_search(arr))