'''Write a program to take any four digit integer numbers. Then separate each digit from the number and the process will stop when the
digit is lesser than or equal to 1. The number must contain 1 in any places except the unit place. Once the loop will break display the
digits and sum of all the digit printed.'''
n=int(input("Enter any 4 digit number: "))
sum=0
print("The digits are: ")
while(n>0):
    r=n%10
    n=n//10
    if(r<=1):
        break
    print(r,end=' ')
    sum=sum+r
print("\nThe sum of digits=",sum)

