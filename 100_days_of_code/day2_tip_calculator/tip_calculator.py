print("Welcome to the tip calculator !")

total_bill_amount = float(input("What was the total bill?\n"))
percentage_tip = int(input("How much tip would you like to give? 10, 12 or 15? \n"))
split_number = int(input("How many people will split the bill?\n"))

pay_per_person = ((total_bill_amount*(1+percentage_tip/100))/split_number)
pay_per_person = round(pay_per_person, 2)

print(f"Each person should pay {pay_per_person}")