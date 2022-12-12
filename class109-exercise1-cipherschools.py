def check_list(l):
    count=0
    for i in l:
        if type(i) == list:
            count += 1
    return count
list1=eval(input("Enter a list of lists: "))
print(check_list(list1))