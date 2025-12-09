from tkinter import *

window = Tk()
window.title("My first GUI window")
window.minsize(width=500, height=300)


def on_click():
    label.config(text=user_input.get())

label = Label(text="Hello from windows", font=("Cambria",15, "bold"))
label.pack()

button = Button(text="click me", command=on_click)
button.pack()

user_input = Entry()
user_input.pack()


window.mainloop()