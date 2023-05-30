from customtkinter import * 
from PyDictionary import PyDictionary

def home():
    root.destroy()
    import Everything

def search():
    text.delete(1.0,END)

    dictionary = PyDictionary()
    define = dictionary.meaning(entry.get())

    for key,value in define.items():
        text.insert(END, key + "\n\n")

        for values in value:
            text.insert(END, f"- {values}\n\n")

root = CTk()
root.title("Dictionary")
root.geometry("600x580")

set_appearance_mode("System")
set_default_color_theme("blue")

label = CTkFrame(root, corner_radius=10)
label.pack(pady=20)

entry = CTkEntry(label,width=400, font=("Helvetica",28))
entry.grid(row=0, column=0, padx=10, pady=10)

button = CTkButton(label, text="Search", command=search, height=37)
button.grid(row=0, column=1, padx=8, pady=10)

textFrame = CTkFrame(root, corner_radius=10)
textFrame.pack(pady=10)

text = CTkTextbox(textFrame,width=560, height=400, wrap=WORD, font=("Arial",18))
text.pack(pady=10,padx=10)

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35)
back.pack(side=BOTTOM)

root.mainloop()