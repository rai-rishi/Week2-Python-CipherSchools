def func(list):
    evennum=[]
    oddnum=[]
    list1=[]
    for a in list:
        if a%2==0:
            evennum.append(a)
        else:
            oddnum.append(a)
    list1.append(evennum)
    list1.append(oddnum)
    return list1
list=eval(input("Enter a list: "))
print(func(list))
    