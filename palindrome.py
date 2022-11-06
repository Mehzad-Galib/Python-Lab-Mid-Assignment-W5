given_string = input("Enter string to check palindrome: ")

reverse_string = given_string[::-1]

if given_string == reverse_string:
    print('The given string is palindrome')
    
else:
    print("The given string is not palindrome")
