from tkinter import *
import numpy as np

#Root Node
root = Tk()
root.geometry("800x600")

#Global Variables
dim = IntVar()
dim.set(1)
pdim = 0

#Functions
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def draw_Matrix(matrix):
    clear_frame(kv_frame)
    for i in matrix:
        row = Label(kv_frame, text=i)
        row.pack()

kv_matrix = np.zeros((dim.get(),dim.get()))

def create_Matrix(size):
    global kv_matrix
    if size%2 == 0:
        temp_dim = 2 ** (int(size/2))
        kv_matrix = np.zeros((temp_dim,temp_dim))
    else:
        temp_dim = 2 ** (int(size/2))
        kv_matrix = np.zeros((temp_dim,temp_dim*2))

def update_Matrix(event):
    global pdim
    if pdim != dim.get():
        create_Matrix(dim.get())
        draw_Matrix(kv_matrix)
        root.update()
        pdim = dim.get()

#Widgets
label = Label(root, text="Hello World!")
label.pack()

kv_frame = Frame(root, width=400, height=200)
kv_frame.pack_propagate(False)
kv_frame.pack()

scale = Scale(root, from_=1, to=7, orient=HORIZONTAL, variable=dim, command=update_Matrix)
scale.set(1)
scale.pack()



draw_Matrix(kv_matrix)
root.mainloop()