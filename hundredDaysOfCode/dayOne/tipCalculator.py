# print("Welcome to the tip calculator\n")
# totalBill = input("What is your total bill? ")
# print("What percentage tip would you like to give")
# tip = input("What percentage tip would you like to give")
# tipPErcentage = tip / 100
# billSplit = input("How many people are splitting the bill")
# eachPErsonPays = totalBill / billSplit
# print(f"each person pays R{eachPErsonPays}")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? R"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
print(f"the bill with tip is {bill_with_tip}")
bill_per_person = bill_with_tip  / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay R{final_amount}")
