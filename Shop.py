# imports
from tkinter import *
# from PIL import *
from tkinter import messagebox
import sqlite3
# start
shop=Tk()
shop.title("shop program")
photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
shop.iconphoto(False, photo)
# shop.geometry("500x500")
# Data base
def Data_base():
    global db
    global cr
    db=sqlite3.connect("shop.db")
    cr=db.cursor()
    cr.execute("CREATE TABLE if not exists shop(name text,id integer,counts integer,price integer ) ")
def cc():
    db.commit()
    db.close()

def s():
    Data_base()
    cr.execute(f"insert into shop values('{name.get()}','{ids.get()}','{count.get()}','{price.get()}')")
    name.delete(0,END)
    ids.delete(0,END)
    count.delete(0,END)
    price.delete(0,END)
    cc()

def v():
    Data_base()
    cr.execute(f"select * from shop where name='{name1.get()}'")
    t=cr.fetchall()
    if t!=None:
        cr.execute(f"delete from shop where name='{name1.get()}'")
        Label(r,text=f"broduct who had name:'{name1.get()}' was removed ").grid(row=5,column=1)
        name1.delete(0,END)
    else:messagebox.showerror("error","it not exist")
    cc()

def show():
    Data_base()
    cr.execute(f"select * from shop where name='{e.get()}'")
    t=cr.fetchall()
    if t!=None:
        for i in t:
            Label(shop,text=f"name:{i[0]}\n id:{i[1]}\n count:{i[2]}\n price:{i[3]}").grid(row=5,column=0,columnspan=2)
            sell=Button(shop,bg="blue",text="Sell",command=sl).grid(row=6,column=1)
    else:messagebox.showerror("error","it not exist")
    cc()

def sl():
    Data_base()
    cr.execute(f"select * from shop where name='{e.get()}'")
    t=cr.fetchall()
    if t!=None:
        for i in t:
            c=i[2]
            cr.execute(f"update shop set counts='{c-1}' where name='{e.get()}'")
    else:messagebox.showerror("error","it not exist")
    cc()

def up():
    Data_base()
    cr.execute(f"select * from shop where name='{pc1.get()}'")
    t=cr.fetchall()
    global p1
    global c1
    if t!=None:
        Label(ut,text="New price of broduct:").grid(row=4,column=1)
        p1=Entry(ut,width=30)
        p1.grid(row=5,column=1)
        Button(ut,text="submit",bg="blue",width=20,pady=6,command=p).grid(row=6,column=1)
        Label(ut,text="New count of broduct:").grid(row=7,column=1)
        c1=Entry(ut,width=30)
        c1.grid(row=8,column=1)
        Button(ut,text="submit",bg="blue",width=20,pady=6,command=ct).grid(row=9,column=1)
    else:messagebox.showerror("error","it not exist")
    cc()

def p():
    Data_base()
    cr.execute(f"select * from shop where name='{pc1.get()}'")
    t=cr.fetchall()
    if t!=None:
        cr.execute(f"update shop set price='{p1.get()}' where name='{pc1.get()}'")
        p1.delete(0,END)
    else:messagebox.showerror("error","it not exist")

    cc()

def ct():
    Data_base()
    cr.execute(f"select * from shop where name='{pc1.get()}'")
    t=cr.fetchall()
    if t!=None:
        cr.execute(f"update shop set counts='{c1.get()}' where name='{pc1.get()}'")
        c1.delete(0,END)
    else:messagebox.showerror("error","it not exist")
    cc()

def c():
    t=Toplevel()
    t.title("shop program")
    photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
    t.iconphoto(False, photo)
    def add():
        Data_base()
        a=Toplevel()
        a.title("shop program add")
        photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
        a.iconphoto(False, photo)
        Label(a,text="add").grid(row=0,column=1)
        global name
        global ids
        global count
        global price
        nl=Label(a,text="Name").grid(row=1,column=1)
        name=Entry(a,width=30)
        name.grid(row=1,column=1)
        i=Label(a,text="id").grid(row=2,column=1)
        ids=Entry(a,width=30)
        ids.grid(row=3,column=1)
        ct=Label(a,text="count").grid(row=4,column=1)
        count=Entry(a,width=30)
        count.grid(row=5,column=1)
        pc=Label(a,text="price").grid(row=6,column=1)
        price=Entry(a,width=30)
        price.grid(row=7,column=1)
        Button(a,text="submit",bg="blue",width=20,pady=6,command=s).grid(row=8,column=1)
        Button(a,bg="blue",command=a.destroy,text="quit").grid(row=9,column=1)
        cc()
    def remove():
        Data_base()
        global r
        r=Toplevel()
        r.title("shop program remove")
        photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
        r.iconphoto(False, photo)
        global name1
        Label(r,text="remove").grid(row=0,column=1)
        Label(r,text="Name of broduct").grid(row=1,column=1)
        name1=Entry(r,width=30)
        name1.grid(row=2,column=1)
        Button(r,text="submit",bg="blue",width=20,pady=6,command=v).grid(row=3,column=1)
        Button(r,bg="blue",command=r.destroy,text="quit").grid(row=4,column=1)
        cc()
    def update():
        Data_base()
        global ut
        ut=Toplevel()
        ut.title("shop program update")
        photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
        ut.iconphoto(False, photo)
        global pc1
        Label(ut,text="update").grid(row=0,column=1)
        Label(ut,text="Name of broduct:").grid(row=1,column=1)
        pc1=Entry(ut,width=30)
        pc1.grid(row=2,column=1)
        Button(ut,bg="blue",command=up,text="submit").grid(row=3,column=1)
        Button(ut,bg="blue",command=ut.destroy,text="quit").grid(row=10,column=1)
        cc()

    Label(t,text="choose").grid(row=0,column=1,columnspan=2)
    Button(t,text="Add",bg="blue",width=20,pady=6,command=add).grid(row=1,column=1,columnspan=2)
    Button(t,text="update",bg="blue",width=20,pady=6,command=update).grid(row=2,column=1,columnspan=2)
    Button(t,text="Remove",bg="blue",width=20,pady=6,command=remove).grid(row=3,column=1,columnspan=2)
    Button(t,bg="blue",command=t.destroy,text="quit").grid(row=4,column=1,columnspan=2)

m_l=Label(shop,text="mt²",fg="black",font=("arial",25)).grid(row=0,column=0,columnspan=2)
s_l=Label(shop,text="write name of broudct:").grid(row=1,column=0)
e=Entry(shop,width=50)
e.grid(row=1,column=1)
m_b=Button(shop,text="click!",bg="blue",width=20,pady=6,command=show).grid(row=3,column=0,columnspan=2)
s_b=Button(shop,bg="blue",command=c).grid(row=2)
Button(shop,bg="blue",text="quit",command=quit).grid(row=4,column=0,columnspan=2)

shop.mainloop()

