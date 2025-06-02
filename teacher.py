from tkinter import *
from PIL import Image,ImageTk
from coursebtn import Courseclass
from studentbtn import Stuclass
from getresult import Resultclass

class T_win():
    def __init__(self,root):
        self.root=root
        root.title("TEACHER PORTAL")
        root.geometry('880x630+190+30')
        self.root.resizable(False, False)
        root.wm_iconbitmap("images//icon.ico")
        Label(self.root,text="Student management system",font=("goudy ol style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=30)
        m_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        m_frame.place(x=10,y=50,width=860,height=66)
        Button(m_frame,text="COURSE",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.courfunc).place(x=10,y=5,width=120,height=30)
        Button(m_frame,text="STUDENT",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.stufunc).place(x=145,y=5,width=120,height=30)
        Button(m_frame,text="RESULT",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.resultfunc).place(x=280,y=5,width=120,height=30)
        Button(m_frame,text="VIEW STDENT RESULT",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=415,y=5,width=250,height=30)
        Button(m_frame,text="UPDATE",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=680,y=5,width=120,height=30)
        Label(self.root, text="SDMS-Sudent Data Management System \nIf any Tachnical Issue raised please contact uttam singh class:12A ", font=("goudy ol style", 12), bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        bg_image=Image.open("images\\Tpic.jpg")
        bg_image=bg_image.resize((550,350),Image.Resampling.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(bg_image)
        Label(self.root,image=self.bg_image).place(x=320,y=120,width=550,height=350)
        self.lbl_stu=Label(self.root,text=f"Total Students\n[]",font=("goudy old style",20 ),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_stu.place(x=370,y=480,width=200,height=90)
        self.lbl_pres = Label(self.root, text="Total Present\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE,bg="#038074", fg="white")
        self.lbl_pres.place(x=590,y=480,width=200,height=90)
        self.sdlbl=Frame(self.root,bd=5,relief=RIDGE,bg="#0676ad")
        self.sdlbl.place(x=10,y=120,width=300,height=460)
        a,b,c,d,e,f="","","","","",""
        Label(self.sdlbl,text=f"Class={a}",bg="#0676ad",fg="White",font=("goudy old style",13,"bold")).place(x=10,y=5)
        Label(self.sdlbl,text=f"Section={b}",bg="#0676ad",fg="White",font=("goudy old style",13,"bold")).place(x=10,y=35)
        Label(self.sdlbl,text=f"Last Updated={c}",bg="#0676ad",fg="White",font=("goudy old style",13,"bold")).place(x=10,y=65)
        Label(self.sdlbl,text=f"Updated By={d}",bg="#0676ad",fg="White",font=("goudy old style",13,"bold")).place(x=10,y=95)

    def courfunc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Courseclass(self.new_win)

    def stufunc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Stuclass(self.new_win)

    def resultfunc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Resultclass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj1=T_win(root)
    root.mainloop()