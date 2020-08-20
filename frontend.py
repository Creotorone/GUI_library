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


def search_command():
    list_box.delete(0, END)

    for row in backend.search(
        title_value.get(), auth_value.get(), year_value.get(), isbn_value.get()
    ):
        list_box.insert(END, row)


def add_command():
    backend.insert(
        title_value.get(), auth_value.get(), year_value.get(), isbn_value.get()
    )
    list_box.delete(0, END)
    list_box.insert(
        END, (title_value.get(), auth_value.get(), year_value.get(), isbn_value.get())
    )


def get_selected_row(event):

    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)

    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[1])

    auth_entry.delete(0, END)
    auth_entry.insert(END, selected_tuple[2])

    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[3])

    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[4])


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(
        selected_tuple[0],
        title_value.get(),
        auth_value.get(),
        year_value.get(),
        isbn_value.get(),
    )


window = Tk()

window.wm_title("BookStore")

title_lab = Label(window, text="Title")
title_lab.grid(row=0, column=0)
title_value = StringVar()
title_entry = Entry(window, textvariable=title_value)
title_entry.grid(row=0, column=1)

auth_lab = Label(window, text="Author")
auth_lab.grid(row=0, column=2)
auth_value = StringVar()
auth_entry = Entry(window, textvariable=auth_value)
auth_entry.grid(row=0, column=3)

year_lab = Label(window, text="Year")
year_lab.grid(row=1, column=0)
year_value = StringVar()
year_entry = Entry(window, textvariable=year_value)
year_entry.grid(row=1, column=1)

isbn_lab = Label(window, text="ISBN")
isbn_lab.grid(row=1, column=2)
isbn_value = StringVar()
isbn_entry = Entry(window, textvariable=isbn_value)
isbn_entry.grid(row=1, column=3)

view_button = Button(window, text="View all", command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", command=window.destroy)
close_button.grid(row=7, column=3)

list_box = Listbox(window, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_box.yview)

list_box.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()

