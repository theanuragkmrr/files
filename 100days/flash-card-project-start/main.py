from tkinter import *
import pandas
import random
#------------------read csv file-------------------

data=pandas.read_csv("../data/french_words.csv")
list_data=data.to_dict(orient="records")
current_card={}

#------------------end csv read-------------------

#------------------random word generator___________


def ran():
    global current_card, timer
    window.after_cancel(timer)
    current_card=random.choice(list_data)
    F=current_card["French"]
    canvas.itemconfig(Tilte,text="French",fill="black")
    canvas.itemconfig(Word,text=F,fill="black")
    canvas.itemconfig(canvas_image, image=fimg)
    timer=window.after(3000, flip)

def flip():

    canvas.itemconfig(canvas_image, image=bimg)
    E = current_card["English"]
    canvas.itemconfig(Tilte, text="English",fill="white")
    canvas.itemconfig(Word, text=E, fill="white")

def remove_word():
    list_data.remove(current_card)
    x=pandas.DataFrame(list_data)
    x.to_csv("words_to_learn.csv")
    ran()
#------------------end random word generator___________


#------------------end random word generator___________

BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer=window.after(3000,flip)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
fimg=PhotoImage(file="../images/card_front.png")
bimg = PhotoImage(file="../images/card_back.png")
canvas_image=canvas.create_image(400,263,image=fimg)
Tilte=canvas.create_text(400, 150, text="Title",font=("Arial",28,"italic"))
Word=canvas.create_text(400, 263, text="Word",font=("Arial",28,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

wimg=PhotoImage(file="../images/wrong.png")
wrong_button=Button(image=wimg,bg=BACKGROUND_COLOR,highlightthickness=0,command=ran)
wrong_button.grid(column=0,row=1)

rimg=PhotoImage(file="../images/right.png")
right_button=Button(image=rimg,bg=BACKGROUND_COLOR,highlightthickness=0, command=remove_word)
right_button.grid(column=1,row=1)

ran()

window.mainloop()