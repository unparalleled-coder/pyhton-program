n= int(input())
matrix=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
s1=0
s2=0
for i in range(n):
    for j in range(n):
        if (i==j):
            s1=s1+matrix[i][j]
        if (i+j==n-1):
            s2=s2+matrix[i][j]
print(abs(s1-s2))
