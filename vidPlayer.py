from tkinter import *
import datetime
import tkinter as tk
from customtkinter import *
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo

root = CTk()
root.title("VLC")
root.geometry("1080x720+290+10")
frame = tk.Frame(root)
frame.pack()

image_icon = PhotoImage(file="assets/logo png.png")

lower_frame = CTkFrame(root , bg_color = "#FFFFFF")
lower_frame.pack ( fill="both", side = BOTTOM)

def update_duration(event):
    duration = vid_player.video_info()["duration"]
    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration


def update_scale(event):
    progress_value.set(vid_player.current_duration())


def load_video():
    file_path = filedialog.askopenfilename()

    if file_path:
        vid_player.load(file_path)

        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "Play"
        progress_value.set(0)


def seek(value):
    vid_player.seek(int(value))


def skip(value: int):
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get() + value)


def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "Pause"

    else:
        vid_player.pause()
        play_pause_btn["text"] = "Play"


def video_ended(event):
    progress_slider.set(progress_slider["to"])
    play_pause_btn["text"] = "Play"
    progress_slider.set(0)

def home():
    root.destroy()
    import Everything

load_btn = CTkButton(root, text="Browse", font=("calibri",12, "bold"), command=load_video)
load_btn.pack(ipadx=12, ipady=4, anchor=tk.NW)

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35)
back.place(x=1022, y=0)

vid_player = TkinterVideo(root, scaled=True, bg="black")
vid_player.pack(expand=True, fill=BOTH)

Buttonbackward = PhotoImage(file="assets/backward.png")
back = tk.Button(lower_frame, image=Buttonbackward, bd=0, height = 50, width =50,command=lambda: skip(-5))
back.pack(side = LEFT)

play_pause_btn = CTkButton(lower_frame, text="Play", width = 40, height = 2, command = play_pause, corner_radius=20)
play_pause_btn.pack(expand=True, fill="both", side = LEFT)

ButtonPlay = PhotoImage(file="assets/forward.png")
Playbutton = tk.Button(lower_frame, image=ButtonPlay, bd=0,  height = 50, width =50,
       command=lambda: skip(5)).pack(side = LEFT)

start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)), bg="black",fg="white")
start_time.pack(side="left")

progress_value = tk.IntVar(root)
progress_slider = tk.Scale(root, variable=progress_value, from_=0, to=0, orient="horizontal", command=seek, bg="black")
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)), bg="black",fg="white")
end_time.pack(side="left")

vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<SecondChanged>>", update_scale)
vid_player.bind("<<Ended>>", video_ended )

root.mainloop()