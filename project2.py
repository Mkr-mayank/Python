list=[]
newlist=[]
sum=0
print("Enter 6 elements in the list: ")
for i in range(0,6):
  x=int(input())
  list.append(x)
print("The required list is: ",list)
for i in range(0,6):
  if(list[i]%2==0):
     list[i]=list[i]+3
     newlist.append(list[i])
  else:
     list[i]=list[i]-1
     newlist.append(list[i])
print("Modified list is ",newlist)
print("Odd elements in modified list are: ",end=' ')
for i in range(0,6):
  if(newlist[i]%2==0):
    sum=sum+newlist[i]
  else:
    print(newlist[i], end=' ')
print("\nSum of even elements = ",sum)