print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?: "))
tip = int (input("How much tip would you like to give, 10, 12 or 15?: "))
people_number = int (input("How many people to split the bill?: "))
tip_amount = total_bill * (tip / 100)
final_bill = total_bill + tip_amount
pay_per_person = (final_bill / people_number)
print(f"Each person should pay ${pay_per_person:.2f}")