print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?: $"))
amount_of_guests = float(input("How many people split the bill?: "))
tip_percentage = float(input("What percentage tip would you like to give?: %"))
pay_amount = (((100 + tip_percentage) * total_bill) / 100) / amount_of_guests
print(f"Each person should pay {round(pay_amount, 2)}$.")