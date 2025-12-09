import tkinter

window = tkinter.Tk()
window.title("My first GUI window")
window.minsize(width=500, height=300)

label = tkinter.Label(text="Hello from windows", font=("Cambria",15, "bold"))
label.pack(side="bottom", )


window.mainloop()