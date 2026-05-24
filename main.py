from tkinter import *
import numpy as np

root = Tk()
root.geometry("800x600")

label = Label(root, text="Hello World!")
label.pack()

kv_frame = Frame(root, width=200, height=200)
kv_frame.pack_propagate(False)
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
    global kv_matrix
    if pdim != dim.get():
        kv_matrix = np.zeros((dim.get(),dim.get()))
        draw_Matrix(kv_matrix)
        root.update()
        pdim = dim.get()

scale = Scale(root, from_=1, to=7, orient=HORIZONTAL, variable=dim, command=update_Matrix)
scale.set(3)
scale.pack()


draw_Matrix(kv_matrix)
root.mainloop()