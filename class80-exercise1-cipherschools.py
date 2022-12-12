# Palindrome Strings 
def get_palindrome(str1):
    rev=str1[::-1]
    if str1==rev:
        print(f"{str1} is a palindrome string")
    else:
        print(f"{str1} is not a palindrome string")
str=input("Enter a String: ")
get_palindrome(str)