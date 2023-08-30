from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
t=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(t)
    canvas.itemconfig(timer,text="00:00")
    timer_label.config(text="Timer")
    chk_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1

    work_sec=10
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2==0:
        timer_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Working Time",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global t
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    elif count_min==0:
        count_min="00"

    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        t=window.after(1000, count_down, count - 1)
    else:

        start_timer()
        marks=""
        for _ in range(int(reps/2)):
            marks+="✔"
        chk_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


timer_label=Label(text="Timer",font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
pic=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=pic)
timer=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,28,"bold"))
canvas.grid(column=1,row=1)



start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

chk_mark=Label(text="",fg=GREEN,bg=YELLOW,highlightthickness=0,font=(20))
chk_mark.grid(column=1,row=3)



window.mainloop()