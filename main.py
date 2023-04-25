from tkinter import *

def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    wiersz = website + " | " + username + " | " + password + "\n"
    with open("passwords.txt", "a") as file:
        file.write(wiersz)
    input_website.delete(0, 'end')
    input_username.delete(0, 'end')
    input_username.insert(0, "angela@gmail.com")
    input_password.delete(0, 'end')

window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
input_website = Entry(width=42)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)
input_username = Entry(width=42)
input_username.grid(column=1, row=2, columnspan=2)
input_username.insert(0, "angela@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
input_password = Entry(width=32)
input_password.grid(column=1, row=3)

button_generate_password = Button(text="Generate")
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)








window.mainloop()
