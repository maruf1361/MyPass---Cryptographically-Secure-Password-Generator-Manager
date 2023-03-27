from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, string = password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    get_website = website_entry.get()
    get_pass = pass_entry.get()
    get_email = email_entry.get()

    if len(get_website) >0 and len(get_pass) > 0:
        warning = messagebox.askokcancel(title=get_website, message=f"These are the details you entered:\nWebsite: {get_website}\nPassword: {get_pass}\nDo you wish to save this?")
        if warning:
            with open("data.text", "a") as file:
                file.write(f"{get_website} | {get_email} | {get_pass}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Warning!!", message="Please don't leave any field empty")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass: Everyone's Trusted Password Manager")
window.config(padx=30, pady=20)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

website_entry = Entry(width= 52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width= 52)
email_entry.insert(END, string="maruf.bin.faruque.payel.1361@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width= 34)
pass_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", command= generate_password)
generate_btn.grid(row=3, column=2, columnspan=2)

add_btn = Button(text="Add", width= 45, command= save_password)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()