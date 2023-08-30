from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Tic Tac Toe")
root.geometry('400x400')

clicked = True
count = 0


# dissabled all buttons after win
def disable_btn():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


# winniner checking function
def chk_win():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()

    #         "O" check winning
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'O' is winner")
        disable_btn()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'X' is winner")
        disable_btn()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'O' is winner")
        disable_btn()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'O' is winner")
        disable_btn()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message=" 'O' is winner")
        disable_btn()
    elif b4["text"] == "O" and b5["text"] == "0" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'O' is winner")
        disable_btn()
    elif b7["text"] == "O" and b8["text"] == "0" and b9["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", message="'O' is winner")
        disable_btn()


# Button clicked function

def b_click(b):
    global count, clicked
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        chk_win()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        chk_win()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey the box is already filled...\n choose another box")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global count,clicked
    clicked=True
    count=0
    b1 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b1))
    b1.grid(row=0, column=0)

    b2 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b2))
    b2.grid(row=0, column=1)

    b3 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b3))
    b3.grid(row=0, column=2)

    b4 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b4))
    b4.grid(row=1, column=0)

    b5 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b5))
    b5.grid(row=1, column=1)

    b6 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b6))
    b6.grid(row=1, column=2)

    b7 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b7))
    b7.grid(row=2, column=0)

    b8 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b8))
    b8.grid(row=2, column=1)

    b9 = Button(root, text=" ", height=7, width=14, bg="SystemButtonFace", font=("roboto"), command=lambda: b_click(b9))
    b9.grid(row=2, column=2)


# menu
menubar = Menu(root)
root.config(menu=menubar)
# create menu options
options_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)
reset()
root.mainloop()
