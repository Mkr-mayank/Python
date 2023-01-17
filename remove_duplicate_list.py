list=[]
newlist=[]
print("Enter 12 elements in the list: ")
for i in range(12):
    ele=int(input("Enter elements: "))
    list.append(ele)
for i in list:
    if i not in newlist:
        newlist.append(i)
print("After removing duplicate elements the required list is : ",newlist)
