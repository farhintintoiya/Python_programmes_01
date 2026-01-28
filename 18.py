def rectangle(L, B):
    A = L * B            # Area
    P = 2 * (L + B)      # Perimeter
    print(f"The area of rectangle is {A}.")
    print(f"The Perimeter of rectangle is {P}.")


L = float(input("Enter the length : "))
B = float(input("Enter the Width : "))


rectangle(L, B)
