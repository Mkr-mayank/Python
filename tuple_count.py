t1=(2,4,6,7,4,8,4)
count=0
ele=int(input("Enter the element to be count: "))
for i in t1:
    if(i==ele):
        count=count+1
print("No of times ",ele,"present is",count)