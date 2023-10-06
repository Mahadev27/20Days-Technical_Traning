n=int(input("Enter the size of matrix:"))
r,c=0,n//2
matrix =[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(0)
    matrix.append(a)
for i in range(1,n**2+1):
    matrix[r][c]=i
    nr,nc=(r-1)%n,(c+1)%n
    if matrix[nr][nc]!=0:
        r=(r+1)%n
    else:
        r,c=nr,nc
print("The Magical matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
print()
matrix1=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(0)
    matrix1.append(a)
for _ in range(n+1):
    for i in range(n):
        for j in range(n-1,-1,-1):
            matrix1[i][j]=matrix[j][i]
    for i in range(n):
        for j in range(n):
            print(matrix1[i][j],end=" ")
        print()
    print()