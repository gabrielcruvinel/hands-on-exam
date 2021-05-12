def palindrome():
    string = input("Enter one string: \n")
    treated_string = string.replace(" ", "").lower()

    if treated_string == treated_string[::-1]:
        print("This string are a palindrome")
    else:
        print("This string is not a palindrome")

palindrome()