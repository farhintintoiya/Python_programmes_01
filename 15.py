degF = float(input("Enter the temperature in fahrenheit : "))

def f2c() :
    
    C = 5/9 * (degF - 32)
    print(f"The {degF} fahrenheit is {C} in celcius")


f2c()