n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

def mini_calci() :
    
    add = n1 + n2
    sub = n1 - n2
    multiply = n1 * n2
    devide = n1 / n2

    print(f"The addition of n1 = {n1} and n2 = {n2} is {add}")
    print(f"The substraction of n1 = {n1} and n2 = {n2} is {sub}")
    print(f"The multiplication of n1 = {n1} and n2 = {n2} is {multiply}")
    print(f"The devision of n1 = {n1} and n2 = {n2} is {devide}")


mini_calci()

