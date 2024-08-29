from tkinter import *
# from PIL import *
from tkinter import messagebox
import sqlite3
# start
book=Tk()
book.title("book viwer")
photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
book.iconphoto(False, photo)
book.geometry("302x100")

def Data_base():
    global db
    global cr
    db=sqlite3.connect("book.db")
    cr=db.cursor()
    cr.execute("CREATE TABLE if not exists book(bookname text,writername text,noo3 text,tkim integer,pref text) ")
def cc():
    db.commit()
    db.close()

def done():
    if len(sec_e.get())>0:k=sec_e.get()
    else:k=click.get()
    Data_base()
    cr.execute(f"insert into book(bookname,writername,noo3,tkim,pref) values('{w_e2.get()}','{w_e.get()}','{k}' ,'{c.get()}','{pt}')")
    w_e.delete(0,END)
    w_e2.delete(0,END)
    sec_e.delete(0,END)
    cc()



def add():
    t=Toplevel()
    t.title("book viwer")
    photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
    t.iconphoto(False, photo)

    global w_e
    global w_e2
    global sec_e
    global click
    global c
    global pt
    pt="no pref"

    def pref():
        p=Toplevel()
        p.title("book viwer")
        photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
        p.iconphoto(False, photo)

        def s():
            global pt
            pt=T.get()
            T.delete(0,END)

        Label(p,text="write your pref ",fg="black",font=("arial",15)).grid(row=0,column=1,columnspan=2)
        # T = Text(p, height = 5, width = 52)
        T = Entry(p, width = 52)
        T.grid(row=2,column=1,pady=10,padx=10)
        b=Button(p,text="أتمام",width=20,command=s)
        Button(p,text="exit",width=20,command=p.destroy).grid(row=5,column=2,columnspan=2)
        b.grid(row=4,column=2,columnspan=2)
    ########
    a_l=Label(t,text="Add New Book",fg="black",font=("arial",15)).grid(row=0,column=1,columnspan=2)
    w_e=Entry(t,width=50)
    w_l=Label(t,text="اسم الكاتب: ",fg="black",font=("arial",10)).grid(row=4,column=0)
    w_e.grid(row=2,column=2,columnspan=2)
    # Label(t).grid(row=3,column=0)
    w_e2=Entry(t,width=50)
    w_l2=Label(t,text="اسم الكتاب: ",fg="black",font=("arial",10)).grid(row=2,column=0)
    w_e2.grid(row=4,column=2,columnspan=2)
    # Label(t).grid(row=5,column=0)
    cl=[
    "علمي",
    "تاريخي",
    "روايه تاريخيه",
    "روايه رعب",
    "روايه",
    "دين",
    "فلسفه"
    ]
    click=StringVar()
    click.set(":نوع الكتاب")
    drop=OptionMenu(t,click,*cl)
    drop.grid(row=6)
    sec_e=Entry(t,width=50)
    sec_e.grid(row=6,pady=10,column=2)

    tm=[
    1,
    2,
    3,
    4,
    5
    ]
    c=IntVar()
    c.set(":تقيم")
    drop=OptionMenu(t,c,*tm)
    drop.grid(row=7,column=1,columnspan=2)


    Button(t,text="كتابه اللخص",width=20,command=pref).grid(row=8 ,column=2)
    Button(t,text="أتمام",width=20,command=done).grid(row=9 ,column=2)



def search():
    t=Toplevel()
    t.title("book viwer")
    photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
    t.iconphoto(False, photo)
    global w
    global w_2
    global sec
    global cl


    Label(t,text="search about Book",fg="black",font=("arial",15)).grid(row=0,column=1,columnspan=2)
    w=Entry(t,width=50)
    Label(t,text="اسم الكاتب: ",fg="black",font=("arial",10)).grid(row=2,column=0)
    w.grid(row=2,column=2,columnspan=2)
    # Label(t).grid(row=3,column=0)
    w_2=Entry(t,width=50)
    Label(t,text="اسم الكتاب: ",fg="black",font=("arial",10)).grid(row=4,column=0)
    w_2.grid(row=4,column=2,columnspan=2)


    def su():
        global pr
        Data_base()
        cr.execute(f"select * from book where bookname ='{w_2.get()}' and  writername ='{w.get()}' ")
        t=cr.fetchall()
        if t!=None:
            for i in t:
                pr=i[4]
                Label(book,text=f"اسم الكتاب:{i[0]}\n اسم الكاتب:{i[1]}\n النوع:{i[2]}\n التقيم:{i[3]}",font=("arial",12)).grid(row=4,column=2,columnspan=2)
                Button(book,text="قرائه اللخص",width=20,command=red).grid(row=5 ,column=2)
        cc()


    def red():
        r=Toplevel()
        r.title("book viwer")
        photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
        r.iconphoto(False, photo)
        Label(r,text="Red the pref ",fg="black",font=("arial",15)).pack()
        T = Label(r,text=f"{pr}").pack()
        Button(r,text="أتمام",width=20,command=r.destroy).pack()

    Button(t,text="أتمام",width=20,command=su).grid(row=7 ,column=2)

m_l=Label(book,text="bookviwer",fg="black",font=("arial",20)).grid(row=0,column=2,columnspan=2)
f_b=Button(book,text="سجل",bg="blue",width=20,command=add).grid(row=3 ,column=2)
s_b=Button(book,text="بحث",bg="blue",width=20,command=search).grid(row=3 ,column=3)

book.mainloop()