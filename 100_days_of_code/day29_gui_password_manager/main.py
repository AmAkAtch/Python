from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("Generate Password")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    print("Save Password")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

cv = Canvas(width=200, height=200)
logo = PhotoImage(file="day29_gui_password_manager/logo.png")
cv.create_image(100, 100, image=logo)
cv.grid(row=0, column=1)


#row for website
label_website = Label(text="Website:")
label_website.grid(row=1, column=0 )

input_website = Text(width=35, height=1)
input_website.grid(row=1, column=1, columnspan=2)

#row for email
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0 )

input_email = Text(width=35, height=1)
input_email.grid(row=2, column=1, columnspan=2)

#row for password
label_password = Label(text="Password:")
label_password.grid(row=3, column=0 )

input_password = Text(width=21, height=1)
input_password.grid(row=3, column=1)

btn_gnrt_pswd = Button(text="Generate Password", command=generate_password)
btn_gnrt_pswd.grid(row=3, column=2)

#row to save password
btn_save = Button(text="Add", width=36 ,command=save_password)
btn_save.grid(row=4, column=1, columnspan=2)









window.mainloop()