from tkinter import *
import time

#Create Master Window
master = Tk()
master.geometry('600x200+350+300')
master.title("Digital Clock by Pieter Paauw (Data2Wisdom) inpspired by Pydem")

timenow = ' '

cframe = Frame(master, width=400, height=100, bg='orange', relief=GROOVE)
cframe.pack()

clock = Label(cframe, padx=25, pady=40, bd=3,fg='black', font=('arial',38, 'bold'), text= timenow, bg='light green', relief = SUNKEN)
clock.pack()

def tick():
    global timenow
    newtime = time.strftime('TIME %H: %M: %S %p')
    if newtime != timenow:
        timenow = newtime
        clock.config(text = timenow)
    clock.after(200, tick)
    
tick()
master.mainloop()