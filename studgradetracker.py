import tkinter as tk
from tkinter import *

root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")

def Calculation():
    english = int(englishentry.get())
    skills = int(analytical_skillentry.get())
    general = int(generalknowledgeentry.get())
    total = (english + skills + general)
    Label(root, text=f"{total}", font="arial 15 bold").place(x=250, y=170)

    average = int(total / 3)
    Label(root, text=f"{average}", font="arial 15 bold").place(x=250, y=210)

    if average > 50:
        grade = "PASS"
    else:
        grade = "FAIL"
    Label(root, text=f"{grade}", font="arial 15 bold", fg="blue").place(x=250, y=250)

sub1 = Label(root, text="English:", font="arial 10")
sub2 = Label(root, text="Analytical Skill:", font="arial 10")
sub3 = Label(root, text="General Knowledge:", font="arial 10")
total = Label(root, text="Total:", font="arial 10")
avg = Label(root, text="Average:", font="arial 10")
grade = Label(root, text="Grade:", font="arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=70)
sub3.place(x=50, y=120)
total.place(x=50, y=170)
avg.place(x=50, y=210)
grade.place(x=50, y=250)

englishentry = Entry(root)
analytical_skillentry = Entry(root)
generalknowledgeentry = Entry(root)

englishentry.place(x=250, y=20)
analytical_skillentry.place(x=250, y=70)
generalknowledgeentry.place(x=250, y=120)

Button(root, text="Calculate", command=Calculation).place(x=150, y=300)
Button(root, text="Exit", command=root.destroy).place(x=250, y=300)

root.mainloop()
