from tkinter import *
from PIL import Image,ImageTk
from stud_lgn_win import Login
from Ad_lgn_win import Adlogin
from teach_lgn_win import Tlogin

class main():
    def __init__(self,root):
        self.root=root
        self.root.title("Option window")
        self.root.geometry('860x540+190+30')
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("images//icon.ico")
        self.root.config(bg="#4A4848")
        image = Image.open("images\\Mpic.jpg")
        image = image.resize((200, 170), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        pic_lbl=Label(self.root, image=self.image,bg="white")
        pic_lbl.place(x=350, y=10, width=200, height=170)
        Label(self.root,bg="#4A4848",text="WHO'S USING THE APP?",font=("goudy old style",25 , "bold"),fg="white").place(x=250, y=200)

        Button(self.root, text="ADMIN", font=("goudy old style", 20, "bold"), bg="#eb5834", fg="white", cursor="hand2",bd=10,relief=RIDGE,command=self.admin_win).place(x=70, y=270, width=200, height=100)
        Button(self.root, text="TEACHER", font=("goudy old style", 20, "bold"), bg="#e4f2e5", fg="blue", cursor="hand2",bd=10,relief=RIDGE,command=self.teach_win).place(x=320, y=270, width=200, height=100)
        Button(self.root, text="STUDENT", font=("goudy old style", 20, "bold"), bg="#0c8518", fg="white", cursor="hand2",bd=10,relief=RIDGE,command=self.std_win).place(x=570, y=270, width=200, height=100)

    def std_win(self):
        self.root.destroy()
        self.new_win = Tk()
        self.new_obj = Login(self.new_win)

    def admin_win(self):
        self.root.destroy()
        self.new_win = Tk()
        self.new_obj = Adlogin(self.new_win)

    def teach_win(self):
        self.root.destroy()
        self.new_win = Tk()
        self.new_obj = Tlogin(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=main(root)
    root.mainloop()