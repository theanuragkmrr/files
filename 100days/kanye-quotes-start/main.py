from tkinter import *
import requests

def get_quote():
    response=requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data=response.json()
    q=data["quote"]
    canvas.itemconfig(t,text=q)
    #Write your code here.



window=Tk()
window.title("Kenya Quotes")
window.config(padx=50,pady=50)
canvas=Canvas(width=300,height=414)
img=PhotoImage(file="background.png")
canvas.create_image(130,207,image=img,)
t=canvas.create_text(150,207,text="Kanye Quote",width=250,font=("Arial",24,"normal"))
canvas.grid(column=0,row=0)
k=PhotoImage(file="kanye.png")
kb=Button(image=k,highlightthickness=0,command=get_quote)
kb.grid(row=1,column=0)
window.mainloop()