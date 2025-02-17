# inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit

# Output
# Total amoung you have to pay is:

rent = int (input("Enter your flat rent:"))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Person living in flat: "))

total_bill = electricity_spend*charge_per_unit
Total_amount = rent + food + total_bill
each_person_bill = Total_amount / persons
print(f"the total bill is: {Total_amount}")
print(f'Each person will pay: {each_person_bill}')
