
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in Kg: "))

bmi=round(weight/height**2)
if bmi <18.5:
    print(f"Your bmi is {bmi}, your underweight.")
elif bmi <25:
    print(f"your bmi is {bmi}, you have normal weight.")
elif bmi <30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi <35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")