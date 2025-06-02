from tkinter import *
from tkinter import messagebox
from admin import Admin

class Adlogin():
    def __init__(self,root):
        self.root=root
        self.root.title("SIGNUP")
        self.root.geometry('650x500+350+90')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("images//icon.ico")
        self.root.config(bg="black")
        self.img=PhotoImage(file="images\\logsdph.png")
        Label(self.root,image=self.img, borderwidth=0, bg="black").place(x=280,y=10)
        Frame_login=Frame(self.root,bg="black")
        Frame_login.place(x=0, y=130,height=470,width=700)
        Label(Frame_login,text="Please fill all informations",font=("HELVETICA", 15,"bold"),bg="black",fg="white").place(x=210,y=5)

        Label(Frame_login, text="ADMIN ID", font=("Goudy old style", 15, "bold"), background="black",fg="white").place(x=150, y=60)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_user.place(x=153, y=90, width=356, height=25)

        Label(Frame_login, text="ADMIN PASSWORD", font=("Goudy old style", 15, "bold"), background="black",fg="white").place(x=150, y=140)
        self.txt_passwd = Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.txt_passwd.place(x=153, y=170, width=356, height=25)

        Submit=Button(self.root, text="SUBMIT", bg="#1138fa", fg="white", width=20, borderwidth=0, font=("HELVETICA", 12, "bold"), cursor="hand2", command=self.checkdata)
        Submit.place(x=225,y=370)

    def checkdata(self):
        if self.txt_passwd.get()=="" or self.txt_user.get()=="" :
            messagebox.showerror("ERROR",'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            if self.txt_user.get()=="admin" and self.txt_passwd.get()=="admin123":
                messagebox.showinfo("WELCOME", 'Welcome admin')
                self.admin_win()
            else:
                messagebox.showerror("ERROR", 'INCORRECT ID OR PASSWORD \n PLEASE FILL ALL DETAILS')

    def admin_win(self):
        self.root.destroy()
        self.new_win = Tk()
        self.new_obj = Admin(self.new_win)



if __name__=="__main__":
    root=Tk()
    obj=Adlogin(root)
    root.mainloop()
