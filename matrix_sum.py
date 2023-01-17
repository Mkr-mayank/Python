m1=[]
m2=[]
sum=[]
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
print("Enter elements in matrix 1: ")
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input())
        l1.append(x)
    m1.append(l1)
print("Enter elements in matrix 2: ")
for i in range(r):
    l1=[]
    for j in range(c):
        y=int(input())
        l1.append(y)
    m2.append(l1)
print("Matrix 1: ",m1)
print("Matrix 2: ",m2)
for i in range(r):
    l1=[]
    for j in range(c):
        s=m1[i][j]+m2[i][j]
        l1.append(s)
    sum.append(l1)
print("Sum of matrix 1 and matrix 2 is: ")
for i in range(r):
    for j in range(c):
        print(sum[i][j],end=' ')
    print()