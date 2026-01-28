sub1 = float(input("Enter marks for subject 1 : "))
sub2 = float(input("Enter marks for subject 2 : "))
sub3 = float(input("Enter marks for subject 3 : "))


def total_and_avg():
    total = sub1 + sub2 + sub3
    avg = total / 3
    print(f"The total is {total}.")
    print(f"The average is {avg}.")


total_and_avg()
