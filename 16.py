P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate of Interest (R): "))
N = float(input("Enter Time (N): "))

def simple_interest():
    SI = (P * R * N) / 100
    print(f"The Simple Interest is {SI}")

simple_interest()
