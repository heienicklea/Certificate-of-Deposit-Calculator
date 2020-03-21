#cdCaculator.py
#A program that calculators the profits of a Certificate of Deposit after three options of year for x amount of deposit.
from tkinter import *
from tkinter import messagebox
import time
win = Tk()
win.title("CD Calculator")
win.configure(background="#FFF")
win.geometry("400x500")

def compute():
    threeMonths = .08
    oneYear = .10
    threeYears = .12
    deposit1 = deposit.get()
    timeSelection1 = timeSelection.get()

    if timeSelection1 == 1:
        rate = threeMonths / 12
        time = 3 / 12 * 12
        time_word = "three months"
    if timeSelection1 == 2:
        rate = oneYear / 12
        time = 1 * 12
        time_word = "one year"
    if timeSelection1 == 3:
        rate = threeYears / 12
        time = 3 * 12
        time_word = "three years"

    ratePlusOne = rate + 1
    rightSide = ratePlusOne ** time
    totalReturns = int(deposit1 * rightSide)
    profit = int(totalReturns - deposit1)
    output_label.configure(text=f" The investment took you {time_word}.\n Initial Deposit:${deposit1}\n New Balance: ${totalReturns} \n Total Profit:${profit} ")

def clear():
    output_label.configure(text="")
    deposit_input_entry.delete(0, 'end')
    timeSelection_input_entry.delete(0, 'end')


def close():
    exit(win)

def clicked():
    messagebox.showinfo('More', 'More Info on CDs: \nA certificate of deposit (CD) is a savings account found at banks and credit unions where you can deposit money for a predetermined amount of time and earn interest on those funds. The interest is usually compounded and added to the principal. Choose your CD length wisely. The duration of CD accounts typically determines the rate; the longer the term, the better your CD interest rate will be.\n\nCreated with the purpose to be an interactive aid for those trying to better understand how a CD works \n\nProject Developers:\nAaron Heienickle Class of 2020\nJonathan Werner Class of 2023\n ')

title_frame = Frame(win)
title_frame.pack(side = TOP)
title_label = Label(title_frame, text="Certificate of Deposit Calculator", font="Trebuchet 16 bold", background = "#FFF", fg="#808000", relief = GROOVE)
title_label.grid(row=0,column=0,columnspan=3)

description_frame = Frame(win, background = '#FFF')
description_frame.pack(side = TOP)
description_label = Label(description_frame, text="A CD is an investment in which money is invested for a \n specific amount of time gaining a return based on a set interest rate.", font="Trebuchet 10", background = "#FFF", justify = CENTER)
description_label.grid(row=0,column=0,columnspan=3)

button_frame = Frame(win, background="#FFF")
button_frame.pack(side = RIGHT, fill = BOTH)
button_compute = Button(button_frame, text="Compute", width=7, command = compute, background="White")
button_compute.grid(row=0, column=0, columnspan=5)
button_clear = Button(button_frame, text="Clear", width=7, command = clear, background="White")
button_clear.grid(row=1, column=0, columnspan=5)
button_exit = Button(button_frame, text="Exit", width=7, command = close, background="White")
button_exit.grid(row=2, column=0, columnspan=5)
button_credit = Button(button_frame, text="More", width=7, command=clicked, background="White")
button_credit.grid(row=3, column=0, columnspan=5)

timeSelection_input_frame = Frame(win, background="#FFF")
timeSelection_input_frame.pack()
timeSelection_input_label = Label(timeSelection_input_frame, text="Below are the rates for three amounts of time, \n select one by typing the number it corresponds to (1, 2, or 3). \n\n(1) Three months: 8%\n(2) One Year: 10%\n(3) Three Years: 12%", background = "#FFF", justify = LEFT, relief = RIDGE)
timeSelection_input_label.grid(row=0,column=0, columnspan=20)
timeSelection = IntVar()
timeSelection_input_entry = Entry(timeSelection_input_frame, textvariable=timeSelection, width=1, background="#FFF", relief = SUNKEN)
timeSelection_input_entry.grid(row=0, column=1, columnspan=20)


input_frame = Frame(win, background="#FFF")
input_frame.pack()
deposit_amount_label = Label(input_frame, text="How much would you like to deposit:", background="#FFF", justify = LEFT, relief = RIDGE)
deposit_amount_label.grid(row=0, column=0, columnspan=10)
deposit = IntVar()
deposit_input_entry = Entry(input_frame, textvariable=deposit, background="#FFF", width=10, relief = RIDGE)
deposit_input_entry.grid(row=2, column=2, columnspan=5)

output_frame = Frame(win)
output_frame.pack()
output_label = Label(output_frame, text="", background="#FFF")
output_label.grid(row=2, column=0, columnspan=2)



image_frame = Frame(win, background = '#FFF')
image_frame.pack(side = BOTTOM)
teacher_picture = PhotoImage(file='man.png')
teacher_picture_label = Label(image_frame, image=teacher_picture)
teacher_picture_label.image = teacher_picture
teacher_picture_label.grid(row=0, column=0)
#for fun and learning
for i in range(1, 25):
    top = Toplevel(win, bg = "BLUE")
    top.geometry("1000x200")
    top.title("Are you Ready to Calculate CDs!")
    top2 = Toplevel(win, bg = "RED")
    top2.geometry("1050x20")
    top2.title("CDs CDs CDs CDs")
    top3 = Toplevel(win, bg="Yellow")
    top3.geometry("1100x200")
    top3.title("CD Calculator Inbound")
    top4 = Toplevel(win, bg="Green")
    top4.geometry("1150x200")
    top4.title("CERTIFICATE OF DEPOSITS")
    top5 = Toplevel(win, bg="Purple")
    top5.geometry("1200x200")
    top5.title("Sorry if you were grading this at night Mr. Stapelton")


win.mainloop()


