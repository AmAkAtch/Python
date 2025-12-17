from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

cv = Canvas(width=200, height=200)
logo = PhotoImage(file="day29_gui_password_manager/logo.png")
cv.create_image(100, 100, image=logo)

cv.grid(row=0, column=1)








window.mainloop()