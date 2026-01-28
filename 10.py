
def d2p(d) :
    p = d * (48/70)

    print(f"The {d} dollar is {p:.2f} in pounds")

d = float(input("Enter the dollars : "))

d2p(d)