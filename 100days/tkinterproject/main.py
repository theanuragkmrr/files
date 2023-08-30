from tkinter import *
window=Tk()

window.title("my first GUI program")
window.minsize(600,600)
#padding to all widgets
window.config(padx=40,pady=40)
#Label

label = Label(text="Hello", fg='red',  font=("Arial", 20, "bold"))
label.config(padx=50,pady=50)
label.grid(column=0,row=0)

# label.config(text="Anurag")

def button_clicked():
    a = Input.get()
    label.config(text=a)



button=Button(text="my button",fg='red',bg="blue",font=("Roboto",15,"italic"),command=button_clicked)
button.grid(column=1,row=0)


#ENtry component

Input=Entry(width=10)

Input.grid(column=0,row=2)






window.mainloop()