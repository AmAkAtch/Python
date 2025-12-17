from tkinter import *
from tkinter import messagebox

#Constants
DEFAULT_EMAIL = "gadhavirushiraj7@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    print("Generate Password")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if input_website.get() and input_email.get() and input_password.get():
        with open("day29_gui_password_manager/passwords.txt", "a") as file:
            file.write(f'\n{input_website.get()} | {input_email.get()} | {input_password.get()}')
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()
            print("Password Saved")
    else:
        messagebox.showwarning(title="Missing Data", message="Please fill all fields.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

cv = Canvas(width=200, height=200)
logo = PhotoImage(file="day29_gui_password_manager/logo.png")
cv.create_image(100, 100, image=logo)
cv.grid(row=0, column=1)


#row for website
label_website = Label(text="Website:")
label_website.grid(row=1, column=0 )

input_website = Entry(width=45)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

#row for email
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0 )

input_email = Entry(width=45)
input_email.insert(0, DEFAULT_EMAIL)
input_email.grid(row=2, column=1, columnspan=2)

#row for password
label_password = Label(text="Password:")
label_password.grid(row=3, column=0 )

input_password = Entry(width=27)
input_password.grid(row=3, column=1)

btn_gnrt_pswd = Button(text="Generate Password", command=generate_password)
btn_gnrt_pswd.grid(row=3, column=2)

#row to save password
btn_save = Button(text="Add", width=40 ,command=save_password)
btn_save.grid(row=4, column=1, columnspan=2)









window.mainloop()