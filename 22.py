def net_sales(gross):
    discount = 0.10 * gross   # 10% discount
    net = gross - discount
    print(f"The net sales is {net}.")


gross = float(input("Enter Gross Sales: "))


net_sales(gross)
