from tkinter import *
window=Tk()
window.title("Miles to Kilometer")
window.minsize(400,200)
window.config(padx=100,pady=50)

def calculate():
    m=float(miles_input.get())
    c=round(m*1.603,2)
    calculate_label.config(text=c)



miles_input=Entry()
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_to_lable=Label(text="is equal to")
is_equal_to_lable.grid(column=0,row=1)


calculate_label=Label(text="0")
calculate_label.grid(column=1,row=1)


km_label=Label(text="Km")
km_label.grid(column=2,row=1)

calculate_button=Button(text="Calculates",command=calculate)
calculate_button.grid(column=1,row=2)








window.mainloop()