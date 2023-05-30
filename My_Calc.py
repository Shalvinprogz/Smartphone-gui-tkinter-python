import tkinter as tk
from customtkinter import *
root = CTk()
root.title('Calculator')
#root.geometry("425x425")

frame = CTkFrame(root, corner_radius=10)
frame.pack(pady=10)

entry = CTkEntry(frame,width=200)
entry.grid(row=0,column=0,columnspan=3)

def home():
    root.destroy()
    import Everything


def click(n):
    entry.insert(tk.END,n)

def plus():
    k = entry.get()
    entry.delete(0, tk.END)
    global math
    math = "+"
    global p
    p = int(k)

def sub():
    k = entry.get()
    entry.delete(0, tk.END)
    global math
    math = "-"
    global p
    p = int(k)

def mul():
    k = entry.get()
    entry.delete(0, tk.END)
    global math
    math = "*"
    global p
    p = int(k)

def div():
    k = entry.get()
    entry.delete(0, tk.END)
    global math
    math = "/"
    global p
    p = int(k)

def clear():
    entry.delete(0,tk.END)


def equal():
    if math == "+":
        i = entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,p+int(i))
    elif math == "-":
        i = entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,p-int(i))
    elif math == "*":
        i = entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,p*int(i))
    elif math == "/":
        i = entry.get()
        entry.delete(0,tk.END)
        entry.insert(0,p/int(i))


buttton_1 = CTkButton(frame,text="1",command=lambda: click(1), width=60, height=60)
buttton_1.grid(row=1,column=0)
buttton_2 = CTkButton(frame,text="2",command=lambda: click(2), width=60, height=60)
buttton_2.grid(row=1,column=1)
buttton_3 = CTkButton(frame,text="3",command=lambda: click(3), width=60, height=60)
buttton_3.grid(row=1,column=2)
buttton_4 = CTkButton(frame,text="4",command=lambda: click(4), width=60, height=60)
buttton_4.grid(row=2,column=0)
buttton_5 = CTkButton(frame,text="5",command=lambda: click(5), width=60, height=60)
buttton_5.grid(row=2,column=1)
buttton_6 = CTkButton(frame,text="6",command=lambda: click(6), width=60, height=60)
buttton_6.grid(row=2,column=2)
buttton_7 = CTkButton(frame,text="7",command=lambda: click(7), width=60, height=60)
buttton_7.grid(row=3,column=0)
buttton_8 = CTkButton(frame,text="8",command=lambda: click(8), width=60, height=60)
buttton_8.grid(row=3,column=1)
buttton_9 = CTkButton(frame,text="9",command=lambda: click(9), width=60, height=60)
buttton_9.grid(row=3,column=2)
buttton_0 = CTkButton(frame,text="0",command=lambda: click(0), width=60, height=60)
buttton_0.grid(row=6,column=0)
buttton_plus = CTkButton(frame,text="+",command=plus, width=60, height=60)
buttton_plus.grid(row=4,column=0)
buttton_minus = CTkButton(frame,text="-",command=sub, width=60, height=60)
buttton_minus.grid(row=4,column=1)
buttton_equal = CTkButton(frame,text="=",command=equal, width=60, height=120)
buttton_equal.grid(row=4,column=2,rowspan=2)
buttton_multiply = CTkButton(frame,text="*",command=mul, width=60, height=60)
buttton_multiply.grid(row=5,column=0)
buttton_divide = CTkButton(frame,text="/",command=div, width=60, height=60)
buttton_divide.grid(row=5,column=1)
button_clear = CTkButton(frame,text="Clear",command=clear, width=120, height=60)
button_clear.grid(row=6,column=1,columnspan=2)

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35).pack(side=BOTTOM)

root.mainloop()