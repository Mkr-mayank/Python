dict={"Himanshu":{"Maths":92,"Computer":96,"Economics":90},"Suraj":{"Maths":83,"Computer":92,"Economics":91},"Mahesh":{"Maths":86,"Computer":98,"Economics":88}}
dict_avg={}
sum=0
for name,sub in dict.items():
    for marks in sub.values():
        sum=sum+marks
    avg=sum/3
    dict_avg[name]=avg
    sum=0
print(dict)
print(dict_avg)
high=max(dict_avg.values())
for name,marks in dict_avg.items():
    if(marks==high):
        print(name)
