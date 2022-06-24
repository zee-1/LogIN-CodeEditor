from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()
img = Image.open('Python/Project/tkinter/bg.jpg')
im  = ImageTk.PhotoImage(img)
root.minsize(width=im.width(), height=im.height())
root.configure(background=im)
f1 = Frame(root, width=400, height=400, padx=10, pady=10, bg="red")
f1.place(anchor=CENTER,relx=0.5,rely=0.5)
f2 = Frame(f1,width=50, height=50, padx=10, pady=10, bg="green")
f2.grid(sticky='nsew')
f2.place(anchor=CENTER,relx=0.5,rely=0.5)

root.mainloop()