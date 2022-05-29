print("Welcome to the roller coaster!")
hei=int(input("What is your height(in cm)?"))
bill =0

if hei>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age?"))
    if age <12:
        bill =5
        print("child tickets are $5.")
    elif age <=18:
        bill=7
        print("Youth tickets are $7.")
    elif age>=45 and age<=55:
        print("Everything is going to be ok. Have a free ride on us!!")
    else:
        bill=12
        print("Adult tickets are $12.")
    photo=input("Do you want a photo taken? Y or N.")
    if photo =="Y":
        bill +=3
    
    print(f"your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
    
    
    

# Age calculator


from tkinter import *
from datetime import date

# initialized window
root = Tk()
root.geometry('280x300')
root.resizable(0, 0)
root.title('Age Calculator')
statement = Label(root)

# defining the function for calculating age


def ageCalc():
    global statement
    statement.destroy()
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(
        monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year
    if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
        age -= 1
    statement = Label(text=f"{nameValue.get()}'s age is {age}.")
    statement.grid(row=6, column=1, pady=15)


# creating a label for person's name to display
l1 = Label(text="Name: ")
l1.grid(row=1, column=0)
nameValue = StringVar()

# creating a entry box for input
nameEntry = Entry(root, textvariable=nameValue)
nameEntry.grid(row=1, column=1, padx=10, pady=10)

# label for year in which user was born
l2 = Label(text="Year: ")
l2.grid(row=2, column=0)
yearValue = StringVar()
yearEntry = Entry(root, textvariable=yearValue)
yearEntry.grid(row=2, column=1, padx=10, pady=10)

# label for month in which user was born
l3 = Label(text="Month: ")
l3.grid(row=3, column=0)
monthValue = StringVar()
monthEntry = Entry(root, textvariable=monthValue)
monthEntry.grid(row=3, column=1, padx=10, pady=10)

# label for day/date on which user was born
l4 = Label(text="Day: ")
l4.grid(row=4, column=0)
dayValue = StringVar()
dayEntry = Entry(root, textvariable=dayValue)
dayEntry.grid(row=4, column=1, padx=10, pady=10)

# create a button for calculating age
button = Button(text="Calculate age", command=ageCalc)
button.grid(row=5, column=1)

# infinite loop to run program
root.mainloop()
