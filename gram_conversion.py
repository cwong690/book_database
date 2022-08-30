"""
A program that takes user input gram value and convert to kilogram, pound and ounce
"""

# import library to create the GUI
from tkinter import *

# Creating tkinter empty window
window = Tk()

# Function for calculating values
def from_g():
    # Gets user input and convert to kilogram, pounds and ounces
    kgram = float(e1_value.get())*1000
    pound = float(e1_value.get())*2.20462
    ounce = float(e1_value.get())*35.274

    # Adds created values to a text box, removing previous text if present
    t1.delete("1.0", END)
    t1.insert(END, kgram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

# Create label widget for what number users will be inputting and what the outputs represent
l1 = Label(window, text="Gram")
l1.grid(row=0, column=0)
l2 = Label(window, text="Kilogram")
l2.grid(row=2, column=0)
l3 = Label(window, text="Pound")
l3.grid(row=2, column=1)
l4 = Label(window, text="Ounce")
l4.grid(row=2, column=2)

# Create StringVar object to store value from entry box for user input
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Create button widget for conversion function to be called
b1 = Button(window, text="Convert", command=from_g)
b1.grid(row=0, column=2)

# Create empty text boxes for output values
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

# Keeps main window open until manual closure
window.mainloop()