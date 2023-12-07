# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%\n"))
total_tip = (bill * percentage_tip) / 100
total_bill = bill + total_tip
total_persons = int(input("How many people to split the bill?\n"))
contribution_of_each_person = round(total_bill / total_persons, 2)
final_amount = "{:.2f}".format(contribution_of_each_person)
print(f"Each person should pay: ${final_amount}")