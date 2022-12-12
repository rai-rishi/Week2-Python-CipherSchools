def rev_list(list):
    list1=[]
    for a in list:
        list1.append(a[::-1])
    return list1
list=eval(input("Enter a list of strings: "))
print(rev_list(list))
        