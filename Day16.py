
# age calculator
age=int(input("Enter your age: "))

years_remaining= 90 - age
days_remaining = years_remaining*365
weeks_remaining =years_remaining*52
months_remaining=years_remaining*12

r=f"you have {days_remaining}days, {weeks_remaining}weeks,and{months_remaining}months"
print(r)


# Tip Calculator

print("Welcome to tip calculator!!!")
bill = float(input("Enter the bill amount here: INR "))
tip = int(input("how much would like to give? 10,12,15?"))
people=int(input("How many people to split the bill?"))

tip_percent=tip/100
total_tip=bill*tip_percent
total_bill=bill+total_tip
bill_per_person=total_bill/people
result=round(bill_per_person,2)
print(f"Each person should pay {result}INR")