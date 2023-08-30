from tkinter import *
from tkinter import  messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    rl=random.randint(8,10)
    rn=random.randint(2,4)
    rs=random.randint(2,4)
    pass_list_l=[random.choice(letters) for _ in range(rl) ]
    pass_list_n=[random.choice(numbers) for _ in range(rn) ]
    pass_lists_s=[random.choice(symbols) for _ in range(rs) ]

    pass_list=pass_list_n+pass_lists_s+pass_list_l
    random.shuffle(pass_list)
    password="".join(pass_list)
    pass_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w=input_website.get()
    e=user_input.get()
    p=pass_input.get()
    new_data={
        w:{
            "Email":e,
            "Password":p
        }
    }


    if len(w)==0 and len(p)==0 and len(e)==0:
        messagebox.askokcancel(title=w,
                               message="The fields are empty.")

    else:
        is_ok=messagebox.askokcancel(title=w,
                                       message=f"Thses are the details entered: \nEmail: {e}\nPassword: "
                                               f"{p}\nIs it ok to save?")


        if is_ok:
            try:
                with open("data.json","r") as f:
                    #Read old data
                    data=json.load(f)
            except FileNotFoundError:
                with open("data.json","w") as f:
                    json.dump(new_data,f,indent=4)
            else:
                #update old data with holder
                data.update(new_data)
                with open("data.json","w") as f:
                    # saving updated data
                    json.dump(data,f,indent=4)
            finally:
                input_website.delete(0, END)
                pass_input.delete(0, END)

#-------------------------search password------------------------------ #

def search():

    w=input_website.get()
    try:
        with open("data.json") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.askokcancel(title=w,
                               message="No data file found!")
    else:
            if w in data:
                e=data[w]["Email"]
                p=data[w]["Password"]
                user_input.insert(0,e)
                pass_input.insert(0,p)
                # messagebox.showinfo(title=w,message=f"\nEmail: {e}\nPassword: "
                #                                    f"{p}")
            else:
                messagebox.askokcancel(title=w,
                                       message="No result found!")
                input_website.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()

window.title("Password Generator")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
pic=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pic)
canvas.grid(column=1,row=0)

web_label=Label(text='Website: ')
web_label.grid(column= 0,row=1)


input_website=Entry(width=35)
input_website.grid(column=1,row=1)
input_website.focus()
username_label=Label(text='Email/Username: ')
username_label.grid(column= 0,row=2)

user_input=Entry(width=60)
user_input.grid(column=1,row=2,columnspan=2)

password_label=Label(text='Password: ')
password_label.grid(column= 0,row=3)

pass_input=Entry(width=35)
pass_input.grid(column=1,row=3)

genrate_button=Button(text="Generate Password",width=20,command=gen_pass)
genrate_button.grid(column=2 ,row=3)

Add=Button(text="Add",width=50, command=save)
Add.grid(column=1 ,row=4,columnspan=2)

search_button=Button(text="Search",width=20,command=search)
search_button.grid(column=2,row=1)



window.mainloop()