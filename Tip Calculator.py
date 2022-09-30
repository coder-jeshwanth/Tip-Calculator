#1 Granting a Customer
print("Welcome to TIP calculator!")

#2 Input the total bill amount
bill = float(input("What was the Total Bill? ₹"))

#3 Input the percentage of TIP
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))

#4 Calculate the percentage
tip_as_percent = tip / 100

#5 Calculating the total TIP amount
total_tip_amount = bill * tip_as_percent

#6 Input the number of people
people = int(input("How many people to split the bill? "))

#7 ADD Bill and total TIP amount
total_bill = bill + total_tip_amount

#8 Divide the bill
bill_per_person = total_bill / people

#9 Modify the output using ROUND function
final_amount =  round(bill_per_person, 2)

#10 Convert float to string
final_amount = "{:.2f}".format(bill_per_person)

#11 Output the final amount
print(f"Each person should pay ₹{final_amount} ")