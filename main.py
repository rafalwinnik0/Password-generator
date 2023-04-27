from tkinter import *
import random
import json

def generate_password():
    password = ''
    uppercase = [chr(iteration) for iteration in range(65, 91)]
    lowercase = [chr(iteration) for iteration in range(97, 123)]
    signs = [chr(iteration) for iteration in range(33, 39)]
    tab = uppercase + lowercase + signs
    for _ in range(0, 10):
        password += random.choice(tab)
    input_password.insert(0, password)
    print(password)

def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }
    with open("data.json", "r") as file:
        data = json.load(file)
        print(f"Load: {data}")
        data.update(new_data)
        print(f"Update: {data}")
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print(f"Dump: {data}")

    input_website.delete(0, 'end')
    input_username.delete(0, 'end')
    input_username.insert(0, "angela@gmail.com")
    input_password.delete(0, 'end')

def find():
    input_password.delete(0, 'end')
    input_username.delete(0, 'end')
    website = input_website.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        if website in data:
            password = data[website]["password"]
            username = data[website]["username"]
            input_password.insert(0, password)
            input_username.insert(0, username)
        else:
            print(f"Website: {website} doesn't exist!")

window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
input_website = Entry(width=32)
input_website.grid(column=1, row=1)
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

button_generate_password = Button(text="Generate", command=generate_password)
button_generate_password.grid(column=2, row=3)

button_search = Button(text="Search", command=find)
button_search.grid(column=2, row=1)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
