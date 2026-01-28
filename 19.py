def circle(r) :
    C = 2 * (22/7) * r # Circumference
    A = (22/7) * (r ** 2) # Area

    print(f"The Circumference of Circle is {C}.")
    print(f"The Area of Circle is {A}.")
    
r = float(input("Enter the radius : "))

circle(r)