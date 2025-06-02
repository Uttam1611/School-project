from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pymysql


class Stuclass():
    def __init__(self, root):
        self.root = root
        root.title("TEACHER PORTAL")
        root.geometry('1200x600+100+30')
        self.root.resizable(False, False)
        self.root.config(bg="white")
        root.wm_iconbitmap("images//icon.ico")
        self.root.focus_force()
        Label(self.root, text="Manage Student Details", font=("times new roman", 20, "bold"), bg="#0c524f",fg="white").place(x=0, y=0, relwidth=1, height=30)

        self.Llbl = Frame(self.root, relief=RIDGE, bg="white")
        self.Llbl.place(x=0, y=30, height=570, width=700)
        self.Rlbl = Frame(self.root, relief=RIDGE, bg="white")
        self.Rlbl.place(x=700, y=30, height=570, width=500)
        # =============LEFT LABEL===============
        Label(self.Llbl, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=30)
        Label(self.Llbl, text="Admission no", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5,y=70)
        Label(self.Llbl, text="Fathers name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5,y=110)
        Label(self.Llbl, text="Mothers Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5,y=150)
        Label(self.Llbl, text="D.O.B", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=190)
        Label(self.Llbl, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=270)
        Label(self.Llbl, text="Ph no", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=230)
        Label(self.Llbl, text="Roll no", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=30)
        Label(self.Llbl, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=70)
        Label(self.Llbl, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=110)
        Label(self.Llbl, text="Category", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=150)
        Label(self.Llbl, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=190)

        self.var_name = StringVar()
        self.var_Fname = StringVar()
        self.var_Mname = StringVar()
        self.var_rollno = StringVar()
        self.var_admissionno = StringVar()
        self.var_password = StringVar()
        self.var_username = StringVar()
        self.var_phno = StringVar()


        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_name, bg="light yellow",width=20).place(x=140, y=30)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_admissionno, bg="light yellow",width=20).place(x=140, y=70)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable= self.var_Fname, bg="light yellow", width=20).place(x=140, y=110)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable= self.var_Mname, bg="light yellow", width=20).place(x=140, y=150)
        self.txt_rollno=Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_rollno, bg="light yellow",width=20)
        self.txt_rollno.place(x=465, y=30)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_username, bg="light yellow",width=20).place(x=465, y=70)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_password, bg="light yellow",width=20).place(x=465, y=110)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_phno, bg="light yellow",width=20).place(x=140, y=230)

        self.cat = ttk.Combobox(self.Llbl, font=("times new roman", 10),state="readonly",justify=CENTER)
        self.cat["values"] = ("SELECT", "General","Sc/St","Obc")
        self.cat.place(x=465, y=150, width=90, height=25)
        self.cat.current(0)

        self.cal=DateEntry(self.Llbl, selectmode="day")
        self.cal.place(x=140, y=190)

        self.gen = ttk.Combobox(self.Llbl, font=("times new roman", 10),state="readonly",justify=CENTER)
        self.gen["values"] = ("SELECT", "Male",'Female',"Transgender","other")
        self.gen.place(x=465, y=190, width=90, height=25)
        self.gen.current(0)

        self.ad=Text(self.Llbl, font=("times new roman", 15, "bold"), bg="light yellow", height=9, width=50)
        self.ad.place(x=140,y=270)

        self.btn_add=Button(self.Llbl, text="SAVE", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=100,y=490,width=110,height=40)
        self.btn_update=Button(self.Llbl, text="UPDATE", font=("goudy old style", 15, "bold"), bg="#3c966b", fg="white", cursor="hand2",command=self.update)
        self.btn_update.place(x=220, y=490, width=110, height=40)
        self.btn_delete=Button(self.Llbl, text="DELETE", font=("goudy old style", 15, "bold"), bg="#4200d1", fg="white", cursor="hand2",command=self.delete)
        self.btn_delete.place(x=340, y=490, width=110, height=40)
        self.btn_clear=Button(self.Llbl, text="CLEAR", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.clear)
        self.btn_clear.place(x=460, y=490, width=110, height=40)
        # =================RIGHT LABEL======================
        self.search_var = StringVar()
        Label(self.Rlbl, text="Search by | Student Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=10)
        Entry(self.Rlbl, textvariable=self.search_var, font=("goudy old style", 15, "bold"), bg="light yellow",width=18).place(x=240, y=12)
        Button(self.Rlbl, text="Search", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.search).place(x=430, y=8)
        self.C_frame = Frame(self.Rlbl, bd=2, relief=RIDGE)
        self.C_frame.place(x=10, y=60, width=470, height=390)

        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        self.studenttable = ttk.Treeview(self.C_frame, column=("roll no", "name", "admission no"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.studenttable.yview)
        self.studenttable.heading("roll no", text="Roll no")
        self.studenttable.heading("name", text="Student name")
        self.studenttable.heading("admission no", text="Admission no")
        self.studenttable["show"] = "headings"
        self.studenttable.column("roll no", width=50)
        self.studenttable.column("name", width=100)
        self.studenttable.column("admission no", width=50)
        self.studenttable.pack(fill=BOTH, expand=1)
        self.studenttable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    # =========================================================
    def delete(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_rollno.get()=="" or self.var_admissionno.get()=="" or self.var_username.get()=="" or self.var_password.get()=="" or self.cat.get()=="SELECT" or self.gen.get()=="SELECT" :
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from class12A where roll_no=%s", self.var_rollno.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("ERROR", 'USER DOES NOT EXIST.\n PLEASE SELECT FROM THE LIST')
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete")
                    if op == True:
                        cur.execute("delete from class12A where roll_no=%s",(self.var_rollno.get()))
                        con.commit()
                        messagebox.showinfo("Deleted","Student details deleted successfully",parent=self.root)
                        self.clear()


            except Exception as es:
                messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_admissionno.set("")
        self.var_Fname.set("")
        self.var_Mname.set("")
        self.var_username.set("")
        self.var_password.set("")
        self.cat.current(0)
        self.gen.current(0)
        self.ad.delete("1.0", END)
        self.txt_rollno.config(state=NORMAL)
        self.search_var.set("")
        self.var_phno.set("")

    def get_data(self,ev):
        self.txt_rollno.config(state="readonly")
        r=self.studenttable.focus()
        content=self.studenttable.item(r)
        row=content["values"]
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_admissionno.set(row[2])
        self.var_Fname.set(row[3])
        self.var_Mname.set(row[4])
        self.var_username.set(row[5])
        self.var_password.set(row[6])
        curval1= 0
        for i in self.cat["values"]:
            if i==row[8]:
                self.cat.current(curval1)
            else:
                curval1+=1
        curval2 = 0
        for j in self.gen["values"]:
            if j==row[9]:
                self.gen.current(curval2)
            else:
                curval2+=1
        self.ad.delete("1.0",END)
        self.ad.insert(END,row[10])
        self.var_phno.set(row[11])

    def add(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_rollno.get()=="" or self.var_admissionno.get()=="" or self.var_username.get()=="" or self.var_password.get()=="" or self.cat.get()=="SELECT" or self.gen.get()=="SELECT" or self.var_phno.get()=="":
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from class12A where roll_no=%s", self.var_rollno.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("ERROR", 'USER ALREADY EXIST.\n PLEASE FILL CORRECT DETAILS')
                else:
                    cur.execute("insert into class12A (roll_no,student_name,admission_no,fathers_name,mothers_name,username,password,date_of_birth,caste,gender,address,Ph_no) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_rollno.get(),
                                self.var_name.get(),
                                self.var_admissionno.get(),
                                self.var_Fname.get(),
                                self.var_Mname.get(),
                                self.var_username.get(),
                                self.var_password.get(),
                                self.cal.get_date(),
                                self.cat.get(),
                                self.gen.get(),
                                self.ad.get("1.0",END),
                                self.var_phno.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful")
                    self.show()
            except Exception as es:
                messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def show(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="school")
            cur = con.cursor()
            cur.execute("select * from class12A ")
            rows = cur.fetchall()
            self.studenttable.delete(*self.studenttable.get_children())
            self.stucount=0
            for row in rows:
                self.studenttable.insert("",END,values=row)
                self.stucount+=1
        except Exception as es:
            messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def update(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_rollno.get()=="" or self.var_admissionno.get()=="" or self.var_username.get()=="" or self.var_password.get()=="" or self.cat.get()=="SELECT" or self.gen.get()=="SELECT":
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from class12A where roll_no=%s", self.var_rollno.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("ERROR", 'USER DOES NOT EXIST.\n PLEASE SELECT FROM THE LIST')
                else:
                    cur.execute("update class12A set student_name=%s,admission_no=%s,fathers_name=%s,mothers_name=%s,username=%s,password=%s,date_of_birth=%s,caste=%s,gender=%s,address=%s,Ph_no=%s where roll_no=%s",
                                (self.var_name.get(),
                                 self.var_admissionno.get(),
                                 self.var_Fname.get(),
                                 self.var_Mname.get(),
                                 self.var_username.get(),
                                 self.var_password.get(),
                                 self.cal.get_date(),
                                 self.cat.get(),
                                 self.gen.get(),
                                 self.ad.get("1.0",END),
                                 self.var_phno.get(),
                                 self.var_rollno.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "updated Successful")
                    self.show()
            except Exception as es:
                messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="school")
            cur = con.cursor()
            cur.execute(f"select * from class12A where student_name LIKE '%{self.search_var.get()}%'")
            rows = cur.fetchall()
            self.studenttable.delete(*self.studenttable.get_children())
            self.stucount=0
            for row in rows:
                self.studenttable.insert("",END,values=row)
                self.stucount+=1
        except Exception as es:
            messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Stuclass(root)
    root.mainloop()


