from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- Generating password ------------------------------- #

def gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry2.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- PASSWORDS ------------------------------- #

def copy():
    web = entry.get()
    mail = entry1.get()
    pas = entry2.get()
    new_data = {
        web : {
            "email": mail,
            "password": pas,
        }
    }

    if pas and mail:
        is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered: \nEmail: {mail}\nPassword: {pas}.\nIs it OK to save .")

        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    #Read Old Data
                    data = json.load(file)

            except:
                with open("data.json", mode="w") as file:
                    json.dump(new_data,file,indent=5)
            else:
                 #Updating Data
                data.update(new_data)

                with open("data.json", mode="w") as file:
                    #Writing Data
                    json.dump(data,file,indent=5)
            finally:
                entry.delete(0,END)
                entry2.delete(0, END)

    else:
        messagebox.showwarning(title="WARNING",message=f"THESE DETAILS CAN CANNOT BE LEFT EMPTY.\nEmail: {mail}\nPassword : {pas}")

#---------------------------Searching-------------------------#
def find_pasword():
    user_input = entry.get()
    try:
        with open("data.json") as ff:
            data = json.load(ff)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File is not found\nYou have to save some data first.")

    else:
         if user_input in data:
            email = data[user_input]["email"]
            Password = data[user_input]["password"]
            messagebox.showinfo("SAVED DATA",f"Email: {email}\nPassword: {Password} ")
         else:
             messagebox.showinfo(title="ERROR", message=f"No details are found related to {user_input}")
             
# ---------------------------- Interface ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx= 20, pady=20,bg="orange")

canvas = Canvas(width=200, height=200,bg="orange",highlightthickness=0)
logo = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website = Label(text="Website: ",font=("Times New Roman",15,"bold"),bg="orange",fg="blue")
website.grid(row=1,column=0)

entry = Entry(width=35)
entry.grid(row=1,column=1,columnspan=2)
entry.focus()
#-----------------------SEARCH BUTTON-----------------------#
search = Button(text="Search",command=find_pasword)
search.grid(row=1,column=3)

#-----------------------------------------------------------#
mail = Label(text="Email/Username: ",font=("Times New Roman",15,"bold"),bg="orange",fg="blue")
mail.grid(row=2,column=0)

entry1 = Entry(width=35,)
entry1.insert(END,string="default mail")
entry1.grid(row=2,column=1,columnspan=2)

password = Label(text="Password: ",font=("Times New Roman",15,"bold"),bg="orange",fg="blue")
password.grid(row=3,column=0)

entry2 = Entry(width=21)
entry2.grid(row=3,column=1)

generate = Button(text="Generate Password",command=gen)
generate.grid(row=3,column=3)

add = Button(text="Add",width=36,command=copy)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()