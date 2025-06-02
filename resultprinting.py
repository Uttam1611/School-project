from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from openpyxl import *
from openpyxl.styles import Font,Border,Side,PatternFill

class Resultclass():
    def __init__(self,root):
        self.root=root
        root.title("TEACHER PORTAL")
        root.geometry('1200x630+100+30')
        self.root.resizable(False, False)
        self.root.config(bg="white")
        root.wm_iconbitmap("images//icon.ico")
        self.root.focus_force()
        Label(self.root, text="GET STUDENT RESULT", font=("goudy ol style", 20, "bold"), bg="#05fffb",fg="#262626").place(x=0, y=0, relwidth=1, height=40)
        Label(self.root, text="Search by | Roll No", font=("goudy old style", 15, "bold"), bg="white").place(x=5,y=50)
        self.search_var=StringVar()
        Entry(self.root, textvariable=self.search_var, font=("goudy old style", 15, "bold"), bg="light yellow",width=18).place(x=180, y=50)


if __name__=="__main__":
    root=Tk()
    obj=Resultclass(root)
    root.mainloop()