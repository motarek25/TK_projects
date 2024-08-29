# auto-py-to-exe
from tkinter import *
from functools import partial
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import random
import random2
from datetime import *


mydb = mysql.connector.connect(host="localhost", user="root", database="Attendance", password="root")
mycoursor = mydb.cursor()
# mycoursor.execute("DROP TABLE attend")
# mycoursor.execute("DROP TABLE attends")
mycoursor.execute("CREATE TABLE if not exists attend(name text,work_hours INT,title text ,code text,id INT PRIMARY KEY AUTO_INCREMENT)")
mycoursor.execute("CREATE TABLE if not exists attends(id text,attend int ,late text,day int ,mon int ,year int)")
# print(mycoursor)
att= Tk()  
att.geometry('370x125')  
att.title('Attendance Form ')
def log():
    att_l= Toplevel()    
    att_l.geometry('370x200')  
    att_l.title('Attendance Form ')
    Label(att_l, text="Log in",fg="blue",font=("arial",20)).grid(row=0, column=1)
    Label(att_l, text="Id",fg="blue",font=("arial",20)).grid(row=1, column=0)
    i=Entry(att_l,width=35, textvariable=StringVar())
    i.grid(row=1, column=1,columnspan=1)
    Label(att_l, text="hour",fg="blue",font=("arial",13)).grid(row=3, column=0)
    h=Entry(att_l,width=15, textvariable=StringVar())
    h.grid(row=3, column=1)
    Label(att_l, text="minute",fg="blue",font=("arial",13)).grid(row=4, column=0)
    m=Entry(att_l,width=15, textvariable=StringVar())
    m.grid(row=4, column=1)
    def l():
        d=str(datetime.now())
        lat_a=((((int(d[11:13])-9)*60)+int(d[14:16]))/60)
        mycoursor.execute(f"SELECT * FROM  attend where  code='{i.get()}' ")
        e=mycoursor.fetchone()
        mycoursor.execute(f"SELECT * FROM  attends where  year='{int(d[5:7])}' and mon='{int(d[0:4])}'and day='{int(d[8:10])}' ")
        e_2=mycoursor.fetchone()
        if m.get() =="" and h.get() =="" :
            if i.get() !="" :
                if e is None:e="crash";messagebox.showerror("error",f"ther isnot correct id")
                if  e[3]==i.get():
                    if e_2 is None:
                        dbs_2="INSERT into attends(id ,attend  ,late ,day,mon,year ) values(%s,%s,%s,%s,%s,%s)"
                        mycoursor.execute(dbs_2,(f"{i.get()}",f"{int(d[11:13])}",f"{lat_a}",f"{int(d[8:10])}",f"{int(d[5:7])}",f"{int(d[0:4])}"))
                        mydb.commit()
                        i.delete(0,END)
                        messagebox.showinfo("info",f"late is: :{lat_a}")
                    else:messagebox.showerror("error",f" it already login today");i.delete(0,END)
                else:messagebox.showerror("error",f"error in id ");i.delete(0,END)
            else:messagebox.showerror("error","error")
        else:
            lat_m=((((int(int(h.get()))-9)*60)+int(m.get()))/60)
            if i.get() !="" :
                if e is None:e="crash";messagebox.showerror("error",f"ther isnot correct id")
                if  e[3]==i.get():
                    if e_2 is None:
                        dbs_2="INSERT into attends(id ,attend  ,late ,day,mon,year ) values(%s,%s,%s,%s,%s,%s)"
                        mycoursor.execute(dbs_2,(f"{i.get()}",f"{int(d[11:13])}",f"{lat_m}",f"{int(d[8:10])}",f"{int(d[5:7])}",f"{int(d[0:4])}"))
                        mydb.commit()
                        i.delete(0,END)
                        messagebox.showinfo("info",f"late is: :{lat_m}")
                    else:messagebox.showerror("error",f" it already login today");i.delete(0,END)
                else:messagebox.showerror("error",f"error in id ");i.delete(0,END)
            else:messagebox.showerror("error","error")
    sinupButton = Button(att_l, text="log in",bg="blue",width=15,height=2,command=l).grid(row=5, column=1)  
def sin():
    att_s= Toplevel()
    att_s.geometry('370x200')  
    att_s.title('Attendance Form ')
    Label(att_s, text="Sin up",fg="blue",font=("arial",20)).grid(row=0, column=1)
    Label(att_s, text="Name",fg="blue",font=("arial",20)).grid(row=1, column=0)
    n=Entry(att_s,width=35, textvariable=StringVar())
    n.grid(row=1, column=1,columnspan=1)
    Label(att_s, text="Work hours",fg="blue",font=("arial",20)).grid(row=3, column=0)
    w=Entry(att_s,width=35, textvariable=StringVar())
    w.grid(row=3, column=1,columnspan=1)
    Label(att_s, text="title",fg="blue",font=("arial",20)).grid(row=4, column=0)
    t=Entry(att_s,width=35, textvariable=StringVar())
    t.grid(row=4, column=1,columnspan=1)
    def s():
        mycoursor.execute(f"SELECT * FROM  attend where  name='{n.get()}' ")
        e=mycoursor.fetchone()
        if n.get() !="" and w.get() !="" and t.get() !="":
            if e is None:e="crash"
            if  e[0]==n.get():messagebox.showerror("error",f"he alredy in data base")
            else:
                c_1=["A","b","c","D","F","G","h","I","J","K","L","M","N","O","P","Q","a","b","c","d","e","f","g","h","i","g","k"];ch=random2.choice(c_1)
                pn="0123456789";r=("".join((random.choice(pn) for i in range(4))))
                code=str(ch+str(r))
                dbs="INSERT into attend(name ,work_hours,title,code) values(%s,%s,%s,%s)"
                nt=int(w.get())
                mycoursor.execute(dbs,(f"{n.get()}",f"{nt}",f"{t.get()}",f"{code}"))
                # mycoursor.execute("INSERT into attends(id) values(%s)",(f"{code}"))
                mydb.commit()
                n.delete(0,END);w.delete(0,END);t.delete(0,END);
                messagebox.showinfo("info",f"id:{code}")
        else:messagebox.showerror("error","error")
        # if t.get() =="":
        #     print("null")
    sinupButton = Button(att_s, text="Sin Up",bg="blue",width=15,height=2,command=s).grid(row=5, column=1) 

def late():
    att_t= Toplevel()    
    att_t.geometry('370x200')  
    att_t.title('Attendance Form ')
    Label(att_t, text="Late of Attendance",fg="blue",font=("arial",20)).grid(row=0, column=1)
    Label(att_t, text="Late",fg="blue",font=("arial",20)).grid(row=0, column=2)
    Label(att_t, text="Id",fg="blue",font=("arial",20)).grid(row=1, column=0)
    id=Entry(att_t,width=35, textvariable=StringVar())
    id.grid(row=1, column=1,columnspan=1)
    Label(att_t, text="year",fg="blue",font=("arial",13)).grid(row=3, column=0)
    y=Entry(att_t,width=15, textvariable=StringVar())
    y.grid(row=3, column=1)
    Label(att_t, text="month",fg="blue",font=("arial",13)).grid(row=3, column=2)
    m=Entry(att_t,width=15, textvariable=StringVar())
    m.grid(row=3, column=3)
    Label(att_t, text="day",fg="blue",font=("arial",13)).grid(row=4, column=0)
    d=Entry(att_t,width=15, textvariable=StringVar())
    d.grid(row=4, column=1)
    def inf():
        mycoursor.execute(f"SELECT * FROM  attend where  code='{id.get()}' ")
        e=mycoursor.fetchone()
        if e is None:e="crash"
        if id.get() !="" and y.get() !=""  and m.get()!="" and d.get()!="":
            if  e[3]==id.get():
                mycoursor.execute(f"SELECT * FROM  attends where  id='{id.get()}' and year='{y.get()}' and mon='{m.get()}' and day='{d.get()}'")
                res=mycoursor.fetchall()
                late=0
                for z in res:
                    late+=(float(z[2]))
                mydb.commit()
                messagebox.showinfo("info",f"total late in {y.get()}-{m.get()}-{d.get()}: {late}")
                id.delete(0,END);y.delete(0,END);d.delete(0,END);m.delete(0,END);
            else:messagebox.showerror("error",f"the id is wrong and you must wright all feilds")
        elif id.get() !="" and y.get() !=""  and m.get()!="" and d.get()=="":
            if  e[3]==id.get():
                mycoursor.execute(f"SELECT * FROM  attends where  id='{id.get()}'and year='{y.get()}' and mon='{m.get()}' ")
                res=mycoursor.fetchall()
                late=0
                for z in res:
                    late+=(float(z[2]))
                mydb.commit()
                messagebox.showinfo("info",f"total late in {y.get()}-{m.get()}: {late}")
                id.delete(0,END);y.delete(0,END);d.delete(0,END);m.delete(0,END);
            else:messagebox.showerror("error",f"the id is wrong or you must wright year&month")
        elif id.get() !="" and y.get() !="" and m.get()=="" and m.get()=="":
            if  e[3]==id.get():
                mycoursor.execute(f"SELECT * FROM  attends where  id='{id.get()}' and year='{y.get()}'")
                res=mycoursor.fetchall()
                late=0
                for z in res:
                    late+=(float(z[2]))
                mydb.commit()
                messagebox.showinfo("info",f"total late in {y.get()}: {late}")
                id.delete(0,END);y.delete(0,END);d.delete(0,END);m.delete(0,END);
            else:messagebox.showerror("error",f"the id is wrong and you must wright year")

        else:messagebox.showerror("error","error")
        # if t.get() =="":
        #     print("null")
    sinupButton = Button(att_t, text="Check",bg="blue",width=15,height=2,command=inf).grid(row=5, column=1)
Label(att, text="Attendance",fg="blue",font=("arial",20)).grid(row=0, column=2)
loginButton = Button(att, text="sinup",bg="blue",width=15,height=2,command=sin).grid(row=4, column=1)  
sinupButton = Button(att, text="login",bg="blue",width=15,height=2,command=log).grid(row=4, column=2)  
sinupButton = Button(att, text="info",bg="blue",width=15,height=2,command=late).grid(row=4, column=3)  

mydb.commit()
att.mainloop()
print(mydb)
