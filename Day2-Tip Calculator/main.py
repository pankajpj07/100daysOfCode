print("Welcome to Tip Calculalor!")

bill = float(input("What was your total bill?\n$"))

tip_percentage = int(input("What percentage you want to give as a tip (10,12 or 15)?\n"))

people = int(input("How many people to split the bill?\n"))


total_tip = tip_percentage/100*bill
total_bill = round(bill+total_tip,2)

bill_per_person= total_tip/people

print("Thanks for paying $", total_tip, "tip")

print("Your total bill is $",total_bill+total_tip)

print("Each person have to pay $",bill_per_person)

