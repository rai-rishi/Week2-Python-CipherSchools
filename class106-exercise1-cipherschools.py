def common_element(list1,list2):
    list=[]
    for a in list1:
        for b in list2:
            if a==b:
                list.append(a)
    return list
list1=eval(input("Enter  list1: "))
list2=eval(input("Enter list2: "))
print(common_element(list1,list2))