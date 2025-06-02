from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

class Courseclass():
    def __init__(self,root):
        self.root=root
        root.title("TEACHER PORTAL")
        root.geometry('1200x600+100+30')
        self.root.resizable(False, False)
        self.root.config(bg="white")
        root.wm_iconbitmap("images//icon.ico")
        self.root.focus_force()
        Label(self.root, text="Manage Course Details", font=("goudy ol style", 20, "bold"), bg="#033054",fg="white").place(x=0, y=0, relwidth=1, height=30)
        self.Llbl=Frame(self.root,bd=5,relief=RIDGE,bg="#0676ad")
        self.Llbl.place(x=0, y=30,height=570,width=600)
        self.Rlbl = Frame(self.root, bd=5, relief=RIDGE, bg="#e43b06")
        self.Rlbl.place(x=600, y=30, height=570, width=600)
        #====================LEFT LABEL=====================
        Label(self.Llbl,text="Update Homework",font=("helvetica",25,"bold"),fg="white",bg="#0676ad").place(x=130,y=10)
        Label(self.Llbl,text="Subject",font=("goudy old style",20,"bold"),fg="white",bg="#0676ad").place(x=10,y=80)
        self.txt_sub = ttk.Combobox(self.Llbl, font=("times new roman", 15),state="readonly",justify=CENTER)
        self.txt_sub["values"] = ("SELECT", "Maths", "Physics", "Chemistry", "English", "Computer Science")
        self.txt_sub.place(x=100, y=80, width=190, height=30)
        self.txt_sub.current(0)

        Label(self.Llbl,text="Date ",font=("goudy old style",20,"bold"),fg="white",bg="#0676ad").place(x=10,y=120)
        self.cal=DateEntry(self.Llbl,selectmode="day")
        self.cal.place(x=80,y=128)

        Label(self.Llbl, text="Date of submission ", font=("goudy old style", 20, "bold"), fg="white", bg="#0676ad").place(x=10,y=160)
        DateEntry(self.Llbl, selectmode="day").place(x=230, y=170)

        Label(self.Llbl, text="Select Details \n(If you want to) ", font=("goudy old style", 20, "bold"), fg="white", bg="#0676ad").place(x=10,y=200)
        l=Listbox(self.Llbl,selectmode=MULTIPLE,cursor="hand2")
        for i in ["Do neat and clean work","Do in homework section","Do in classwork section","Do in A4 sized sheet","Learn it also"]:
            a=1
            l.insert(a,i)
        l.place(x=200,y=200,width=200,height=100)

        Label(self.Llbl,text="Description",font=("goudy old style",20,"bold"),fg="white",bg="#0676ad").place(x=10,y=300)
        self.txt_desc=Text(self.Llbl,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=310,width=420,height=150)
        Button(self.Llbl,text="Send",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.root.destroy).place(x=240,y=470,width=110,height=40)

        #================Right Label====================
        Label(self.Rlbl, text="OTHER UPDATE", font=("helvetica", 25, "bold"), fg="white", bg="#e43b06").place(x=130,y=10)
        Label(self.Rlbl, text="Subject", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=58)
        self.txt_sub = ttk.Combobox(self.Rlbl, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_sub["values"] = ("SELECT", "Maths", "Physics", "Chemistry", "English", "Computer Science")
        self.txt_sub.place(x=100, y=60, width=180, height=30)
        self.txt_sub.current(0)
        Label(self.Rlbl, text="UPDATE RELATED TO", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=90)
        Button(self.Rlbl, text="COMPLAINT", font=("goudy old style", 10, "bold"), fg="white", bg="#2196f3",command=self.complaint).place(x=270,y=93)
        Button(self.Rlbl, text="ANNOUNCEMENT", font=("goudy old style", 10, "bold"), fg="white", bg="#4caf50",command=self.announcement).place(x=360,y=93)
        Button(self.Rlbl, text="TEST", font=("goudy old style", 10, "bold"), fg="white", bg="#607d8b",command=self.test).place(x=486,y=93)
        Button(self.Rlbl, text="OTHER", font=("goudy old style", 10, "bold"), fg="white", bg="#f44336",command=self.other).place(x=530,y=93)


    def complaint(self):
        Label(self.Rlbl, text="COMPLAINT RELATED TO", font=("goudy old style", 15, "bold"), fg="white",bg="#e43b06").place(x=10, y=140)
        self.txt_comp=ttk.Combobox(self.Rlbl,font=("times new roman", 15),state="readonly",justify=CENTER)
        self.txt_comp["values"] = ("SELECT", "Homework not completed", "Bad behaviour", "Rgular absentee", "Not focusing on studies")
        self.txt_comp.place(x=270, y=139, width=150, height=30)
        self.txt_comp.current(0)
        Label(self.Rlbl, text="OTHER", font=("goudy old style", 15, "bold"), fg="white",bg="#e43b06").place(x=10, y=183)
        Entry(self.Rlbl,font=("goudy old style", 15, "bold"),width=30).place(x=90,y=184)
        Label(self.Rlbl, text="Description", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=230)
        Text(self.Rlbl,font=("goudy old style", 15, "bold"),width=43,height=9).place(x=140,y=230)
        Button(self.Rlbl, text="Send", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.root.destroy).place(x=240, y=470, width=110, height=40)

    def announcement(self):
        Label(self.Rlbl, text="ANNOUNCEMENT RELATED TO", font=("goudy old style", 15, "bold"), fg="white",bg="#e43b06").place(x=10, y=140)
        self.txt_comp = ttk.Combobox(self.Rlbl, font=("times new roman", 15), state="readonly", justify=CENTER)
        self.txt_comp["values"] = ("SELECT", "Olympiad", "Inspection", "Syllabus updated", "Holidays homework", "Notebook checking")
        self.txt_comp.place(x=320, y=139, width=150, height=30)
        self.txt_comp.current(0)
        Label(self.Rlbl, text="OTHER", font=("goudy old style", 15, "bold"), fg="white", bg="#e43b06").place(x=10,y=180)
        Entry(self.Rlbl, font=("goudy old style", 15, "bold"), width=30).place(x=90, y=180)
        Label(self.Rlbl, text="DATE OF HAPPENING", font=("goudy old style", 15, "bold"), fg="white",bg="#e43b06").place(x=10, y=230)
        DateEntry(self.Rlbl, selectmode="day").place(x=228, y=234)
        Label(self.Rlbl, text="Description", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=270)
        Text(self.Rlbl, font=("goudy old style", 15, "bold"), width=43, height=9).place(x=140, y=270)
        Button(self.Rlbl, text="Send", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.root.destroy).place(x=260, y=490, width=110, height=40)

    def test(self):
        Label(self.Rlbl, text="DATE OF TEST", font=("goudy old style", 15, "bold"), fg="white", bg="#e43b06").place(x=10, y=140)
        DateEntry(self.Rlbl, selectmode="day").place(x=160, y=143)
        Label(self.Rlbl, text="Topic/Chapter", font=("goudy old style", 15, "bold"), fg="white", bg="#e43b06").place(x=10, y=180)
        Entry(self.Rlbl, font=("goudy old style", 15, "bold"), width=30).place(x=150, y=180)
        Label(self.Rlbl, text="Total Marks", font=("goudy old style", 15, "bold"), fg="white", bg="#e43b06").place(x=10,y=220)
        Entry(self.Rlbl, font=("goudy old style", 15, "bold"), width=6).place(x=120, y=220)
        Label(self.Rlbl, text="Description", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=270)
        Text(self.Rlbl, font=("goudy old style", 15, "bold"), width=43, height=9).place(x=140, y=270)
        Button(self.Rlbl, text="Send", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.root.destroy).place(x=260, y=490, width=110, height=40)

    def other(self):
        Label(self.Rlbl, text="WHAT RELATED TO", font=("goudy old style", 15, "bold"), fg="white", bg="#e43b06").place(x=10, y=140)
        Entry(self.Rlbl, font=("goudy old style", 15, "bold"), width=30).place(x=220, y=139)
        Label(self.Rlbl, text="Description", font=("goudy old style", 18, "bold"), fg="white", bg="#e43b06").place(x=10,y=190)
        Text(self.Rlbl, font=("goudy old style", 15, "bold"), width=43, height=9).place(x=140, y=193)
        Button(self.Rlbl, text="Send", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2",command=self.root.destroy).place(x=260, y=420, width=110, height=40)


if __name__=="__main__":
    root=Tk()
    obj=Courseclass(root)
    root.mainloop()