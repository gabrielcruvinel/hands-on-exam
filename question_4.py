def sort_array():
    print("*************** -> Sort Array <- ***************\n")


    number_array = []
    aux = 0
    while aux != '0':
        number_input = input("type the numbers to create the array or press [0] to finish the execution: ")
        aux = number_input 
        number_input = int(number_input)
        number_array.append(number_input)

    number_array.sort(reverse=True)
    print(number_array)
sort_array()