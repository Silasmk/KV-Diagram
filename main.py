from tkinter import *
import numpy as np

root = Tk()
root.geometry("800x600")

label = Label(root, text="Hello World!")
label.pack()

kv_frame = Frame(root)
kv_frame.pack()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

dim = IntVar()
dim.set(3)
pdim = 2

def draw_Matrix(matrix):
    clear_frame(kv_frame)
    for i in matrix:
        row = Label(kv_frame, text=i)
        row.pack()

kv_matrix = np.zeros((dim.get(),dim.get()))



def update_Matrix(event):
    global pdim
    print("Update: " + str(dim.get()))
    kv_matrix = np.zeros((dim.get(),dim.get()))
    if pdim != dim.get():
        draw_Matrix(kv_matrix)
        root.update()
        pdim = dim.get()

scale = Scale(root, from_=1, to=7, orient=HORIZONTAL, variable=dim)
scale.set(3)
scale.pack()
scale.bind('<Motion>', update_Matrix)


root.mainloop()