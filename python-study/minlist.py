list1=[9,3,8,5,1,12,11]
list2=[] #新建一个列表
for i in range(0,len(list1)):  #找最小值的次数
            list2.append(min(list1))
            list1.remove(min(list1))
print(list2)