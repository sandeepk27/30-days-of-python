from tkinter import *
import tkinter.font as font


root=Tk()
root.geometry("400x460")
root.title("Calculator")
root.resizable(0, 0)

# Creating a StringVar to take
input=StringVar ()
myFont=font. Font(size=15)


#C reating an Entry widget to get the
screen=Entry(root, text=input, width=30,justify='right', font=(10), bd=4)

# we will usergrid like structure
screen.grid(row=0, columnspan=4, padx=15,pady=15, ipady=5)

#Key matrix contains all the required the keys
key_matrix =[["c", u"\u221A", "/", "<-"],
            ["7", "8", "9", "*"],
            ["4", "5", "6","-"],
            ["1", "2", "3","+"],
            ["!", "0", ".", "-"]]

#Creating a dictionary for the buttons
btn_dict={}

#Variable to store our results
ans_to_print=0

#Defining the function for calculation
def Calculate(event):
    
    #getting the name of the button clicked
    button=event.widget.get("text")
    #Referring the global values
    global key_matrix, input, ans_to_print
    
    try:
        # Event contain a sqrt operation
        if button == u"\u221A":
            ans=float(input.get())**(0.5)
            ans_to_print=str(ans)
            input.set(str(ans))
            
        elif button=="c":# Clear Button
            input.set("")
                    
        elif button == "!": #Factorial !
            def fact(n): return 1 if n==0 else n*fact(n-1)
            input.set(str(fact(int(input.get()))))
            
        elif button-"-": #Backspace
            input.set(input.get()[:len(input.get())-1])
        elif button=="-": #Showing The Results
            #Calculating the mathematical exp. using eval
            ans_to_print=str(eval(input.get()))
        # You may add many more operations
        else:
        # Displaying the digit pressed on screen
            input.set(input.get()+str(button))
    except:
        # In case invalid syntax given in expression
        input.set("wrong Operation")
# Number of rows containing buttons
for i in range(len(key_matrix)):
    # Number of columns
    for j in range(len(key_matrix[i])):
        
        # Creating and Adding the buttons to dictionary
        btn_dict["btn_"+str(key_matrix[i][j])]=Button(
        root, bd=1, text=str(key_matrix[i][j]), font=myFont)
        # Positioning buttons
        btn_dict["btn_"+str(key_matrix[i][j])].grid(
        row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
        # Assigning an action to the buttons
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate)

# Running the main loop
root.mainloop()
