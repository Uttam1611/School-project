from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from teacher import T_win

class Tlogin():
    def __init__(self,root):
        self.root=root
        self.root.title("SIGNUP")
        self.root.geometry('880x630+190+30')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("images//icon.ico")
        self.root.config(bg="black")
        self.img=PhotoImage(file="images\\logsdph.png")
        Label(self.root,image=self.img, borderwidth=0, bg="black").place(x=390,y=10)
        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=100, y=110,height=470,width=700)
        Label(Frame_login,text="Please fill all informations",font=("HELVETICA", 15,"bold"),bg="black",fg="white").place(x=210,y=5)

        Label(Frame_login, text="TEACHER NAME", font=("Goudy old style", 15, "bold"), background="black", fg="white").place(x=150,y=60)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_user.place(x=153,y=90,width=356,height=25)

        Label(Frame_login, text="USERNAME", font=("Goudy old style", 15, "bold"), background="black",fg="white").place(x=150, y=130)
        self.txt_username = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_username.place(x=153, y=160, width=356, height=25)

        Label(Frame_login, text="PASSWORD", font=("Goudy old style", 15, "bold"), background="black",fg="white").place(x=150, y=200)
        self.txt_passwd = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_passwd.place(x=153, y=230, width=356, height=25)

        Label(Frame_login, text="SECTION", font=("Goudy old style", 15, "bold"), background="black", fg="white").place(x=150, y=340)
        self.txt_sec = ttk.Combobox(Frame_login, font=("times new roman", 10),state="readonly")
        self.txt_sec["values"] = ("SELECT", "A")
        self.txt_sec.place(x=250, y=342, width=70, height=25)
        self.txt_sec.current(0)

        Label(Frame_login, text="CLASS", font=("Goudy old style", 15, "bold"), background="black", fg="white").place(x=368, y=340)
        self.txt_class = ttk.Combobox(Frame_login, font=("times new roman", 10),state="readonly",justify=CENTER)
        self.txt_class["values"]=("SELECT","12")
        self.txt_class.place(x=440, y=342, width=70, height=25)
        self.txt_class.current(0)

        Label(Frame_login, text="UNIQUE ID", font=("Goudy old style", 15, "bold"), background="black", fg="white").place(x=150, y=270)
        self.txt_roll = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_roll.place(x=153, y=300, width=356, height=25)

        Submit=Button(self.root, text="SUBMIT", bg="#1138fa", fg="white", width=20, borderwidth=0, font=("HELVETICA", 12, "bold"), cursor="hand2", command=self.checkdata)
        Submit.place(x=340,y=520)

    def checkdata(self):
        if self.txt_roll.get()=="" or self.txt_sec.get()=="SELECT" or self.txt_class.get()=="SELECT" or self.txt_passwd.get()=="" or self.txt_user.get()=="" :
            messagebox.showerror("ERROR",'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="school")

                cur=con.cursor()
                cur.execute(f"select * from teacherclass{self.txt_class.get()}{self.txt_sec.get()} where unique_id=%s and teacher_name=%s and username=%s and password=%s",(
                    self.txt_roll.get(),
                    self.txt_user.get(),
                    self.txt_username.get(),
                    self.txt_passwd.get()
                ))

                row=cur.fetchone()
                if row!=None:
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", f"Welcome {self.txt_user.get()}")
                    self.root.destroy()
                    self.subfunc()

                else:
                    messagebox.showerror("ERROR", 'Incorrect Username or password.\n PLEASE FILL CORRECT DETAILS')

            except Exception as es:
                messagebox.showerror("error",f"Error due to {str(es)}",parent=self.root)


    def subfunc(self):
        self.new_win=Tk()
        self.new_obj=T_win(self.new_win)
if __name__=="__main__":
    root=Tk()
    obj=Tlogin(root)
    root.mainloop()
