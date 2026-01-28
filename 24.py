def swap(a, b):

    print(f"Before swap a = {a} and b = {b}.")
    temp = a
    a = b
    b = temp
    print(f"After swap a = {a} and b = {b}.")


a = input("Enter first value : ")
b = input("Enter second value : ")


swap(a, b)
