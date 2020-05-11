#imports the tkinter package
from tkinter import *

#Initialises the main window
root = Tk()

#Output of Add 
#Output is given by the Label widget
def Sum():
    ans = int(e1.get()) + int(e2.get())
    L1 = Label(root, text= str(ans), padx=20)
    L1.grid(row=3, column=0)
#Output of Substract
#Output is given by the use of Label widget
def Sub():
    ans = int(e1.get()) - int(e2.get())
    L1 = Label(root, text= str(ans), padx=20)
    L1.grid(row=3, column=0)
#Output of Divide
#Output given by Lbel widget
def Div():
    ans = int(e1.get()) / int(e2.get())
    L1 = Label(root, text= str(ans), padx=20)
    L1.grid(row=3, column=0)
#Output for Multipy
#Output given by Label widget
def Prod():
    ans = int(e1.get()) * int(e2.get())
    L1 = Label(root, text= str(ans), padx=20)
    L1.grid(row=3, column=0)

#Clear the output
#Clears the output by laying a blank label over the previous labels
def Reset():
    ans = int(e1.get()) + int(e2.get())
    L1 = Label(root, padx=20)
    L1.grid(row=3, column=0)
# 1st entry
e1 = Entry(root)
e1.grid(row=1,column=0)

#2nd entry
e2 = Entry(root)
e2.grid(row=2,column=0)
# The 4 buttons are below 
b1 = Button(root,text= "Add",padx= 20, pady= 20, command = Sum)
b1.grid(row=4,column= 0)

b2 = Button(root,text= "Substract", pady= 20, command = Sub)
b2.grid(row=4, column=1)

b3 = Button(root,text = "Divide",padx=15, pady=20, command= Div)
b3.grid(row= 5, column=0) 

b4 = Button(root, text= "Multiply",padx=3, pady=20, command= Prod)
b4.grid(row=5, column=1)

b5 = Button(root, text= "Reset",padx= 17, pady=20, command= Reset)
b5.grid(row=6, column= 0)

#This is the mainloop. It keeps looping. Once the mainloop is disrupted,
#the window closes
root.mainloop()