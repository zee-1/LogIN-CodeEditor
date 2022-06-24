from tkinter import *
from tkinter import ttk
from utils.code_editor_pro import *
import utils.round_but


def Wind(*args,**kwargs):
      kwargs["root"].destroy()
      win = Tk()
      win.title("Inside")
      frame = Frame(win, width=128, height= 64)
      frame.grid()
      if kwargs:
            if "text" in kwargs:
                  l = Label(frame, text="Welcome "+kwargs["text"]).grid(row=0,column=0)
      else:
            l = Label(frame, text="You did it, you made it in", font=("Arial", 20), anchor=CENTER)

      win.mainloop()

def Regist(win,*args):
      win.destroy()
      root = Tk()
      root.title("Registration")
      root.minsize(width=1000,height=1000)



      mainframe = Frame(root, width= 800, height=700)
      mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
      mainframe.columnconfigure(0, weight=1)
      mainframe.rowconfigure(0, weight=1)
      mainframe.place(anchor=CENTER,relx=0.5,rely=0.5)

      Name = StringVar()
      Email = StringVar()
      Rnum = StringVar()

      name= Entry(mainframe, width=30, textvariable=Name)
      name.grid(row=0, column=1, sticky=W)
      name.bind('<Enter>', lambda event: name.config(bg="#eef0d5"))
      name.bind('<Leave>', lambda event: name.config(bg="white"))

      rnum = Entry(mainframe, width=30, textvariable=Rnum)
      rnum.grid(row=1, column=1, sticky=W)
      rnum.bind('<Enter>', lambda event: rnum.config(bg="#eef0d5"))
      rnum.bind('<Leave>', lambda event: rnum.config(bg="white"))

      email = Entry(mainframe, width=30, textvariable=Email)
      email.grid(row=2, column=1, sticky=W)
      email.bind('<Enter>', lambda event: email.config(bg="#eef0d5"))
      email.bind('<Leave>', lambda event: email.config(bg="white"))

      name_l = Label(mainframe, text="Name")
      name_l.grid(row=0, column=0, sticky=W)

      rnum_l = Label(mainframe, text="Roll Number")
      rnum_l.grid(row=1, column=0, sticky=W)

      email_l = Label(mainframe, text="Email")
      email_l.grid(row=2, column=0, sticky=W)

      def Submit(*args):
            try:
                  with open("loginDetails/details.txt",'a') as f:
                        f.write("Name: "+Name.get() + "\n" +"Roll_Num:"+ Rnum.get() + "\n" +"Email: "+ Email.get() + "\n\n")
                        Wind(root=root, text="Log in done")
            except FileNotFoundError:
                  pass

      
      submit = Button(mainframe, text="Submit", command=Submit)
      submit.grid(row=3, column=1, sticky=W)
      root.mainloop()
main_win = Tk()
main_win.title("Log In")
main_win.minsize(width=1000,height=1000)
backg = PhotoImage(file='img/bg.png')
bg_l = Label(main_win, image=backg)
bg_l.grid(row=0, column=0, sticky=W)
frame_prime = ttk.Frame(main_win,width=250,height=250)
frame_prime.place(anchor=CENTER, relx=0.5, rely=0.5)

frame_bg_l = Label(frame_prime,image=backg)
frame_bg_l.grid()
name = StringVar()
R_num = StringVar()                   

n = Entry(frame_bg_l, width=30, textvariable=name,relief=FLAT,borderwidth=0,bd=6)
n.bind('<Enter>', lambda event: n.config(bg="#eef0d5"))
n.bind('<Leave>', lambda event: n.config(bg="white"))
n.grid(row=0,column=1,sticky=W)

r = Entry(frame_bg_l, width=30, textvariable=R_num, relief=FLAT,borderwidth=0,bd=6)
r.bind('<Enter>', lambda event: r.config(bg="#eef0d5"))
r.bind('<Leave>', lambda event: r.config(bg="white"))

#LineBreak
br = Label(frame_bg_l,bg="#2F6997",width=30,height=1)
br.grid(row=1,column=1)

r.grid(row=2, column=1, sticky=W)

n_l = Label(frame_bg_l, text="Name",fg='white', bg='#2F6997',font=("Arial",18))
n_l.grid(row=0, column=0, sticky=W)

r_l = Label(frame_bg_l, text="Roll Number",fg='white', bg='#2F6997',font=("Noto",18))
r_l.grid(row=2, column=0, sticky=W)

def logIn(*args):
            with open("loginDetails/details.txt",'r') as f:
                  if name.get() == "" or R_num.get() == "":
                        warn = Label(frame_bg_l, text="Field can't be empty", fg="red", bg='#2F6997',font=("Arial", 16))
                        warn.grid(row=6, column=1, sticky=W)

                  elif (f"Name: {name.get()}\nRoll_Num: {R_num.get()}") in f.read() :
                        main_win.destroy()
                        code_pro()
                  else:
                        warn = Label(frame_bg_l, text="Wrong Details", fg="red", bg='#2F6997',font=("Arial", 16))
                        warn.grid(row=6, column=1, sticky=W)

logger = PhotoImage(file='img/login.png')
log = round_but.RoundedButton(frame_bg_l,30,30,15,0,None,"#2F6997",logIn,logger)
log.grid(row=3, column=0, sticky=W)

reg = PhotoImage(file='img/register-1.png')


temp_but = round_but.RoundedButton(frame_bg_l,120,30,15,0,None,"#2F6997",lambda: Regist(main_win),image=reg)
temp_but.grid(row=4,column=1,sticky=W)

qt = PhotoImage(file="img/quit.png")
quit_r = round_but.RoundedButton(frame_bg_l,30,30,15,0,None,"#2F6997",lambda: main_win.destroy(),qt)
quit_r.grid(row=3,column=1,sticky=W)

main_win.bind('<Return>',logIn)
main_win.mainloop()
