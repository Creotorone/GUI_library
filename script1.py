from tkinter import *


window = Tk()

l1 = Label(window, text="kg")
l1.grid(row=0, column=0)


def convert_kg():
    print(e1_value.get())
    grams = round(float(e1_value.get()), 2) * 1000
    pounds = round(float(e1_value.get()), 2) * 2.2046
    ounces = round(float(e1_value.get()), 2) * 35.27
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


b1 = Button(window, text="Convert", command=convert_kg)
b1.grid(row=0, column=2)


e1_value = StringVar()

e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


t1 = Text(window, height=1, width=10)
t1.grid(row=1, column=0)


t2 = Text(window, height=1, width=10)
t2.grid(row=1, column=1)


t3 = Text(window, height=1, width=10)
t3.grid(row=1, column=2)

window.mainloop()

