from customtkinter import *
from tkintermapview import TkinterMapView

root = CTk()
root.geometry(f"{600}x{400}")
root.title("map_view_simple_example.py")

def home():
    root.destroy()
    import Everything

map_widget = TkinterMapView(root, corner_radius=0, width=600, height=400)
map_widget.pack(fill="both", expand=True)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.set_address("Berlin Germany", marker=True)

back = CTkButton(root, text="Home", command=home, corner_radius=10, width=50, height=35).pack(side=BOTTOM)

root.mainloop()