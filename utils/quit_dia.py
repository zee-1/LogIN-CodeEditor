from tkinter import *
from tkinter import ttk


def quit_conf(*args,root=None):

      conf_window = Tk()
      conf_window.winfo_toplevel()
      conf_window.minsize(width=200,height=50)
      conf_window.maxsize(width=2000,height=1000)
      conf_window.title("Quit")
      def quit_conf_yes(*args):
            conf_window.destroy()
            if root != None:
                  root.destroy()

      main_frame  = ttk.Frame(conf_window,width=200, height=50)
      l = Label(main_frame, width=200, height=50)

      message_lable = Label(l ,width=100, height=10, text="Are you sure you want to quit?")
      message_lable.grid(row=0,column=0)

      butt_lab = Label(l,width=200, height=20)
      butt_lab.grid(row=1, column=0)

      yes = Button(butt_lab,text="Yes", command=lambda:quit_conf_yes(conf_window))
      yes.grid(row=0,column=0)

      No =  Button(butt_lab,text="No", command=lambda:quit_conf_yes(conf_window))
      No.grid(row=0, column=1)
      main_frame.grid(row=0, column=0)
      l.grid(row=0, column=0)
      
      conf_window.mainloop()