import tkinter as tk
from customtkinter import *
from pytube import YouTube


def Download_Video():     
    url =YouTube(str(link.get()),use_oauth=True, allow_oauth_cache=True)
    video = url.streams.get_highest_resolution()
    video.download()
    tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  

window = CTk()
window.geometry("600x200")
window.resizable(width=False,height=False)
window.title('YouTube Video Downloader')
set_default_color_theme("blue")

link = tk.StringVar()
CTkLabel(window,text = '                   Youtube Video Downloader                    ', font =("Arial",20,'bold')).pack()
CTkLabel(window, text = 'Paste Your YouTube Link Here:', font = ("Arial",20,'bold')).place(x= 5 , y = 60)
link_enter = CTkEntry(window, width = 580,textvariable = link,font = ("Arial", 15, 'bold')).place(x = 5, y = 100)
CTkButton(window,text = 'DOWNLOAD VIDEO', font = ("Arial", 15, 'bold'),command=Download_Video).place(x=385 ,y = 140)

window.mainloop()