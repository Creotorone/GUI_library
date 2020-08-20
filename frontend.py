"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close 

"""
import backend
from tkinter import *


def view_command():
    list_box.delete(0, END)

    for row in backend.view():
        list_box.insert(END, row)


window = Tk()

title_lab = Label(window, text="Title")
title_lab.grid(row=0, column=0)
title_value = StringVar()
entry_title = Entry(window, textvariable=title_value)
entry_title.grid(row=0, column=1)

year_lab = Label(window, text="Year")
year_lab.grid(row=1, column=0)
year_value = StringVar()
year_entry = Entry(window, textvariable=year_value)
year_entry.grid(row=1, column=1)

auth_lab = Label(window, text="Author")
auth_lab.grid(row=0, column=2)
auth_value = StringVar()
auth_entry = Entry(window, textvariable=auth_value)
auth_entry.grid(row=0, column=3)

isbn_lab = Label(window, text="ISBN")
isbn_lab.grid(row=1, column=2)
isbn_value = StringVar()
isbn_entry = Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=1, column=3)

view_button = Button(window, text="View all", command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry")
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update")
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete")
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close")
close_button.grid(row=7, column=3)

list_box = Listbox(window, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_box.yview)

window.mainloop()

