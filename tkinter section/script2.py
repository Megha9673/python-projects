from tkinter import *

window=Tk()

def convert():
    gm = float(value.get())*1000
    pnds = float(value.get())*2.20462
    oncs = float(value.get())*35.274
    t2.insert(END,gm)
    t3.insert(END,pnds)
    t4.insert(END,oncs)

t1=Label(window,text="Kg")
t1.grid(row=0,column=0)

value=StringVar()
e1=Entry(window,textvariable=value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=convert)
b1.grid(row=0,column=2)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=0)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=1)

t4=Text(window,height=1,width=20)
t4.grid(row=1,column=2)

window.mainloop()
