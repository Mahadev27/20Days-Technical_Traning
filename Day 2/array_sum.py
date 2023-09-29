def sum_of_array(a):
    sum=0
    for i in a:
        sum+=i
    return sum
arr=list(map(int,input('Enter a array:').split()))
print(sum_of_array(arr))