from tkinter import *
import numpy as np

root = Tk()
root.geometry("800x600")

label = Label(root, text="Hello World!")
label.pack()

size = 4
kv_matrix = np.zeros((size,size))

for i in kv_matrix:
    print(i)
    row = Label(root, text=i)
    row.pack()


root.mainloop()