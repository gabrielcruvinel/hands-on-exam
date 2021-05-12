def prime_number():

    print("************* -> Prime Numbers <- ************\n")
    number = int(input("Enter a number:"))
    aux = 0

    for element in range(2, number):
        if(number% element ==0):
            aux +=1
    if aux == 0:
        print("Its a prime number")
    else:
        print("Is not a prime number")
prime_number()