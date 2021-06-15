print("welcome to the tip calculator!")

bill = float(input("what is the total bill? "))

tip = int(input("how much tip would you like to give 10, 12 or 15? "))

people = int(input("how many people to split the bill? "))

tip_amount = (tip / 100) * bill

total_tip_amount = tip_amount + bill

bill_per_person = total_tip_amount / people

final_amount = round(bill_per_person,2)

print(f"each person should pay ${final_amount}")