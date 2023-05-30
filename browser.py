# Import tkinter and webview libraries
from customtkinter import *
import tkinterweb
import webview

root = CTk()
root.geometry("400x720")

frame = tkinterweb.HtmlFrame(root)
frame.load_website("https://www.google.com/")
frame.pack(fill="both", expand=True)

def home():
    root.destroy()
    import UI

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35).pack(side=BOTTOM)

root.mainloop()
