from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=200)

def calculate_miles():
    miles_op.config(text=float(km_input.get())*1.609344)

title_label = Label(text="Miles to Km", font=("Ariel", 30, "bold"))
title_label.grid(column=1, row=0)

km_label = Label(text="Enter Km", font=("Ariel", 12))
km_label.grid(column=0, row=1)

km_input = Entry()
km_input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Ariel", 12))
miles_label.grid(column=0, row=2)

miles_op = Label(text="", font=("Ariel", 12))
miles_op.grid(column=2, row=2)

button = Button(text="Calculate", command=calculate_miles)
button.grid(column=1, row=3)











window.mainloop()