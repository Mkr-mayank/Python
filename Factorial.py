n=int(input("Enter a number: "))
fac=1
for i in range(1,n+1):
    fac=fac*i
print("The factorial of %d is %d"%(n,fac))