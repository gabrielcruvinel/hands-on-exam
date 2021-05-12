def fibonacci_series():
    next = 0
    previous = 0
    print("****************** FIBONACCI SERIES *******************\n\n")
    number = int(input("Enter the number where the fibonnaci sequence will stop: "))
    while (next <= number):   
        print(next)
        next = next + previous
        previous = next - previous

        if(next == 0):
            next = next + 1

fibonacci_series()