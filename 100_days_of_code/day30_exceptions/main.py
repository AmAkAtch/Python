from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip

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
    # pyperclip.copy(password)

    input_password.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def create_or_update_json(data):
    with open("day30_exceptions/passwords.json", "w") as file:
                json.dump(data,file, indent=4)

def save_password():
    website = input_website.get().title()
    email = input_email.get()
    password = input_password.get()

    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \nis this correct?")
        if is_ok:
            try:
                with open("day30_exceptions/passwords.json", "r") as file:
                    data = json.load(file)        
            except FileNotFoundError:
                print("File did not exist, Creating new file")
                create_or_update_json(new_data)
            except json.JSONDecodeError:
                create_or_update_json(new_data) 
            else:
            
                data.update(new_data)
                create_or_update_json(data)    
            finally:    
                input_website.delete(0, END)
                input_password.delete(0, END)
                input_website.focus()
                messagebox.showinfo(title="Password Saved", message="Details Saved Successfully")
    else:
        messagebox.showwarning(title="Missing Data", message="Please fill all fields.")

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open("day30_exceptions/passwords.json", "r") as data_file:
            data = json.load(fp=data_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Passwords Stored in Database")
    except json.JSONDecodeError:
        messagebox.showerror(message="No Passwords Stored in Database") 
    else:
        if input_website.get():
            user_search = input_website.get().title()
            try:
                email = data[user_search]["email"]
                password = data[user_search]["password"]
                messagebox.showinfo(title=f"Details for {user_search}",message=f'Email: {email}\nPassword: {password}')
            except KeyError:
                messagebox.showwarning(message="No website with same name Avaialable")
        else:
            messagebox.showwarning(message="Enter Website Name to Search first!")       


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

input_website = Entry(width=27)
input_website.grid(row=1, column=1)
input_website.focus()

btn_search = Button(text="Search", command=search_website, width=15)
btn_search.grid(row=1, column=2)

#row for email
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0 )

input_email = Entry(width=46)
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