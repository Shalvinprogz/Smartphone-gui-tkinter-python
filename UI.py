from customtkinter import *
from time import strftime
from PIL import Image,ImageTk

def Drawer():
    root.destroy()
    import Everything

def camera():
    import Camera

def time():
	string = strftime('%H:%M:%S %p                                                                                           ')
	lbl.configure(text=string+'100%')
	lbl.after(1000, time)

def browser():
    root.destroy()
    import browser

def ai():
    import assistant

set_default_color_theme("blue")
root = CTk()
root.title("Home Screen")
root.geometry("400x720")
root.wm_attributes('-transparentcolor', '#ab23ff')



#wall = CTkImage(Image.open("wall.jpg"))
wall = ImageTk.PhotoImage((Image.open("assets/wall.png")).resize((500,1000), Image.ANTIALIAS))
img= ImageTk.PhotoImage((Image.open("assets/open_app_drawer_button.png")).resize((70,70), Image.ANTIALIAS))
cam= ImageTk.PhotoImage((Image.open("assets/cam.png")).resize((70,70), Image.ANTIALIAS))
brw= ImageTk.PhotoImage((Image.open("assets/safari-icon.png")).resize((70,70), Image.ANTIALIAS))
sear= ImageTk.PhotoImage((Image.open("assets/ai.png")).resize((70,70), Image.ANTIALIAS))

panel = CTkLabel(root, image = wall, text="")
panel.place(x=0,y=0, relwidth=1, relheight=1)

lbl = CTkLabel(root, bg_color="#444340", font=("Helvetica",13,'bold'), height=4)
lbl.pack(side=TOP, anchor=NW)
time()

frame = CTkFrame(root)
frame.pack(side=BOTTOM)

Browser = CTkButton(frame, command=browser, image=brw, text="", width=10, height=10, corner_radius=50)
Browser.grid(row=0, column=1, pady=10, padx=10)

appDrawer = CTkButton(frame, command=Drawer, image=img, text="", width=10, height=10, corner_radius=50)
appDrawer.grid(row=0, column=2, pady=10, padx=10)

camera = CTkButton(frame, command=camera, image=cam, text="", width=10, height=10, corner_radius=50)
camera.grid(row=0, column=4, pady=10, padx=10)

search = CTkButton(frame, image=sear, fg_color="white", text="", corner_radius=20,  width=10, height=10, command=ai)
search.grid(row=0, column=0, pady=10, padx=10)


root.mainloop()