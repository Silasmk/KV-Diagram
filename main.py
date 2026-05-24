from tkinter import *
import numpy as np
import random

#Root Node
root = Tk()
root.geometry("800x600")

#Global Variables
dim = IntVar()
dim.set(1)
pdim = 0

kv_matrix = [0,0]

#Functions
def draw_Matrix(matrix):
    for widget in kv_frame.winfo_children():
        widget.destroy()
    for i in matrix:
        temp = ""
        for j in i:
            match j:
                case 0:
                    temp = temp + " □"
                case 1:
                    temp = temp + " ■"
        row = Label(kv_frame, text=temp)
        row.pack()

def create_Matrix(size):
    global kv_matrix
    if size%2 == 0:
        temp_dim = 2 ** (int(size/2))
        kv_matrix = np.random.choice([0, 1], size=(temp_dim,temp_dim), p=[0.5, 0.5])
    else:
        temp_dim = 2 ** (int(size/2))
        kv_matrix = np.random.choice([0, 1], size=(temp_dim,temp_dim*2), p=[0.5, 0.5])

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



update_Matrix(kv_matrix)
root.mainloop()