from tkinter import Tk
import round_label

root = Tk()
root.minsize(500,500)
l = round_label.RoundedLabel(root,100,10,5,0,"white","black")
l.grid(row=0,column=0)

root.mainloop()