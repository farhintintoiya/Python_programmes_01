def net_salary(gross):

    allowance = 0.10 * gross     # 10% allowance
    deduction = 0.03 * gross     # 3% deduction
    net_salary = gross + allowance - deduction
    print(f"The net sallary is {net_salary}.")


gross = float(input("Enter gross salary: "))


net_salary(gross)
