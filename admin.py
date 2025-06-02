from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pymysql


class Admin():
    def __init__(self, root):
        self.root = root
        root.title("ADMIN PORTAL")
        root.geometry('1200x600+100+30')
        self.root.resizable(False, False)
        self.root.config(bg="white")
        root.wm_iconbitmap("images//icon.ico")
        self.root.focus_force()
        self.Llbl = Frame(self.root, relief=RIDGE, bg="white")
        self.Llbl.place(x=0, y=30, height=570, width=700)
        self.Rlbl = Frame(self.root, relief=RIDGE, bg="white")
        self.Rlbl.place(x=700, y=30, height=570, width=500)
        Label(self.root, text="Manage Teacher Details", font=("times new roman", 20, "bold"), bg="#0c524f",
              fg="white").place(x=0, y=0, relwidth=1, height=30)
        # =============LEFT LABEL===============

        # ====================LEFT SIDE==============
        Label(self.Llbl, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=30)
        Label(self.Llbl, text="Mothers name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5,y=70)
        Label(self.Llbl, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5,y=110)
        Label(self.Llbl, text="Ph no", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=150)
        Label(self.Llbl, text="Classes", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=190)
        Label(self.Llbl, text="(Please enter values like 12A,7B...) ", font=("times new roman", 15, "bold"), bg="white",fg="black").place(x=5, y=230)
        Label(self.Llbl, text="D.O.B", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=270)
        # ==================RIGHT SIDE==========================
        Label(self.Llbl, text="Unique id", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=30)
        Label(self.Llbl, text="Fathers name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=70)
        Label(self.Llbl, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=110)
        Label(self.Llbl, text="Category", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=150)
        Label(self.Llbl, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=190)
        Label(self.Llbl, text="Subject", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=230)
        Label(self.Llbl, text="Class teacher", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=360,y=270)
        # ===========LEFT ENTRIES VARIABLES==================
        self.var_name = StringVar()
        self.var_Mname = StringVar()
        self.var_username = StringVar()
        self.var_phno = StringVar()
        self.var_classes = StringVar()

        # ===========RIGHT ENTRIES VARIABLES==================
        self.var_uniqueid = StringVar()
        self.var_Fname = StringVar()
        self.var_password = StringVar()

        # ===========LEFT ENTRIES ==================
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_name, bg="light yellow",width=20).place(x=140, y=30)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_Mname, bg="light yellow",width=20).place(x=140, y=70)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_username, bg="light yellow",width=20).place(x=140, y=110)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_phno, bg="light yellow",width=20).place(x=140, y=150)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_classes, bg="light yellow",width=20).place(x=140, y=190)
        self.cal = DateEntry(self.Llbl, selectmode="day")
        self.cal.place(x=140, y=270)

        # ===========RIGHT ENTRIES ==================
        self.unid=Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_uniqueid, bg="light yellow",width=20)
        self.unid.place(x=495, y=30)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_Fname, bg="light yellow",width=20).place(x=495, y=70)
        Entry(self.Llbl, font=("times new roman", 15, "bold"), textvariable=self.var_password, bg="light yellow",width=20).place(x=495, y=110)

        self.cat = ttk.Combobox(self.Llbl, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.cat["values"] = ("SELECT", "General", "Sc/St", "Obc")
        self.cat.place(x=495, y=150, width=90, height=25)
        self.cat.current(0)

        self.gen = ttk.Combobox(self.Llbl, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.gen["values"] = ("SELECT", "Male", 'Female', "Transgender", "other")
        self.gen.place(x=495, y=190, width=90, height=25)
        self.gen.current(0)

        self.sub = ttk.Combobox(self.Llbl, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.sub["values"] = ("SELECT", "Maths", 'Physics', "English", "Chemistry", "Computer science", "Physical education" )
        self.sub.place(x=495, y=230, width=110, height=25)
        self.sub.current(0)

        self.T_class = ttk.Combobox(self.Llbl, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.T_class["values"] = ("SELECT", "12")
        self.T_class.place(x=495, y=270, width=70, height=25)
        self.T_class.current(0)
        self.T_sec = ttk.Combobox(self.Llbl, font=("times new roman", 10), state="readonly", justify=CENTER)
        self.T_sec["values"] = ("SELECT", "A", 'B', "C", "D", "E", "F")
        self.T_sec.place(x=575, y=270, width=70, height=25)
        self.T_sec.current(0)
        # =================ADDRESS=========================
        Label(self.Llbl, text="Address", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=5, y=310)
        self.ad=Text(self.Llbl, font=("times new roman", 15, "bold"), bg="light yellow", height=7, width=50)
        self.ad.place(x=140,y=310)
        # ======================BUTTONS=======================
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
        Label(self.Rlbl, text="Search by | Teacher Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10,y=10)
        Entry(self.Rlbl, textvariable=self.search_var, font=("goudy old style", 15, "bold"), bg="light yellow",width=18).place(x=240, y=12)
        Button(self.Rlbl, text="Search", font=("goudy old style", 12, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.search).place(x=430, y=8)
        self.C_frame = Frame(self.Rlbl, bd=2, relief=RIDGE)
        self.C_frame.place(x=10, y=60, width=470, height=390)

        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        self.teachertable = ttk.Treeview(self.C_frame, column=("Unique id", "teacher name", "class teacher"), yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)

        scrolly.config(command=self.teachertable.yview)
        self.teachertable.heading("Unique id", text="Unique id")
        self.teachertable.heading("teacher name", text="Teacher name")
        self.teachertable.heading("class teacher", text="Class teacher")
        self.teachertable["show"] = "headings"
        self.teachertable.column("Unique id", width=50)
        self.teachertable.column("teacher name", width=100)
        self.teachertable.column("class teacher", width=50)
        self.teachertable.pack(fill=BOTH, expand=1)
        self.teachertable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # =========================================================
    def delete(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_uniqueid.get()=="" or self.var_username.get()== "" or self.var_password.get()== "" or self.cat.get()== "SELECT" or self.gen.get()== "SELECT" or self.var_phno.get()== "" or self.T_class.get()=="SELECT" or self.T_sec.get()=="SELECT" or self.var_classes=="" or self.sub.get()=="SELECT" or self.ad.get("1.0",END)=="":
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from teacherclass12A where unique_id=%s", self.unid.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("ERROR", 'USER DOES NOT EXIST.\n PLEASE SELECT FROM THE LIST')
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete")
                    if op == True:
                        cur.execute("delete from teacherclass12A where unique_id=%s",(self.unid.get()))
                        con.commit()
                        messagebox.showinfo("Deleted","Student details deleted successfully",parent=self.root)
                        self.clear()


            except Exception as es:
                messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def clear(self):
        self.show()
        self.var_uniqueid.set(""),
        self.var_name.set(""),
        self.T_class.current(0),
        self.T_sec.current(0),
        self.var_username.set(''),
        self.var_password.set(''),
        self.var_phno.set(''),
        self.var_classes.set(''),
        self.var_Fname.set(''),
        self.var_Mname.set(''),
        self.cat.current(0),
        self.gen.current(0),
        self.sub.current(0),
        self.ad.delete("1.0", END),

    def get_data(self,ev):
        self.unid.config(state="readonly")
        r=self.teachertable.focus()
        content=self.teachertable.item(r)
        row=content["values"]
        self.var_uniqueid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_username.set(row[3]),
        self.var_password.set(row[4]),
        self.var_phno.set(row[5]),
        self.var_classes.set(row[6])
        self.var_Fname.set(row[8]),
        self.var_Mname.set(row[9]),
        curval1= 0
        for i in self.cat["values"]:
            if i==row[10]:
                self.cat.current(curval1)
            else:
                curval1+=1
        curval2 = 0
        for j in self.gen["values"]:
            if j==row[11]:
                self.gen.current(curval2)
            else:
                curval2+=1

        curval3 = 0
        for i in self.sub["values"]:
            if i == row[12]:
                self.sub.current(curval3)
            else:
                curval3 += 1

        a=list(row[2])
        b=a.pop()
        c="".join(a)
        curval4 = 0
        for i in self.T_class["values"]:
            if i ==c:
                self.T_class.current(curval4)
            else:
                curval4 += 1

        curval5 = 0
        for i in self.T_sec["values"]:
            if i == b:
                self.T_sec.current(curval5)
            else:
                curval5 += 1

        self.ad.delete("1.0",END)
        self.ad.insert(END,row[13])

    def add(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_uniqueid.get()=="" or self.var_username.get()== "" or self.var_password.get()== "" or self.cat.get()== "SELECT" or self.gen.get()== "SELECT" or self.var_phno.get()== "" or self.T_class.get()=="SELECT" or self.T_sec.get()=="SELECT" or self.var_classes=="" or self.sub.get()=="SELECT" or self.ad.get("1.0",END)=="":
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from teacherclass12a where unique_id=%s", self.var_uniqueid.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("ERROR", 'USER ALREADY EXIST.\n PLEASE FILL CORRECT DETAILS')
                else:
                    self.classt=f"{self.T_class.get()}"+f"{self.T_sec.get()}"
                    cur.execute("insert into teacherclass12a (unique_id,teacher_name,class_teacher,username,password,Ph_no,classes,date_of_birth,fathers_name,mothers_name,category,gender,subject,address) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_uniqueid.get(),
                                 self.var_name.get(),
                                 self.classt,
                                 self.var_username.get(),
                                 self.var_password.get(),
                                 self.var_phno.get(),
                                 self.var_classes.get(),
                                 self.cal.get_date(),
                                 self.var_Fname.get(),
                                 self.var_Mname.get(),
                                 self.cat.get(),
                                 self.gen.get(),
                                 self.sub.get(),
                                 self.ad.get("1.0", END),
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
            cur.execute("select * from teacherclass12a")
            rows = cur.fetchall()
            self.teachertable.delete(*self.teachertable.get_children())
            self.teachcount=0
            for row in rows:
                self.teachertable.insert("", END, values=row)
                self.teachcount+=1
        except Exception as es:
            messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def update(self):
        if self.var_name.get()=="" or self.var_Fname.get()=="" or self.var_Mname.get()=="" or self.var_uniqueid.get()=="" or self.var_username.get()== "" or self.var_password.get()== "" or self.cat.get()== "SELECT" or self.gen.get()== "SELECT" or self.var_phno.get()== "" or self.T_class.get()=="SELECT" or self.T_sec.get()=="SELECT" or self.var_classes=="" or self.sub.get()=="SELECT" or self.ad.get("1.0",END)=="":
            messagebox.showerror("ERROR", 'ALL FIELDS ARE REQUIRED \n PLEASE FILL ALL DETAILS')
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="school")
                cur = con.cursor()
                cur.execute("select * from teacherclass12a where unique_id=%s", self.var_uniqueid.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("ERROR", 'USER DOES NOT EXIST.\n PLEASE SELECT FROM THE LIST')
                else:
                    self.classt = f"{self.T_class.get()}" + f"{self.T_sec.get()}"
                    cur.execute("update teacherclass12a set teacher_name=%s,class_teacher=%s,username=%s,password=%s,Ph_no=%s,classes=%s,date_of_birth=%s,fathers_name=%s,mothers_name=%s,category=%s,gender=%s,subject=%s,address=%s where unique_id=%s",
                                (self.var_name.get(),
                                 self.classt,
                                 self.var_username.get(),
                                 self.var_password.get(),
                                 self.var_phno.get(),
                                 self.var_classes.get(),
                                 self.cal.get_date(),
                                 self.var_Fname.get(),
                                 self.var_Mname.get(),
                                 self.cat.get(),
                                 self.gen.get(),
                                 self.sub.get(),
                                 self.ad.get("1.0", END),
                                 self.var_uniqueid.get(),
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Updated Successful")
                    self.show()
            except Exception as es:
                messagebox.showerror("error", f"Error due to {str(es)}", parent=self.root)

    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="school")
            cur = con.cursor()
            cur.execute(f"select * from teacherclass12a where teacher_name LIKE '%{self.search_var.get()}%'")
            rows = cur.fetchall()
            self.teachertable.delete(*self.teachertable.get_children())
            for row in rows:
                self.teachertable.insert("", END, values=row)
        except Exception as es:
            messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()


