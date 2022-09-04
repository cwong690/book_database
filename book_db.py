"""
Create program that stores book information such as Title, Author, Year and ISBN
Allows users to view all records, search/add/update entry, delete and close
"""

from tkinter import *
from backend import *

# Create functions that can be inputted into the buttons command. This ensures the command won't run until buttons are pressed
def get_selected_row(event):
    # Grabs index of selected tuple and creates global variable to be used by delete_command
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    # Populates entry boxes with selected values
    for k, v in zip([e1,e2,e3,e4], selected_tuple[1:]):
        k.delete(0,END)
        k.insert(END, v)

def view_command():
    list1.delete(0,END)
    for row in view():
        list1.insert(END,row)

def search_command():
    # receives parameters from the entry buttons StringVars
    list1.delete(0, END)
    for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    # receives parameters from the entry buttons StringVars
    add_entry(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# def update_command():


def delete_command():
    delete(selected_tuple[0])
    view_command()

window=Tk()

# Create labels for entry boxes
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Create entry boxes
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Create list box
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create scrollbar then configure to listbox
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Binds listbox to select action and this event triggers the get_selected_row function
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create buttons
b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)
b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)
b4=Button(window, text="Update", width=12)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6=Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()