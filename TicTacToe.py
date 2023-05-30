import tkinter as tk
from tkinter import messagebox
from customtkinter import *

root = CTk()
root.title("Tik Tak Toe")
buttons = [[0,0,0],[0,0,0],[0,0,0]]
player = "X"

def home():
    root.destroy()
    import Everything

def winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            messagebox.showinfo("TIC TAC","You Win")
            return True

    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            messagebox.showinfo("TIC TAC","You Win")
            return True
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        messagebox.showinfo("TIC TAC","You Win")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "": 
        messagebox.showinfo("TIC TAC","You Win")
        return True
    elif tie() == False:
        messagebox.showinfo("TIC TAC TOE","Tie")
    else:
        return False
    
def tie():
    count = 0

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] != "":
                count += 1

    if count == 9:
        return False
    else:
        return True

def restart():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")
    global player
    player = "X"

def funct(row,column):
    global player
    if buttons[row][column]["text"] == "" and winner() == False:
        if player == "X":
            buttons[row][column].config(text="X")
            if winner() == False:
                player = "O"

        else:
            buttons[row][column].config(text="O")
            if winner() == False:
                player = "X"

for row in range(3):
    for  column in range(3):
        buttons[row][column] = tk.Button(root,text="",command=lambda row=row,column=column: funct(row,column),font=('consolas',40),width=5,height=2)
        buttons[row][column].grid(row=row,column=column)

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35)
back.grid(row=3,column=0)
CTkButton(root,text="Restart",command=restart,corner_radius=10, width=50, height=35).grid(row=3,column=2)

root.mainloop()