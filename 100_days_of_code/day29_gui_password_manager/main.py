from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Constants
DEFAULT_EMAIL = "gadhavirushiraj7@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    input_password.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \n is this correct?")
        if is_ok:
            with open("day29_gui_password_manager/passwords.txt", "a") as file:
                file.write(f'{input_website.get()} | {input_email.get()} | {input_password.get()}\n')
                input_website.delete(0, END)
                input_password.delete(0, END)
                input_website.focus()
                messagebox.showinfo(title="Password Saved", message="Details Saved Successfully")
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