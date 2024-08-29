from tkinter import *
from functools import partial
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

tkWindow = Tk()  
tkWindow.geometry('370x125')  
tkWindow.title(' Login Form ')
Label(tkWindow, text="Login&SinUp",fg="blue",font=("arial",20)).grid(row=0, column=2)

def data():
    global con
    global cr
    con=sqlite3.connect("logsin.db")
    cr=con.cursor()
    cr.execute("CREATE TABLE if not exists Datas(User_name text ,Email text,password_key text)")
# create defs




def sinup():
    Windowtk = Toplevel()  
    Windowtk.geometry('370x135')  
    Windowtk.title(' Login SinUp ')
    photo = PhotoImage(file ="C:/Users/ptof/Desktop/html/xd/icon/home.png")
    Windowtk.iconphoto(False, photo)
    Label(Windowtk,font=("arial",20),fg="blue", text="SinUp").grid(row=0, column=1)
    usernameLabel = Label(Windowtk, text="User Name").grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(Windowtk, textvariable=username,width=35)
    usernameEntry.grid(row=1, column=1)  
    EmailLabel = Label(Windowtk, text="Email").grid(row=2, column=0)
    username = StringVar()
    EmailEntry = Entry(Windowtk, textvariable=username,width=35)
    EmailEntry.grid(row=2, column=1)  
    passwordLabel = Label(Windowtk,text="Password").grid(row=3, column=0)  
    password = StringVar()
    passwordEntry = Entry(Windowtk, textvariable=password,width=35 ,show='*')
    passwordEntry.grid(row=3, column=1)  
    def sin():
        data()
        pg=passwordEntry.get()
        cr.execute(f"select *from Datas where  password_key='{pg}' ")
        rs=cr.fetchall()
        match rs:
            case None:messagebox.askyesnocancel(" its aready  exist")
            case i:
                cr.execute(f"insert into Datas values('{usernameEntry.get()}','{EmailEntry.get()}','{passwordEntry.get()}')")
                con.commit()
                con.close()
                passwordEntry.delete(0,END)
                EmailEntry.delete(0,END)
                usernameEntry.delete(0,END)
                print("sucssful sin up")
                quit()
    Buton= Button(Windowtk, text="submit", command=sin,bg="blue",width=25,height=2).grid(row=4, column=1)  


def Login():
    Window = Toplevel()  
    Window.geometry('370x135')  
    Window.title(' Login Form ')
    Label(Window, text="Login",font=("arial",20),fg="blue").grid(row=0, column=1)
    EmailLabel = Label(Window, text="Email").grid(row=2, column=0)
    username = StringVar()
    EmailEntry = Entry(Window,width=35, textvariable=username)
    EmailEntry.grid(row=2, column=1)  
    passwordLabel = Label(Window,text="Password").grid(row=3, column=0)  
    password = StringVar()
    passwordEntry = Entry(Window, textvariable=password, show='*',width=35)
    passwordEntry .grid(row=3, column=1) 
    def log():
        data()
        pg=passwordEntry.get()
        cr.execute(f"select * from Datas where  password_key='{pg}' ")
        rs=cr.fetchall()
        match rs:
            case None:
                messagebox.askyesnocancel(" itsnot exist")
            case defu:
                con.commit()
                con.close()
                passwordEntry.delete(0,END)
                EmailEntry.delete(0,END)
                print("sucssful login")
                for i in rs :
                    print(f"yous user name: {i[0]}")
                quit()
    Buttons= Button(Window, text="submit", command=log,bg="blue",width=25,height=2).grid(row=4, column=1)  
# validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login", command=Login,bg="blue",width=25,height=2).grid(row=4, column=2)  
sinupButton = Button(tkWindow, text="sinup", command=sinup,bg="blue",width=25,height=2).grid(row=4, column=1)  

tkWindow.mainloop()