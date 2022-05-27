print("Welcome to pizza deliveries!")
size=input("Select the size you want to order? S, M, or L")
extra_pepper=input("Do you want pepperoni? Y or N")
cheese=input("Do you want extra cheese? Y or N")

total_bill=0
if size =="S":
    total_bill +=15
elif size=="M":
    total_bill +=20
else:
    total_bill+=25

    
if extra_pepper=="Y":
    if size=="S":
        total_bill +=2
    else:
        total_bill +=3
        
if cheese=="Y":
    total_bill +=1

print(f"Your final bill is ${total_bill}")