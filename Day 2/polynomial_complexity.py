def generate(n):
    l=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(j)
        l.append(row)
    return l
print(generate(10))