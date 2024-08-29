from tkinter import*
cal=Tk()
cal.title("calculator")

# start code
# input
e=Entry(cal,width=40,borderwidth=3)
e.grid(row=0,column=0,columnspan=3,pady=10,padx=10)

# fun
def btn_click(number):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(number))

def btn_Clear():
    e.delete(0,END)

def btn_add():
    f_n=e.get()
    global nr
    global math
    math="add"
    nr=int(f_n)
    e.delete(0,END)

def btn_min():
    f_n=e.get()
    global nr
    global math
    math="min"
    nr=int(f_n)
    e.delete(0,END)

def btn_div():
    f_n=e.get()
    global nr
    global math
    math="div"
    nr=int(f_n)
    e.delete(0,END)

def btnx():
    f_n=e.get()
    global nr
    global math
    math="x"
    nr=int(f_n)
    e.delete(0,END)
def btn_p():
    f_n=e.get()
    global nr
    global math
    math="p"
    nr=int(f_n)
    e.delete(0,END)

def btn_equ():
    s_n=e.get()
    e.delete(0,END)
    if   math =="add":e.insert(0,nr+int(s_n))
    elif math =="min":e.insert(0,nr-int(s_n))
    elif math =="div":e.insert(0,nr/int(s_n))
    elif math =="x":e.insert(0,nr*int(s_n))
    elif math =="p":e.insert(0,nr**int(s_n))
    else :e.delete(0,END)

#btn 
btn_1=Button(cal,text="1",padx=35,pady=15,command=lambda: btn_click(1))
btn_2=Button(cal,text="2",padx=35,pady=15,command=lambda: btn_click(2))
btn_3=Button(cal,text="3",padx=35,pady=15,command=lambda: btn_click(3))
btn_4=Button(cal,text="4",padx=35,pady=15,command=lambda: btn_click(4))
btn_5=Button(cal,text="5",padx=35,pady=15,command=lambda: btn_click(5))
btn_6=Button(cal,text="6",padx=35,pady=15,command=lambda: btn_click(6))
btn_7=Button(cal,text="7",padx=35,pady=15,command=lambda: btn_click(7))
btn_8=Button(cal,text="8",padx=35,pady=15,command=lambda: btn_click(8))
btn_9=Button(cal,text="9",padx=35,pady=15,command=lambda: btn_click(9))
btn_0=Button(cal,text="0",padx=35,pady=15,command=lambda: btn_click(0))
btn_pls=Button(cal,text="+",padx=35,pady=15,command= btn_add)
btn_mi=Button(cal,text="-",padx=35,pady=15,command=btn_min)
btn_di=Button(cal,text="/",padx=35,pady=15,command=btn_div)
btn_x=Button(cal,text="x",padx=35,pady=15,command=btnx)
btn_eq=Button(cal,text="=",padx=80,pady=15 ,command= btn_equ)
btn_clear=Button(cal,text="c",padx=80,pady=15 ,command=btn_Clear)
btn_p=Button(cal,text="**",padx=120,pady=15 ,command=btn_p)

# btn place
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)

btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_0.grid(row=4 , column=0)
btn_eq.grid(row=4,column=1,columnspan=2)

btn_pls.grid(row=5,column=0)
btn_clear.grid(row=5,column=1,columnspan=2)

btn_mi.grid(row=6,column=0)
btn_x.grid(row=6,column=1)
btn_di.grid(row=6,column=2)

btn_p.grid(row=7,column=0,columnspan=3)

cal.mainloop()