from util.generic import leer_imagen
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("1355x580")
window.config(bg="white")
window.resizable(False,False)

selimage = leer_imagen("recursos_img/menu_sele1.png",(456,50))
selimage2 = leer_imagen("recursos_img/menu_sele2.png",(456,50))

frame_cen = Frame(window, height= 540, width=1355, bg="#fff")
frame_cen.place(x=0,y=20)
#---------botones--------
def enter(e):
    selabel_btn1["image"] =selimage2
    selabel_btn1.image=selimage2
def leave(e):
    selabel_btn1["image"] =selimage
    selabel_btn1.image=selimage
selabel1 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn1 = Button(selabel1,image=selimage,bd=0,bg="#fff")
tex1 = Label(selabel1, text="Test 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex1.place(x=25,y=3)
selabel_btn1.pack()
selabel_btn1.bind("<Enter>",enter)
selabel_btn1.bind("<Leave>",leave)
selabel1.place(x=180,y=170)


def enter(e):
    selabel_btn2["image"] =selimage2
    selabel_btn2.image=selimage2
def leave(e):
    selabel_btn2["image"] =selimage
    selabel_btn2.image=selimage
selabel2 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn2 = Button(selabel2,image=selimage,bd=0,bg="#fff")
tex2 = Label(selabel2, text="Test 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex2.place(x=25,y=3)
selabel_btn2.pack()
selabel_btn2.bind("<Enter>",enter)
selabel_btn2.bind("<Leave>",leave)
selabel2.place(x=180,y=250)

def enter(e):
    selabel_btn3["image"] =selimage2
    selabel_btn3.image=selimage2
def leave(e):
    selabel_btn3["image"] =selimage
    selabel_btn3.image=selimage
selabel3 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn3 = Button(selabel3,image=selimage,bd=0,bg="#fff")
tex3 = Label(selabel3, text="Test 3", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex3.place(x=25,y=3)
selabel_btn3.pack()
selabel_btn3.bind("<Enter>",enter)
selabel_btn3.bind("<Leave>",leave)
selabel3.place(x=180,y=330)

def enter(e):
    selabel_btn4["image"] =selimage2
    selabel_btn4.image=selimage2
def leave(e):
    selabel_btn4["image"] =selimage
    selabel_btn4.image=selimage
selabel4 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn4 = Button(selabel4,image=selimage,bd=0,bg="#fff")
tex4 = Label(selabel4, text="Test 4", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex4.place(x=25,y=3)
selabel_btn4.pack()
selabel_btn4.bind("<Enter>",enter)
selabel_btn4.bind("<Leave>",leave)
selabel4.place(x=716,y=170)

def enter(e):
    selabel_btn5["image"] =selimage2
    selabel_btn5.image=selimage2
def leave(e):
    selabel_btn5["image"] =selimage
    selabel_btn5.image=selimage
selabel5 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn5 = Button(selabel5,image=selimage,bd=0,bg="#fff")
tex5 = Label(selabel5, text="Test 5", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex5.place(x=25,y=3)
selabel_btn5.pack()
selabel_btn5.bind("<Enter>",enter)
selabel_btn5.bind("<Leave>",leave)
selabel5.place(x=716,y=250)

def enter(e):
    selabel_btn6["image"] =selimage2
    selabel_btn6.image=selimage2
def leave(e):
    selabel_btn6["image"] =selimage
    selabel_btn6.image=selimage
selabel6 = Frame(frame_cen, height=50, width=456,bg= "#fff")
selabel_btn6 = Button(selabel6,image=selimage,bd=0,bg="#fff")
tex6 = Label(selabel6, text="Test 6", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
tex6.place(x=25,y=3)
selabel_btn6.pack()
selabel_btn6.bind("<Enter>",enter)
selabel_btn6.bind("<Leave>",leave)
selabel6.place(x=716,y=330)










window.mainloop()