from functools import wraps
from os import system
from tkinter import *
from tkinter import ttk
from tkcode import CodeEditor
from tkinter.filedialog import asksaveasfile, test
import time
from .quit_dia import *
from .file_runner import *
from .round_but import *

def change_text(label,text):
      label.text.set("heyy")

def save():
      files = [('All Files', '*.*'), 
                   ('Python Files', '*.py'),
                   ('Text Document', '*.txt'),
                   ('C++ Files', '*.cpp'),
                   ('C Files', '*.c'),
                   ]
      file = asksaveasfile(filetypes = files, defaultextension = files)

def Timer(*args, Time,Lab):
      for i in range(Time):
            time.sleep(60)
            Lab.configure(text="Remaining Time:"+Time-1+"min")

def Submit_code(*args,announce,**kwargs):
      try:
            
            if kwargs['language'] == "Python":
                  output_obtainer_py(Codes=kwargs['code'])
            elif kwargs['language'] == "C++":
                  output_obtainer_cpp(Codes=kwargs['code'])
            elif kwargs['language'] == "C":
                  output_obtainer_c(Codes=kwargs['code'])
            louder = StringVar()
            var =result(output=open('Submissions/output.txt','r'),true_output=open('Submissions/output.txt','r'))
            print(var+"-Var")
            louder.set(var)
            announce['text']=louder.get()
            announce.after(0)
      except FileNotFoundError:
            extension = "py"
            if kwargs['language'] == "C++":
                  extension = "cpp"
            elif kwargs['language'] == "C":
                  extension = "c"
            with open("Submissions/Temp."+extension,"w") as f:
                  f.write(kwargs['code'])
            system("touch Submission."+extension)
def code_pro(*arg):
      root = Tk()
      root.minsize(width=1000,height=10)
      root.maxsize(height=60)
      root.rowconfigure(2, weight=2)
      root.columnconfigure(0, weight=2)
      
      notebook = ttk.Notebook(root)
      Butt_frame = Frame(root,width=1000,height=30)

      lang = StringVar()
      lang.set("Python")

      list = OptionMenu(Butt_frame,lang,"C++","C","Python")
      list.grid(row=0, column=0, sticky=W)

      Sub = Button(Butt_frame, text="Submit",relief=FLAT)
      Sub.grid(row=0, column=1, sticky=W)

      save_copy = Button(Butt_frame, text='Save on device', command=save,relief=FLAT)
      save_copy.grid(row=0, column=2,sticky=W)

      Quit = Button(Butt_frame, text='Quit Challenge', command=lambda:quit_conf(root=root), bg='Red', fg='White',relief=FLAT)
      Quit.grid(row=0, column=3, sticky=W)

      Right_s = Label(width=50,height=110)
      Right_s.grid(row=1,column=1)
      Right_s.grid_anchor(N)

      test_cases=Label(Right_s,width=50,height=40)
      test_cases.grid(row=0,column=0,sticky=N)
      with open('TestCases/TestCases.txt','r') as f:
            test_text = Label(test_cases,width=30,height=40,text=f.read())
            test_text.grid(row=0,column=0,sticky=N)

      bottom_touch = Label(Right_s,width=50,height=80)
      bottom_touch.grid(row=1,column=0,sticky=N)

      loud=StringVar()
      loud.set("No Output yet")
      announce = Label(bottom_touch,bg="green",width=50,height=10,text=loud.get())
      if lang.get() =="Python":
            CE = CodeEditor(notebook,width=100,height=80,background="black",font="Arial",language="Python",highlighter="dracula",autofocus=True,blockcursor=False,insertofftime=0,padx=10,pady=10)
            CE.pack(fill=BOTH, expand=1)
            Sub.config(command=lambda:Submit_code(code=CE.get(1.0,END),language=lang.get(),announce=announce))

      elif lang.get() =="C++":
            CE = CodeEditor(notebook,width=100,height=80,background="black",font="Arial",language="C++",highlighter="dracula",autofocus=True,blockcursor=False,insertofftime=0,padx=10,pady=10)
            CE.pack(fill=BOTH, expand=1)
            Sub.config(command=lambda:Submit_code(code=CE.get(1.0,END),language=lang.get(),announce=announce))
      elif lang.get() =="C":
            CE = CodeEditor(notebook,width=100,height=80,background="black",font="Arial",language="C",highlighter="dracula",autofocus=True,blockcursor=False,insertofftime=0,padx=10,pady=10)
            CE.pack(fill=BOTH, expand=1)
            Sub.config(command=lambda:Submit_code(code=CE.get(1.0,END),language=lang.get(),annuounce=announce))
      announce.grid(row=0,column=0,sticky=N)
      Butt_frame.grid(row=0, column=0, sticky='nesw')
      notebook.grid(row=1, column=0, sticky='nswe')
      announce.after(0)
      root.option_add("*tearOff", TRUE)
      root.update()
      root.resizable()
      root.mainloop()