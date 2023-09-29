def fibonacci_series(n):
    if n<=1:
        return n
    return (fibonacci_series(n-1)+fibonacci_series(n-2))
n=5
for i in range(n):
    print(fibonacci_series(i),end=" ")
    