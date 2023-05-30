from tkinter import *
from customtkinter import * 
from time import strftime
from PIL import Image,ImageTk

def Youtube():
    import Youtube

def Dictionary():
    import Dictionary
    
def Calculator():
    import My_Calc

def player():
    window.destroy()
    import vidPlayer

def Flappy():
    pass

def back():
    window.destroy()
    import UI

def maps():
    window.destroy()
    import maps

def time():
	string = strftime('%H:%M:%S %p                                                                                                                   ')
	lbl.config(text=string+'100%')
	lbl.after(1000, time)
        
def tic():
    import TicTacToe

window = CTk()
window.title("APPS")
window.geometry("480x720")
set_appearance_mode("System")
set_default_color_theme("blue")

lbl = Label(window, background="#41403f", font="Helvetica 12 bold", foreground="white")
lbl.pack(side=TOP, anchor=NW)
time()

text = CTkLabel(window, text="APPS", font=("Helvetica", 25, 'bold'), text_color="#1d73c8").pack(pady=10)

frame = CTkFrame(window, corner_radius=10)
frame.pack(pady=10)


dic = ImageTk.PhotoImage((Image.open("assets/dict2.png")).resize((100,100), Image.ANTIALIAS))
cal = ImageTk.PhotoImage((Image.open("assets/download.png")).resize((100,100), Image.ANTIALIAS))
vid = ImageTk.PhotoImage((Image.open("assets/vid.png")).resize((100,100), Image.ANTIALIAS))
m = ImageTk.PhotoImage((Image.open("assets/maps.png")).resize((100,100), Image.ANTIALIAS))
tictac = ImageTk.PhotoImage((Image.open("assets/tictac.png")).resize((100,100), Image.ANTIALIAS))
vide = ImageTk.PhotoImage((Image.open("assets/vlc.png")).resize((100,100), Image.ANTIALIAS))


button1 = CTkButton(frame, command=Dictionary, text="", height=50, width=50, image=dic, corner_radius=50)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = CTkButton(frame, command=Calculator, text="", height=50, width=50, image=cal, corner_radius=50)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = CTkButton(frame, command=Youtube, text="", height=50, width=50, image=vid, corner_radius=50)
button3.grid(row=1, column=0, padx=10, pady=10)

button4 = CTkButton(frame, command=maps, text="", height=50, width=50, image=m, corner_radius=50)
button4.grid(row=1, column=1, padx=10, pady=10)

button5 = CTkButton(frame, command=tic, text="", height=50, width=50, image=tictac, corner_radius=50)
button5.grid(row=2, column=0, padx=10, pady=10)

button6 = CTkButton(frame, command=player, text="", height=50, width=50, image=vide, corner_radius=50)
button6.grid(row=2, column=1, padx=10, pady=10)

frame2 = CTkFrame(window, corner_radius=10)
frame2.pack(side=BOTTOM, padx=10, pady=10)

back = CTkButton(frame2, text="Home", command=back, corner_radius=10, width=50, height=35)
back.pack(side=BOTTOM)

window.mainloop()