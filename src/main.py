# A calculator using GUI by Module TKinter
from tkinter import *

# MEMORY ----> list( [ str(current_value), str(operation) ] )
list_numbs = list()

# BUTTONS FUNCTIONS
#----Operations
def add():
    list_numbs.insert(0, e.get())
    list_numbs.insert(1, "addition")
    e.delete(0, END)

def sub():
    list_numbs.insert(0, e.get())
    list_numbs.insert(1, "subtraction")
    e.delete(0, END)

def mult():
    list_numbs.insert(0, e.get())
    list_numbs.insert(1, "multiplication")
    e.delete(0, END)

def div():
    list_numbs.insert(0, e.get())
    list_numbs.insert(1, "division")
    e.delete(0, END)
#----Concatenation
def number(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(n))
#----Clear
def clear():
    e.delete(0, END)
#----Display Result
def res():
    first_number, operation = list_numbs[0], list_numbs[1]
    second_number = e.get()
    
    if operation == "addition":
        res = int(first_number) + int(second_number)
        e.delete(0, END)
        e.insert(0, res)
    elif operation == "subtraction":
        res = int(first_number) - int(second_number)
        e.delete(0, END)
        e.insert(0, res)
    elif operation == "multiplication":
        res = int(first_number) * int(second_number)
        e.delete(0, END)
        e.insert(0, res)
    elif operation == "division":
        res = int(first_number) / int(second_number)
        e.delete(0, END)
        e.insert(0, res)

# CONFIGURATION OF GUI
root = Tk()
# root.geometry("400x500")
root.title("Calculator")
root.config(bg="#434343")

# BUTTONS
#----Input of numbers
e = Entry(root, width=35, border=10)
#----Number Buttons
button_0 = Button(root,padx=40,pady=20,text="0",command=lambda: number(0))
button_1 = Button(root,padx=40,pady=20,text="1",command=lambda: number(1))
button_2 = Button(root,padx=40,pady=20,text="2",command=lambda: number(2))
button_3 = Button(root,padx=40,pady=20,text="3",command=lambda: number(3))
button_4 = Button(root,padx=40,pady=20,text="4",command=lambda: number(4))
button_5 = Button(root,padx=40,pady=20,text="5",command=lambda: number(5))
button_6 = Button(root,padx=40,pady=20,text="6",command=lambda: number(6))
button_7 = Button(root,padx=40,pady=20,text="7",command=lambda: number(7))
button_8 = Button(root,padx=40,pady=20,text="8",command=lambda: number(8))
button_9 = Button(root,padx=40,pady=20,text="9",command=lambda: number(9))
#----Clear and Result
clear = Button(root,padx=25,pady=20,text="CLEAR",command=clear)
res = Button(root,padx=39,pady=20,text="=",command=res)
#----Operations Buttons
addition = Button(root,padx=27,pady=20,text="+",command=add)
subtraction = Button(root,padx=29,pady=20,text="-",command=sub)
multiplication = Button(root,padx=29,pady=20,text="*",command=mult)
division = Button(root,padx=29,pady=20,text="/",command=div)

# DISPLAY AS GRID
"""
 DISPLAY
7   8   9   /
4   5   6   *
1   2   3   -
0   CL  =   +
"""
#----Input of numbers
e.grid(row=0, column=0, columnspan=4, padx=20, pady=10)
#----Number Buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
#----Clear and Result
clear.grid(row=4, column=1)
res.grid(row=4, column=2)
#----Operations Buttons
addition.grid(row=4, column=3)
subtraction.grid(row=3,column=3)
multiplication.grid(row=2,column=3)
division.grid(row=1,column=3)

# RUNNING PROGRAM
root.mainloop()