try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from doctest import master
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.font as font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from setuptools import Command
from util.generic import leer_imagen
import random

logic_score = 0
pseint_score = 0
math_score= 0
coding_score = 0
class Fullscreen_Example(tk.Tk):
    def __init__(self,*args,**kwargs):
        #super().__init__(*args,**kwargs)
        self.window = tk.Tk()
        self.window.title("PLM+")
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" % (self.w, self.h))
        self.window.config(bg='white')
        self.window.iconbitmap("images/iconi.ico")
        
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        self.frame_principal = Frame(self.window, bg='white')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.frame_principal.columnconfigure(1,weight=1)
        self.frame_principal.rowconfigure(1,weight=1)
        self.frame_principal.place(x=1, y=105)
        self.widgets()

    
    def menu1(self):
        self.notebook.select([self.page5])
        self.page5.columnconfigure(0, weight=1)
    def menu2(self):
        self.notebook.select([self.page6])
        self.page6.columnconfigure(0, weight=1)
    def menu3(self):
        self.notebook.select([self.page7])
        self.page7.columnconfigure(0, weight=1)
    def menu4(self):
        self.notebook.select([self.page8])
        self.page8.columnconfigure(0, weight=1)
    def home(self):
        self.notebook.select([self.page1])
        self.page1.columnconfigure(0, weight=1)
    def stadistics(self):
        self.canvas.draw()
        self.notebook.select([self.page3])
        self.page3.columnconfigure(0, weight=1)
        #self.page3.place(x=0,y=200)
    def info_f(self):
        self.notebook.select([self.page4])
        self.page4.columnconfigure(0, weight=1)
    def test1(self):
        self.notebook.select([self.page2])
        self.page2.columnconfigure(0, weight=1)
    def test2(self):
        self.notebook.select([self.page9])
        self.page9.columnconfigure(0, weight=1)
    def test3(self):
        self.notebook.select([self.page10])
        self.page10.columnconfigure(0, weight=1)
    
    ''' def comprob(self):
        global score
        #self.listeichon.insert(0,self.score)
        self.listeichon[0]=score
        self.listeichon = self.listeichon
        print(self.listeichon)
        self.progress_in['value']+=20
        self.frame_text.destroy()
        self.frame_text1.place(x=200,y=295)'''

    def widgets(self):

        self.selimage = leer_imagen("recursos_img/menu_sele1.png",(456,50))
        self.selimage2 = leer_imagen("recursos_img/menu_sele2.png",(456,50))
        self.submit1 = leer_imagen("recursos_img/submit1.png",(105,80))
        self.submit2 = leer_imagen("recursos_img/submit2.png",(105,80))
        self.frame_en = leer_imagen("recursos_img/frame_entry.png",(900,80))
        self.frame_en2 = leer_imagen("recursos_img/frame_entry2.png",(900,400))
        self.plant_info = leer_imagen("recursos_img/info_back.png",(972,454))
        self.barra_info = leer_imagen("recursos_img/barra_info.png",(582,45))
        self.next1 = leer_imagen("recursos_img/next.png",(60,60))
        self.privius = leer_imagen("recursos_img/previous.png",(60,60))
        self.foquito= leer_imagen("recursos_img/foquito.png",(83,110))
        self.foto_grup1 = leer_imagen("images/timeline1.png",(775,400))
        self.foto_grup2 = leer_imagen("images/timeline2.png",(775,400))
        self.foto_grup3 = leer_imagen("images/timeline3.png",(775,400))
        self.op_frame1 = leer_imagen("recursos_img/op_frame1.png",(160,120))
        self.op_frame2 = leer_imagen("recursos_img/op_frame2.png",(160,120))
        self.reload = leer_imagen("recursos_img/reload.png",(60,60))
        self.imagen_figuras = leer_imagen("images/imagen_figuras.png",(400,200))
        self.imagen_del_auto = leer_imagen("images/imagen_del_auto.png",(400,200))


        estilo_paginas = ttk.Style()
        estilo_paginas.configure("TNotebook",background ='white',foreground='white',padding=0,borderwidth=0)
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook",background='white',borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab",background='white',borderwidth=0)
        estilo_paginas.map("TNotebook", background=[("selected",'white')])
        estilo_paginas.map("TNotebook.Tab",background=[("selected",'white')],foreground=[("selected",'white')]);
        
        self.notebook = ttk.Notebook(self.frame_principal,style='TNotebook')
        self.notebook.grid(column=0,row=0,sticky='nsew')
        self.page1= Frame(self.window,width=1355,height=580,bg="white")
        self.page2= Frame(self.window,width=1355,height=580,bg="white")
        self.page3= Frame(self.window,width=1355,height=500,bg="white")
        self.page4= Frame(self.window,width=1355,height=580,bg="white")
        self.page5= Frame(self.window,width=1355,height=580,bg="white")
        self.page6= Frame(self.window,width=1355,height=580,bg="white")
        self.page7= Frame(self.window,width=1355,height=580,bg="white")
        self.page8= Frame(self.window,width=1355,height=580,bg="white")
        self.page9= Frame(self.window,width=1355,height=580,bg="white")
        self.page10= Frame(self.window,width=1355,height=580,bg="white")
        self.notebook.add(self.page1)
        self.notebook.add(self.page2)
        self.notebook.add(self.page3)
        self.notebook.add(self.page4)
        self.notebook.add(self.page5)
        self.notebook.add(self.page6)
        self.notebook.add(self.page7)
        self.notebook.add(self.page8)
        self.notebook.add(self.page9)
        self.notebook.add(self.page10)

####################################################PAGE ONE#################################################################################################
        def random1():
            num = random.randint(1,3)
            if num==1:
                self.test1()
            elif num == 2:
                self.test2()
            else:
                self.test3()
        self.navbar = leer_imagen("recursos_img/barranv.png",(1260,100))
        self.info = leer_imagen("recursos_img/info_con.png",(80,80))
        self.stadistic = leer_imagen("recursos_img/stadistic_con.png",(80,80))
        frame_opbar=Frame(self.page1, width=1325, height=200, bg="white").place(x=20, y=10)
        label = Label(frame_opbar, image=self.navbar, bg='white').place(x=50, y=20)
        info = Button(frame_opbar, image=self.info, bg = "#FCBA40",bd=0, activebackground="#FCBA40",command=self.info_f).place(x=340,y= 30)
        stadistic = Button(frame_opbar, image=self.stadistic, bg="#FCBA40",bd=0,activebackground="#FCBA40",command=self.stadistics).place(x=970,y=30)
        foco = Button(frame_opbar, image=self.foquito, bg="#fff", bd=0, activebackground="#fff",command=random1).place(x=640, y=70)
#--------------------botones------------------------------------------------------------------------
        imagen1 = leer_imagen("recursos_img/pg1.png",(200,200))
        imagen2 = leer_imagen("recursos_img/pg2.png",(200,200))
        def enter(e):
            bt_op1["image"] =imagen2
            bt_op1.image=imagen2
        def leave(e):
            bt_op1["image"] =imagen1
            bt_op1.image=imagen1
        frame_seg1=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg1.place(x=95,y=135)
        bt_op1=Button(frame_seg1,image=imagen1,bg="white",bd=0, command=self.menu1)
        bt_op1.bind("<Enter>",enter)
        bt_op1.bind("<Leave>",leave)
        bt_op1.place(x=20,y=20)
#------boton 2------
        imagen3 = leer_imagen("recursos_img/lo1.png",(200,200))
        imagen4 = leer_imagen("recursos_img/lo2.png",(200,200))
        def enter1(e):
            bt_op2["image"] =imagen4
            bt_op2.image=imagen4
        def leave1(e):
            bt_op2["image"] =imagen3
            bt_op2.image=imagen3
        frame_seg2=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg2.place(x=395,y=135)
        bt_op2=Button(frame_seg2,image=imagen3,bg="white",bd=0,command=self.menu2)
        bt_op2.bind("<Enter>",enter1)
        bt_op2.bind("<Leave>",leave1)
        bt_op2.place(x=20,y=20)
#-------boton 3-------
        imagen5 = leer_imagen("recursos_img/ps1.png",(200,200))
        imagen6 = leer_imagen("recursos_img/ps2.png",(200,200))
        def enter2(e):
            bt_op3["image"] =imagen6
            bt_op3.image=imagen6
        def leave2(e):
            bt_op3["image"] =imagen5
            bt_op3.image=imagen5
        frame_seg3=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg3.place(x=695,y=135)
        bt_op3=Button(frame_seg3,image=imagen5,bg="white",bd=0,command=self.menu3)
        bt_op3.bind("<Enter>",enter2)
        bt_op3.bind("<Leave>",leave2)
        bt_op3.place(x=20,y=20)
#--------boton 4--------
        imagen7 = leer_imagen("recursos_img/lm1.png",(200,200))
        imagen8 = leer_imagen("recursos_img/lm2.png",(200,200))
        def enter3(e):
            bt_op4["image"] =imagen8
            bt_op4.image=imagen8
        def leave3(e):
            bt_op4["image"] =imagen7
            bt_op4.image=imagen7
        frame_seg4=Frame(self.page1,width=250,height=250,bg="white")
        frame_seg4.place(x=995,y=135)
        bt_op4=Button(frame_seg4,image=imagen7,bg="white",bd=0,command=self.menu4)
        bt_op4.bind("<Enter>",enter3)
        bt_op4.bind("<Leave>",leave3)
        bt_op4.place(x=20,y=20)
#-----------------burger menu----------
        sidebar=leer_imagen("recursos_img/sidebar.png",(190,700))
        menuburger=leer_imagen("recursos_img/burgermenu.png",(40,40))
        menuburger2=leer_imagen("recursos_img/burgermenu2.png",(40,40))
        userico=leer_imagen("recursos_img/useric.png",(35,35))
        exitbt = leer_imagen("recursos_img/exitbt.png",(28,28))

        def toggle_win():
            f1=Frame(self.window,width=190,height=760,bg="white")
            f1.place(x=1170,y=13)
            Label(f1, image=sidebar,bg="white").place(x=0,y=0)

            def dele():
                f1.destroy()


            Button(f1,image=menuburger2,command=dele,border=0,activebackground='#035596',bg='#035596').place(x=35,y=34)
            Button(f1,image=userico,bg="#035596",bd=0,activebackground="#035596",command=self.home).place(x=35,y=90)
            Button(f1,image=exitbt,bg="#035596",bd=0,activebackground="#035596",command=self.window.destroy).place(x=130,y=640)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=198)
            pg_bt = Button(f1,text="Coding",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue",command=self.menu1)
            pg_bt.config(font =("Helvetica",14))
            pg_bt.place(x=5,y=200)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=234)
            pg_bt1 = Button(f1,text="Logic",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue",command=self.menu2)
            pg_bt1.config(font =("Helvetica",14))
            pg_bt1.place(x=5,y=236)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=270)
            pg_bt2 = Button(f1,text="PsInt",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue",command=self.menu3)
            pg_bt2.config(font =("Helvetica",14))
            pg_bt2.place(x=5,y=272)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=306)
            pg_bt2 = Button(f1,text="Math logic",width=17,height=1,bg="#035596",fg='white',bd=0,activebackground="#035596",activeforeground="light blue",command=self.menu4)
            pg_bt2.config(font =("Helvetica",14))
            pg_bt2.place(x=5,y=308)
            Frame(f1, width=178, height=2, bg='white').place(x=7, y=342)
            
        burgerbtn =Button(frame_opbar,image=menuburger,bg="#FCBA40",bd=0,activebackground="#FCBA40",command=toggle_win)
        burgerbtn.place(x=1200,y=52)

###############################################################PAGE TWO################################################################################################################
        #Label(self.page2,text="Hola mundo").place(x=1,y=1)
        progress_frame1 = Frame(self.page2, width=1325, height=70,bg ="white")
        progress_frame1.place(x=10,y=20)
#test - 1...............................................................................................................................
        #ans_entry = Frame(self.page2, height=80,width=900,bg="white").place(x=250,y=450)
        self.frame_text= Frame(self.page2,bd=0,width=990,height=100,padx=0,bg="white")
        self.frame_text.place(x=200,y=205)
        Label(self.frame_text,text="What kind of variable It is one that you can use to storage just text format?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        
        self.frame_text1= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text1,text="It is a programming language that actually works to the building of AI´s, Which is it?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text2= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text2,text="What word describes the set of instructions that computers need to work?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text3= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text3,text="How many types of windows does Python use?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text4= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text4,text="What are people who write computer code called?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text5= Frame(self.page2,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text5,text="Is it HTML a programming language?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
#test - 2...............................................................................................................................
        self.frame_text6= Frame(self.page9,bd=0,width=990,height=100,padx=0,bg="white")
        self.frame_text6.place(x=195,y=205)
        Label(self.frame_text6,text="How many trees are in a triangular field where there is a tree in each vertex and five in \neach side?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        
        self.frame_text7= Frame(self.page9,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text7,text="If a pineapple costs $3, How much I have to expend in a dozen and a half?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text8= Frame(self.page9,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text8,text="If each month has four weeks, How many weeks are in a year?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text9= Frame(self.page9,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text9,text="If I have 16 quartes, How much do I have in dollars?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text10= Frame(self.page9,bd=0,width=1020,height=200,padx=0,bg="white")      
        Label(self.frame_text10,image=self.imagen_figuras,
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=270,y=0)

        self.frame_text11= Frame(self.page9,bd=0,width=1020,height=200,padx=0,bg="white")
        Label(self.frame_text11,image=self.imagen_del_auto,
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=270,y=0)
#test - 3...............................................................................................................................
        self.frame_text12= Frame(self.page10,bd=0,width=990,height=100,padx=0,bg="white")
        self.frame_text12.place(x=200,y=205)
        Label(self.frame_text12,text="If I am in a marathon and in the middle of the race I overtake the second runner, in what\n position do I arrive?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)
        
        self.frame_text13= Frame(self.page10,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text13,text="How many times faster is the minute hand than the hour hand on a clock?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text14= Frame(self.page10,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text14,text="You get up at 9 to go to work and you go to sleep at 8, how many hours do you sleep?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text15= Frame(self.page10,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text15,text="A farmer has 17 cows, all but nine die, how many does he have left?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text16= Frame(self.page10,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text16,text="A night guard dies during the day, is he entitled to receive a pension?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)

        self.frame_text17= Frame(self.page10,bd=0,width=1020,height=100,padx=0,bg="white")
        Label(self.frame_text17,text="Each of three brothers has a sister, how many do they all add up to?",
        bg="white",fg="#035596",font=('Microsoft YaHei UI Light', 16,'bold')).place(x=5,y=5)


        t = ttk.Style()
        t.theme_use('default')
        t.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='white',
            background='#FCBA40',
            darkcolor="light blue",
            bordercolor="#FCBA40"
        )
        self.progress_in = ttk.Progressbar(progress_frame1,style="custom.Horizontal.TProgressbar",orient="horizontal",length=1260,mode='determinate')
        self.progress_in.place(x=45,y=40)

        
        def var_avan1():
            self.frame_text.destroy()
            self.frame_text1.place(x=200,y=205)
            
            lab5.place(x=55,y=50)
            op_frame4.place(x=0,y=0)
            frame_op5.place(x=170,y=350)
            lab6.place(x=50,y=45)
            op_frame5.place(x=0,y=0)
            frame_op6.place(x=470,y=350)
            lab7.place(x=50,y=45)
            op_frame6.place(x=0,y=0)
            frame_op7.place(x=770,y=350)
            lab8.place(x=50,y=45)
            op_frame7.place(x=0,y=0)
            frame_op8.place(x=1070,y=350)

            frame_op1.destroy()
            op_frame.destroy()
            lab1.destroy()
            frame_op2.destroy()
            op_frame1.destroy()
            lab2.destroy()
            frame_op3.destroy()
            op_frame2.destroy()
            lab3.destroy()
            frame_op4.destroy()
            op_frame3.destroy()
            lab4.destroy()

            aumento()
        def var_avan1_fak():
            self.progress_in['value']+=20
            self.frame_text.destroy()
            self.frame_text1.place(x=200,y=205)
            
            lab5.place(x=55,y=50)
            op_frame4.place(x=0,y=0)
            frame_op5.place(x=170,y=350)
            lab6.place(x=50,y=45)
            op_frame5.place(x=0,y=0)
            frame_op6.place(x=470,y=350)
            lab7.place(x=50,y=45)
            op_frame6.place(x=0,y=0)
            frame_op7.place(x=770,y=350)
            lab8.place(x=50,y=45)
            op_frame7.place(x=0,y=0)
            frame_op8.place(x=1070,y=350)

            frame_op1.destroy()
            op_frame.destroy()
            lab1.destroy()
            frame_op2.destroy()
            op_frame1.destroy()
            lab2.destroy()
            frame_op3.destroy()
            op_frame2.destroy()
            lab3.destroy()
            frame_op4.destroy()
            op_frame3.destroy()
            lab4.destroy()

        def var_avan2():
            self.frame_text1.destroy()
            self.frame_text2.place(x=200,y=205)

            lab9.place(x=55,y=50)
            op_frame8.place(x=0,y=0)
            frame_op9.place(x=170,y=350)
            lab10.place(x=50,y=45)
            op_frame9.place(x=0,y=0)
            frame_op10.place(x=470,y=350)
            lab11.place(x=50,y=45)
            op_frame10.place(x=0,y=0)
            frame_op11.place(x=770,y=350)
            lab12.place(x=50,y=45)
            op_frame11.place(x=0,y=0)
            frame_op12.place(x=1070,y=350)

            lab5.destroy()
            op_frame4.destroy()
            frame_op5.destroy()
            lab6.destroy()
            op_frame5.destroy()
            frame_op6.destroy()
            lab7.destroy()
            op_frame6.destroy()
            frame_op7.destroy()
            lab8.destroy()
            op_frame7.destroy()
            frame_op8.destroy()

            aumento()
        def var_avan2_fak():
            self.progress_in['value']+=20
            self.frame_text1.destroy()
            self.frame_text2.place(x=200,y=205)

            lab9.place(x=55,y=50)
            op_frame8.place(x=0,y=0)
            frame_op9.place(x=170,y=350)
            lab10.place(x=50,y=45)
            op_frame9.place(x=0,y=0)
            frame_op10.place(x=470,y=350)
            lab11.place(x=50,y=45)
            op_frame10.place(x=0,y=0)
            frame_op11.place(x=770,y=350)
            lab12.place(x=50,y=45)
            op_frame11.place(x=0,y=0)
            frame_op12.place(x=1070,y=350)

            lab5.destroy()
            op_frame4.destroy()
            frame_op5.destroy()
            lab6.destroy()
            op_frame5.destroy()
            frame_op6.destroy()
            lab7.destroy()
            op_frame6.destroy()
            frame_op7.destroy()
            lab8.destroy()
            op_frame7.destroy()
            frame_op8.destroy()
        def var_avan3():
            self.frame_text2.destroy()
            self.frame_text3.place(x=200,y=205)

            lab13.place(x=55,y=50)
            op_frame12.place(x=0,y=0)
            frame_op13.place(x=170,y=350)
            lab14.place(x=50,y=45)
            op_frame13.place(x=0,y=0)
            frame_op14.place(x=470,y=350)
            lab15.place(x=50,y=45)
            op_frame14.place(x=0,y=0)
            frame_op15.place(x=770,y=350)
            lab16.place(x=50,y=45)
            op_frame15.place(x=0,y=0)
            frame_op16.place(x=1070,y=350)

            lab9.destroy()
            op_frame8.destroy()
            frame_op9.destroy()
            lab10.destroy()
            op_frame9.destroy()
            frame_op10.destroy()
            lab11.destroy()
            op_frame10.destroy()
            frame_op11.destroy()
            lab12.destroy()
            op_frame11.destroy()
            frame_op12.destroy()

            aumento()
        def var_avan3_fak():
            self.progress_in['value']+=20
            self.frame_text2.destroy()
            self.frame_text3.place(x=200,y=205)

            lab13.place(x=55,y=50)
            op_frame12.place(x=0,y=0)
            frame_op13.place(x=170,y=350)
            lab14.place(x=50,y=45)
            op_frame13.place(x=0,y=0)
            frame_op14.place(x=470,y=350)
            lab15.place(x=50,y=45)
            op_frame14.place(x=0,y=0)
            frame_op15.place(x=770,y=350)
            lab16.place(x=50,y=45)
            op_frame15.place(x=0,y=0)
            frame_op16.place(x=1070,y=350)

            lab9.destroy()
            op_frame8.destroy()
            frame_op9.destroy()
            lab10.destroy()
            op_frame9.destroy()
            frame_op10.destroy()
            lab11.destroy()
            op_frame10.destroy()
            frame_op11.destroy()
            lab12.destroy()
            op_frame11.destroy()
            frame_op12.destroy()
        
        def var_avan4():
            self.frame_text3.destroy()
            self.frame_text4.place(x=200,y=205)

            lab17.place(x=55,y=50)
            op_frame16.place(x=0,y=0)
            frame_op17.place(x=170,y=350)
            lab18.place(x=50,y=45)
            op_frame17.place(x=0,y=0)
            frame_op18.place(x=470,y=350)
            lab19.place(x=50,y=45)
            op_frame18.place(x=0,y=0)
            frame_op19.place(x=770,y=350)
            lab20.place(x=50,y=45)
            op_frame19.place(x=0,y=0)
            frame_op20.place(x=1070,y=350)

            lab13.destroy()
            op_frame12.destroy()
            frame_op13.destroy()
            lab14.destroy()
            op_frame13.destroy()
            frame_op14.destroy()
            lab15.destroy()
            op_frame14.destroy()
            frame_op15.destroy()
            lab16.destroy()
            op_frame15.destroy()
            frame_op16.destroy()

            aumento()
        def var_avan4_fak():
            self.progress_in['value']+=20
            self.frame_text3.destroy()
            self.frame_text4.place(x=200,y=205)

            lab17.place(x=55,y=50)
            op_frame16.place(x=0,y=0)
            frame_op17.place(x=170,y=350)
            lab18.place(x=50,y=45)
            op_frame17.place(x=0,y=0)
            frame_op18.place(x=470,y=350)
            lab19.place(x=50,y=45)
            op_frame18.place(x=0,y=0)
            frame_op19.place(x=770,y=350)
            lab20.place(x=50,y=45)
            op_frame19.place(x=0,y=0)
            frame_op20.place(x=1070,y=350)

            lab13.destroy()
            op_frame12.destroy()
            frame_op13.destroy()
            lab14.destroy()
            op_frame13.destroy()
            frame_op14.destroy()
            lab15.destroy()
            op_frame14.destroy()
            frame_op15.destroy()
            lab16.destroy()
            op_frame15.destroy()
            frame_op16.destroy()
        def var_avan5():
            self.frame_text4.destroy()
            self.frame_text5.place(x=200,y=205)

            
            lab21.place(x=50,y=45)
            op_frame20.place(x=0,y=0)
            frame_op21.place(x=470,y=350)
            lab22.place(x=50,y=45)
            op_frame21.place(x=0,y=0)
            frame_op22.place(x=770,y=350)
        

            lab17.destroy()
            op_frame16.destroy()
            frame_op17.destroy()
            lab18.destroy()
            op_frame17.destroy()
            frame_op18.destroy()
            lab19.destroy()
            op_frame18.destroy()
            frame_op19.destroy()
            lab20.destroy()
            op_frame19.destroy()
            frame_op20.destroy()

            aumento()
        def var_avan5_fak():
            self.progress_in['value']+=20
            self.frame_text4.destroy()
            self.frame_text5.place(x=200,y=205)

            
            lab21.place(x=50,y=45)
            op_frame20.place(x=0,y=0)
            frame_op21.place(x=470,y=350)
            lab22.place(x=50,y=45)
            op_frame21.place(x=0,y=0)
            frame_op22.place(x=770,y=350)
        

            lab17.destroy()
            op_frame16.destroy()
            frame_op17.destroy()
            lab18.destroy()
            op_frame17.destroy()
            frame_op18.destroy()
            lab19.destroy()
            op_frame18.destroy()
            frame_op19.destroy()
            lab20.destroy()
            op_frame19.destroy()
            frame_op20.destroy()
        def last():
            aumento()
            self.home()
            
        def aumento():
            global coding_score
            coding_score += 1
            #print(coding_score)
            self.progress_in['value']+=20

#......................................pregunta1-------------------------------------
        def enter1(e):
            op_frame["image"] =self.op_frame2
            op_frame.image=self.op_frame2
        def leave1(e):
            op_frame["image"] =self.op_frame1
            op_frame.image=self.op_frame1
        frame_op1 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame=Button(frame_op1,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame.bind("<Enter>",enter1)
        op_frame.bind("<Leave>",leave1)
        lab1 = Label(frame_op1, text="Float", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab1.place(x=55,y=50)
        op_frame.place(x=0,y=0)
        frame_op1.place(x=170,y=350)

        def enter1(e):
            op_frame1["image"] =self.op_frame2
            op_frame1.image=self.op_frame2
        def leave1(e):
            op_frame1["image"] =self.op_frame1
            op_frame1.image=self.op_frame1
        frame_op2 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame1=Button(frame_op2,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1)
        op_frame1.bind("<Enter>",enter1)
        op_frame1.bind("<Leave>",leave1)
        lab2 = Label(frame_op2, text="String", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab2.place(x=50,y=45)
        op_frame1.place(x=0,y=0)
        frame_op2.place(x=470,y=350)

        def enter1(e):
            op_frame2["image"] =self.op_frame2
            op_frame2.image=self.op_frame2
        def leave1(e):
            op_frame2["image"] =self.op_frame1
            op_frame2.image=self.op_frame1
        frame_op3 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame2=Button(frame_op3,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame2.bind("<Enter>",enter1)
        op_frame2.bind("<Leave>",leave1)
        lab3=Label(frame_op3, text="Integer", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab3.place(x=50,y=45)
        op_frame2.place(x=0,y=0)
        frame_op3.place(x=770,y=350)
        
        def enter1(e):
            op_frame3["image"] =self.op_frame2
            op_frame3.image=self.op_frame2
        def leave1(e):
            op_frame3["image"] =self.op_frame1
            op_frame3.image=self.op_frame1
        frame_op4 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame3=Button(frame_op4,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame3.bind("<Enter>",enter1)
        op_frame3.bind("<Leave>",leave1)
        lab4 = Label(frame_op4, text="Boolean", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab4.place(x=50,y=45)
        op_frame3.place(x=0,y=0)
        frame_op4.place(x=1070,y=350)
#......................................pregunta2-------------------------------------
        def enter1(e):
            op_frame4["image"] =self.op_frame2
            op_frame4.image=self.op_frame2
        def leave1(e):
            op_frame4["image"] =self.op_frame1
            op_frame4.image=self.op_frame1
        frame_op5 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame4=Button(frame_op5,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame4.bind("<Enter>",enter1)
        op_frame4.bind("<Leave>",leave1)
        lab5 = Label(frame_op5, text="JavaScript", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame5["image"] =self.op_frame2
            op_frame5.image=self.op_frame2
        def leave1(e):
            op_frame5["image"] =self.op_frame1
            op_frame5.image=self.op_frame1
        frame_op6 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame5=Button(frame_op6,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame5.bind("<Enter>",enter1)
        op_frame5.bind("<Leave>",leave1)
        lab6 = Label(frame_op6, text="PHP", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame6["image"] =self.op_frame2
            op_frame6.image=self.op_frame2
        def leave1(e):
            op_frame6["image"] =self.op_frame1
            op_frame6.image=self.op_frame1
        frame_op7 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame6=Button(frame_op7,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame6.bind("<Enter>",enter1)
        op_frame6.bind("<Leave>",leave1)
        lab7 = Label(frame_op7, text="Java", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame7["image"] =self.op_frame2
            op_frame7.image=self.op_frame2
        def leave1(e):
            op_frame7["image"] =self.op_frame1
            op_frame7.image=self.op_frame1
        frame_op8 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame7=Button(frame_op8,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2)
        op_frame7.bind("<Enter>",enter1)
        op_frame7.bind("<Leave>",leave1)
        lab8=Label(frame_op8, text="Python", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------pregunta3--------------------------------------------------------------------------------------
        def enter1(e):
            op_frame8["image"] =self.op_frame2
            op_frame8.image=self.op_frame2
        def leave1(e):
            op_frame8["image"] =self.op_frame1
            op_frame8.image=self.op_frame1
        frame_op9 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame8=Button(frame_op9,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3)
        op_frame8.bind("<Enter>",enter1)
        op_frame8.bind("<Leave>",leave1)
        lab9 = Label(frame_op9, text="Programm", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame9["image"] =self.op_frame2
            op_frame9.image=self.op_frame2
        def leave1(e):
            op_frame9["image"] =self.op_frame1
            op_frame9.image=self.op_frame1
        frame_op10 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame9=Button(frame_op10,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame9.bind("<Enter>",enter1)
        op_frame9.bind("<Leave>",leave1)
        lab10 = Label(frame_op10, text="Variable", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame10["image"] =self.op_frame2
            op_frame10.image=self.op_frame2
        def leave1(e):
            op_frame10["image"] =self.op_frame1
            op_frame10.image=self.op_frame1
        frame_op11 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame10=Button(frame_op11,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame10.bind("<Enter>",enter1)
        op_frame10.bind("<Leave>",leave1)
        lab11 = Label(frame_op11, text="Screen", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame11["image"] =self.op_frame2
            op_frame11.image=self.op_frame2
        def leave1(e):
            op_frame11["image"] =self.op_frame1
            op_frame11.image=self.op_frame1
        frame_op12 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame11=Button(frame_op12,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame11.bind("<Enter>",enter1)
        op_frame11.bind("<Leave>",leave1)
        lab12=Label(frame_op12, text="Condition", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

#---------------------------------------------------pregunta4------------------------------------------------------------------
        def enter1(e):
            op_frame12["image"] =self.op_frame2
            op_frame12.image=self.op_frame2
        def leave1(e):
            op_frame12["image"] =self.op_frame1
            op_frame12.image=self.op_frame1
        frame_op13 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame12=Button(frame_op13,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame12.bind("<Enter>",enter1)
        op_frame12.bind("<Leave>",leave1)
        lab13 = Label(frame_op13, text="3", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame13["image"] =self.op_frame2
            op_frame13.image=self.op_frame2
        def leave1(e):
            op_frame13["image"] =self.op_frame1
            op_frame13.image=self.op_frame1
        frame_op14 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame13=Button(frame_op14,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4)
        op_frame13.bind("<Enter>",enter1)
        op_frame13.bind("<Leave>",leave1)
        lab14 = Label(frame_op14, text="2", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame14["image"] =self.op_frame2
            op_frame14.image=self.op_frame2
        def leave1(e):
            op_frame14["image"] =self.op_frame1
            op_frame14.image=self.op_frame1
        frame_op15 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame14=Button(frame_op15,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame14.bind("<Enter>",enter1)
        op_frame14.bind("<Leave>",leave1)
        lab15 = Label(frame_op15, text="10", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame15["image"] =self.op_frame2
            op_frame15.image=self.op_frame2
        def leave1(e):
            op_frame15["image"] =self.op_frame1
            op_frame15.image=self.op_frame1
        frame_op16 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame15=Button(frame_op16,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame15.bind("<Enter>",enter1)
        op_frame15.bind("<Leave>",leave1)
        lab16=Label(frame_op16, text="11", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------------pregunta5-------------------------------------------
        def enter1(e):
            op_frame16["image"] =self.op_frame2
            op_frame16.image=self.op_frame2
        def leave1(e):
            op_frame16["image"] =self.op_frame1
            op_frame16.image=self.op_frame1
        frame_op17 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame16=Button(frame_op17,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame16.bind("<Enter>",enter1)
        op_frame16.bind("<Leave>",leave1)
        lab17 = Label(frame_op17, text="CEO", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame17["image"] =self.op_frame2
            op_frame17.image=self.op_frame2
        def leave1(e):
            op_frame17["image"] =self.op_frame1
            op_frame17.image=self.op_frame1
        frame_op18 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame17=Button(frame_op18,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5)
        op_frame17.bind("<Enter>",enter1)
        op_frame17.bind("<Leave>",leave1)
        lab18 = Label(frame_op18, text="Programmer", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame18["image"] =self.op_frame2
            op_frame18.image=self.op_frame2
        def leave1(e):
            op_frame18["image"] =self.op_frame1
            op_frame18.image=self.op_frame1
        frame_op19 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame18=Button(frame_op19,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame18.bind("<Enter>",enter1)
        op_frame18.bind("<Leave>",leave1)
        lab19 = Label(frame_op19, text="Manager", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame19["image"] =self.op_frame2
            op_frame19.image=self.op_frame2
        def leave1(e):
            op_frame19["image"] =self.op_frame1
            op_frame19.image=self.op_frame1
        frame_op20 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame19=Button(frame_op20,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame19.bind("<Enter>",enter1)
        op_frame19.bind("<Leave>",leave1)
        lab20=Label(frame_op20, text="Writters", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-----------------------pregunta6--------------------------------------------------------------------

        def enter1(e):
            op_frame20["image"] =self.op_frame2
            op_frame20.image=self.op_frame2
        def leave1(e):
            op_frame20["image"] =self.op_frame1
            op_frame20.image=self.op_frame1
        frame_op21 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame20=Button(frame_op21,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame20.bind("<Enter>",enter1)
        op_frame20.bind("<Leave>",leave1)
        lab21 = Label(frame_op21, text="Yes", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame21["image"] =self.op_frame2
            op_frame21.image=self.op_frame2
        def leave1(e):
            op_frame21["image"] =self.op_frame1
            op_frame21.image=self.op_frame1
        frame_op22 = Frame(self.page2, width=165, height=120,bg="#fff")
        op_frame21=Button(frame_op22,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=last)
        op_frame21.bind("<Enter>",enter1)
        op_frame21.bind("<Leave>",leave1)
        lab22 = Label(frame_op22, text="No", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
################################################################PAGE TWO-SECOND TEST###############################################################
        progress_frame2 = Frame(self.page9, width=1325, height=70,bg ="white")
        progress_frame2.place(x=10,y=20)

        t1 = ttk.Style()
        t1.theme_use('default')
        t1.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='white',
            background='#FCBA40',
            darkcolor="light blue",
            bordercolor="#FCBA40"
        )
        self.progress_in1 = ttk.Progressbar(progress_frame2,style="custom.Horizontal.TProgressbar",orient="horizontal",length=1260,mode='determinate')
        self.progress_in1.place(x=45,y=40)

        def var_avan1():
            self.frame_text6.destroy()
            self.frame_text7.place(x=200,y=205)
            
            lab27.place(x=55,y=50)
            op_frame26.place(x=0,y=0)
            frame_op27.place(x=170,y=350)
            lab28.place(x=50,y=45)
            op_frame27.place(x=0,y=0)
            frame_op28.place(x=470,y=350)
            lab29.place(x=50,y=45)
            op_frame28.place(x=0,y=0)
            frame_op29.place(x=770,y=350)
            lab30.place(x=50,y=45)
            op_frame29.place(x=0,y=0)
            frame_op30.place(x=1070,y=350)

            frame_op23.destroy()
            op_frame22.destroy()
            lab23.destroy()
            frame_op24.destroy()
            op_frame23.destroy()
            lab24.destroy()
            frame_op25.destroy()
            op_frame24.destroy()
            lab25.destroy()
            frame_op26.destroy()
            op_frame25.destroy()
            lab26.destroy()

            aumento1()
        def var_avan1_fak():
            self.progress_in1['value']+=20
            self.frame_text6.destroy()
            self.frame_text7.place(x=200,y=205)
            
            lab27.place(x=55,y=50)
            op_frame26.place(x=0,y=0)
            frame_op27.place(x=170,y=350)
            lab28.place(x=50,y=45)
            op_frame27.place(x=0,y=0)
            frame_op28.place(x=470,y=350)
            lab29.place(x=50,y=45)
            op_frame28.place(x=0,y=0)
            frame_op29.place(x=770,y=350)
            lab30.place(x=50,y=45)
            op_frame29.place(x=0,y=0)
            frame_op30.place(x=1070,y=350)

            frame_op23.destroy()
            op_frame22.destroy()
            lab23.destroy()
            frame_op24.destroy()
            op_frame23.destroy()
            lab24.destroy()
            frame_op25.destroy()
            op_frame24.destroy()
            lab25.destroy()
            frame_op26.destroy()
            op_frame25.destroy()
            lab26.destroy()

        def var_avan2():
            self.frame_text7.destroy()
            self.frame_text8.place(x=200,y=205)

            lab31.place(x=55,y=50)
            op_frame30.place(x=0,y=0)
            frame_op31.place(x=170,y=350)
            lab32.place(x=50,y=45)
            op_frame31.place(x=0,y=0)
            frame_op32.place(x=470,y=350)
            lab33.place(x=50,y=45)
            op_frame32.place(x=0,y=0)
            frame_op33.place(x=770,y=350)
            lab34.place(x=50,y=45)
            op_frame33.place(x=0,y=0)
            frame_op34.place(x=1070,y=350)

            lab27.destroy()
            op_frame26.destroy()
            frame_op27.destroy()
            lab28.destroy()
            op_frame27.destroy()
            frame_op28.destroy()
            lab29.destroy()
            op_frame28.destroy()
            frame_op29.destroy()
            lab30.destroy()
            op_frame29.destroy()
            frame_op30.destroy()

            aumento1()
        def var_avan2_fak():
            self.progress_in1['value']+=20
            self.frame_text7.destroy()
            self.frame_text8.place(x=200,y=205)

            lab31.place(x=55,y=50)
            op_frame30.place(x=0,y=0)
            frame_op31.place(x=170,y=350)
            lab32.place(x=50,y=45)
            op_frame31.place(x=0,y=0)
            frame_op32.place(x=470,y=350)
            lab33.place(x=50,y=45)
            op_frame32.place(x=0,y=0)
            frame_op33.place(x=770,y=350)
            lab34.place(x=50,y=45)
            op_frame33.place(x=0,y=0)
            frame_op34.place(x=1070,y=350)

            lab27.destroy()
            op_frame26.destroy()
            frame_op27.destroy()
            lab28.destroy()
            op_frame27.destroy()
            frame_op28.destroy()
            lab29.destroy()
            op_frame28.destroy()
            frame_op29.destroy()
            lab30.destroy()
            op_frame29.destroy()
            frame_op30.destroy()
        def var_avan3():
            self.frame_text8.destroy()
            self.frame_text9.place(x=200,y=205)

            lab35.place(x=55,y=50)
            op_frame34.place(x=0,y=0)
            frame_op35.place(x=170,y=350)
            lab36.place(x=50,y=45)
            op_frame35.place(x=0,y=0)
            frame_op36.place(x=470,y=350)
            lab37.place(x=50,y=45)
            op_frame36.place(x=0,y=0)
            frame_op37.place(x=770,y=350)
            lab38.place(x=50,y=45)
            op_frame37.place(x=0,y=0)
            frame_op38.place(x=1070,y=350)

            lab31.destroy()
            op_frame30.destroy()
            frame_op31.destroy()
            lab32.destroy()
            op_frame31.destroy()
            frame_op32.destroy()
            lab33.destroy()
            op_frame32.destroy()
            frame_op33.destroy()
            lab34.destroy()
            op_frame33.destroy()
            frame_op34.destroy()

            aumento1()
        def var_avan3_fak():
            self.progress_in1['value']+=20
            self.frame_text8.destroy()
            self.frame_text9.place(x=200,y=205)

            lab35.place(x=55,y=50)
            op_frame34.place(x=0,y=0)
            frame_op35.place(x=170,y=350)
            lab36.place(x=50,y=45)
            op_frame35.place(x=0,y=0)
            frame_op36.place(x=470,y=350)
            lab37.place(x=50,y=45)
            op_frame36.place(x=0,y=0)
            frame_op37.place(x=770,y=350)
            lab38.place(x=50,y=45)
            op_frame37.place(x=0,y=0)
            frame_op38.place(x=1070,y=350)

            lab31.destroy()
            op_frame30.destroy()
            frame_op31.destroy()
            lab32.destroy()
            op_frame31.destroy()
            frame_op32.destroy()
            lab33.destroy()
            op_frame32.destroy()
            frame_op33.destroy()
            lab34.destroy()
            op_frame33.destroy()
            frame_op34.destroy()
        
        def var_avan4():
            self.frame_text9.destroy()
            self.frame_text10.place(x=200,y=105)

            lab39.place(x=55,y=50)
            op_frame38.place(x=0,y=0)
            frame_op39.place(x=170,y=350)
            lab40.place(x=50,y=45)
            op_frame39.place(x=0,y=0)
            frame_op40.place(x=470,y=350)
            lab41.place(x=50,y=45)
            op_frame40.place(x=0,y=0)
            frame_op41.place(x=770,y=350)
            lab42.place(x=50,y=45)
            op_frame41.place(x=0,y=0)
            frame_op42.place(x=1070,y=350)

            lab35.destroy()
            op_frame34.destroy()
            frame_op35.destroy()
            lab36.destroy()
            op_frame35.destroy()
            frame_op36.destroy()
            lab37.destroy()
            op_frame36.destroy()
            frame_op37.destroy()
            lab38.destroy()
            op_frame37.destroy()
            frame_op38.destroy()

            aumento1()
        def var_avan4_fak():
            self.progress_in1['value']+=20
            self.frame_text9.destroy()
            self.frame_text10.place(x=200,y=105)

            lab39.place(x=55,y=50)
            op_frame38.place(x=0,y=0)
            frame_op39.place(x=170,y=350)
            lab40.place(x=50,y=45)
            op_frame39.place(x=0,y=0)
            frame_op40.place(x=470,y=350)
            lab41.place(x=50,y=45)
            op_frame40.place(x=0,y=0)
            frame_op41.place(x=770,y=350)
            lab42.place(x=50,y=45)
            op_frame41.place(x=0,y=0)
            frame_op42.place(x=1070,y=350)

            lab35.destroy()
            op_frame34.destroy()
            frame_op35.destroy()
            lab36.destroy()
            op_frame35.destroy()
            frame_op36.destroy()
            lab37.destroy()
            op_frame36.destroy()
            frame_op37.destroy()
            lab38.destroy()
            op_frame37.destroy()
            frame_op38.destroy()
        def var_avan5():
            self.frame_text10.destroy()
            self.frame_text11.place(x=200,y=105)

            
            lab43.place(x=55,y=50)
            op_frame42.place(x=0,y=0)
            frame_op43.place(x=170,y=350)
            lab44.place(x=50,y=45)
            op_frame43.place(x=0,y=0)
            frame_op44.place(x=470,y=350)
            lab45.place(x=50,y=45)
            op_frame44.place(x=0,y=0)
            frame_op45.place(x=770,y=350)
            lab46.place(x=50,y=45)
            op_frame45.place(x=0,y=0)
            frame_op46.place(x=1070,y=350)
        

            lab39.destroy()
            op_frame38.destroy()
            frame_op39.destroy()
            lab40.destroy()
            op_frame39.destroy()
            frame_op40.destroy()
            lab41.destroy()
            op_frame40.destroy()
            frame_op41.destroy()
            lab42.destroy()
            op_frame41.destroy()
            frame_op42.destroy()

            aumento1()
        def var_avan5_fak():
            self.progress_in1['value']+=20
            self.frame_text10.destroy()
            self.frame_text11.place(x=200,y=105)

            
            lab43.place(x=55,y=50)
            op_frame42.place(x=0,y=0)
            frame_op43.place(x=170,y=350)
            lab44.place(x=50,y=45)
            op_frame43.place(x=0,y=0)
            frame_op44.place(x=470,y=350)
            lab45.place(x=50,y=45)
            op_frame44.place(x=0,y=0)
            frame_op45.place(x=770,y=350)
            lab46.place(x=50,y=45)
            op_frame45.place(x=0,y=0)
            frame_op46.place(x=1070,y=350)
        

            lab39.destroy()
            op_frame38.destroy()
            frame_op39.destroy()
            lab40.destroy()
            op_frame39.destroy()
            frame_op40.destroy()
            lab41.destroy()
            op_frame40.destroy()
            frame_op41.destroy()
            lab42.destroy()
            op_frame41.destroy()
            frame_op42.destroy()

        def last1():
            aumento1()
            self.home()
            
        def aumento1():
            global math_score
            math_score += 1
            #print(coding_score)
            self.progress_in1['value']+=20

        def enter1(e):
            op_frame22["image"] =self.op_frame2
            op_frame22.image=self.op_frame2
        def leave1(e):
            op_frame22["image"] =self.op_frame1
            op_frame22.image=self.op_frame1
        frame_op23 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame22=Button(frame_op23,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame22.bind("<Enter>",enter1)
        op_frame22.bind("<Leave>",leave1)
        lab23 = Label(frame_op23, text="10", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab23.place(x=55,y=50)
        op_frame22.place(x=0,y=0)
        frame_op23.place(x=170,y=350)

        def enter1(e):
            op_frame23["image"] =self.op_frame2
            op_frame23.image=self.op_frame2
        def leave1(e):
            op_frame23["image"] =self.op_frame1
            op_frame23.image=self.op_frame1
        frame_op24 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame23=Button(frame_op24,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame23.bind("<Enter>",enter1)
        op_frame23.bind("<Leave>",leave1)
        lab24 = Label(frame_op24, text="20", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab24.place(x=50,y=45)
        op_frame23.place(x=0,y=0)
        frame_op24.place(x=470,y=350)

        def enter1(e):
            op_frame24["image"] =self.op_frame2
            op_frame24.image=self.op_frame2
        def leave1(e):
            op_frame24["image"] =self.op_frame1
            op_frame24.image=self.op_frame1
        frame_op25 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame24=Button(frame_op25,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1)
        op_frame24.bind("<Enter>",enter1)
        op_frame24.bind("<Leave>",leave1)
        lab25=Label(frame_op25, text="18", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab25.place(x=50,y=45)
        op_frame24.place(x=0,y=0)
        frame_op25.place(x=770,y=350)
        
        def enter1(e):
            op_frame25["image"] =self.op_frame2
            op_frame25.image=self.op_frame2
        def leave1(e):
            op_frame25["image"] =self.op_frame1
            op_frame25.image=self.op_frame1
        frame_op26 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame25=Button(frame_op26,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame25.bind("<Enter>",enter1)
        op_frame25.bind("<Leave>",leave1)
        lab26 = Label(frame_op26, text="21", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab26.place(x=50,y=45)
        op_frame25.place(x=0,y=0)
        frame_op26.place(x=1070,y=350)
#......................................pregunta2-------------------------------------
        def enter1(e):
            op_frame26["image"] =self.op_frame2
            op_frame26.image=self.op_frame2
        def leave1(e):
            op_frame26["image"] =self.op_frame1
            op_frame26.image=self.op_frame1
        frame_op27 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame26=Button(frame_op27,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame26.bind("<Enter>",enter1)
        op_frame26.bind("<Leave>",leave1)
        lab27 = Label(frame_op27, text="56", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame27["image"] =self.op_frame2
            op_frame27.image=self.op_frame2
        def leave1(e):
            op_frame27["image"] =self.op_frame1
            op_frame27.image=self.op_frame1
        frame_op28 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame27=Button(frame_op28,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2)
        op_frame27.bind("<Enter>",enter1)
        op_frame27.bind("<Leave>",leave1)
        lab28 = Label(frame_op28, text="54", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame28["image"] =self.op_frame2
            op_frame28.image=self.op_frame2
        def leave1(e):
            op_frame28["image"] =self.op_frame1
            op_frame28.image=self.op_frame1
        frame_op29 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame28=Button(frame_op29,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame28.bind("<Enter>",enter1)
        op_frame28.bind("<Leave>",leave1)
        lab29 = Label(frame_op29, text="46", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame29["image"] =self.op_frame2
            op_frame29.image=self.op_frame2
        def leave1(e):
            op_frame29["image"] =self.op_frame1
            op_frame29.image=self.op_frame1
        frame_op30 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame29=Button(frame_op30,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame29.bind("<Enter>",enter1)
        op_frame29.bind("<Leave>",leave1)
        lab30=Label(frame_op30, text="60", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------pregunta3--------------------------------------------------------------------------------------
        def enter1(e):
            op_frame30["image"] =self.op_frame2
            op_frame30.image=self.op_frame2
        def leave1(e):
            op_frame30["image"] =self.op_frame1
            op_frame30.image=self.op_frame1
        frame_op31 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame30=Button(frame_op31,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame30.bind("<Enter>",enter1)
        op_frame30.bind("<Leave>",leave1)
        lab31 = Label(frame_op31, text="54", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame31["image"] =self.op_frame2
            op_frame31.image=self.op_frame2
        def leave1(e):
            op_frame31["image"] =self.op_frame1
            op_frame31.image=self.op_frame1
        frame_op32 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame31=Button(frame_op32,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3)
        op_frame31.bind("<Enter>",enter1)
        op_frame31.bind("<Leave>",leave1)
        lab32 = Label(frame_op32, text="48", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame32["image"] =self.op_frame2
            op_frame32.image=self.op_frame2
        def leave1(e):
            op_frame32["image"] =self.op_frame1
            op_frame32.image=self.op_frame1
        frame_op33 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame32=Button(frame_op33,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame32.bind("<Enter>",enter1)
        op_frame32.bind("<Leave>",leave1)
        lab33 = Label(frame_op33, text="46", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame33["image"] =self.op_frame2
            op_frame33.image=self.op_frame2
        def leave1(e):
            op_frame33["image"] =self.op_frame1
            op_frame33.image=self.op_frame1
        frame_op34 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame33=Button(frame_op34,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame33.bind("<Enter>",enter1)
        op_frame33.bind("<Leave>",leave1)
        lab34=Label(frame_op34, text="12", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

#---------------------------------------------------pregunta4------------------------------------------------------------------
        def enter1(e):
            op_frame34["image"] =self.op_frame2
            op_frame34.image=self.op_frame2
        def leave1(e):
            op_frame34["image"] =self.op_frame1
            op_frame34.image=self.op_frame1
        frame_op35 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame34=Button(frame_op35,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame34.bind("<Enter>",enter1)
        op_frame34.bind("<Leave>",leave1)
        lab35 = Label(frame_op35, text="5", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame35["image"] =self.op_frame2
            op_frame35.image=self.op_frame2
        def leave1(e):
            op_frame35["image"] =self.op_frame1
            op_frame35.image=self.op_frame1
        frame_op36 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame35=Button(frame_op36,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame35.bind("<Enter>",enter1)
        op_frame35.bind("<Leave>",leave1)
        lab36 = Label(frame_op36, text="2", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame36["image"] =self.op_frame2
            op_frame36.image=self.op_frame2
        def leave1(e):
            op_frame36["image"] =self.op_frame1
            op_frame36.image=self.op_frame1
        frame_op37 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame36=Button(frame_op37,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4)
        op_frame36.bind("<Enter>",enter1)
        op_frame36.bind("<Leave>",leave1)
        lab37 = Label(frame_op37, text="4", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame37["image"] =self.op_frame2
            op_frame37.image=self.op_frame2
        def leave1(e):
            op_frame37["image"] =self.op_frame1
            op_frame37.image=self.op_frame1
        frame_op38 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame37=Button(frame_op38,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame37.bind("<Enter>",enter1)
        op_frame37.bind("<Leave>",leave1)
        lab38=Label(frame_op38, text="6", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------------pregunta5-------------------------------------------
        def enter1(e):
            op_frame38["image"] =self.op_frame2
            op_frame38.image=self.op_frame2
        def leave1(e):
            op_frame38["image"] =self.op_frame1
            op_frame38.image=self.op_frame1
        frame_op39 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame38=Button(frame_op39,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame38.bind("<Enter>",enter1)
        op_frame38.bind("<Leave>",leave1)
        lab39 = Label(frame_op39, text="5", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame39["image"] =self.op_frame2
            op_frame39.image=self.op_frame2
        def leave1(e):
            op_frame39["image"] =self.op_frame1
            op_frame39.image=self.op_frame1
        frame_op40 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame39=Button(frame_op40,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5)
        op_frame39.bind("<Enter>",enter1)
        op_frame39.bind("<Leave>",leave1)
        lab40 = Label(frame_op40, text="1", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame40["image"] =self.op_frame2
            op_frame40.image=self.op_frame2
        def leave1(e):
            op_frame40["image"] =self.op_frame1
            op_frame40.image=self.op_frame1
        frame_op41 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame40=Button(frame_op41,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame40.bind("<Enter>",enter1)
        op_frame40.bind("<Leave>",leave1)
        lab41 = Label(frame_op41, text="0", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame41["image"] =self.op_frame2
            op_frame41.image=self.op_frame2
        def leave1(e):
            op_frame41["image"] =self.op_frame1
            op_frame41.image=self.op_frame1
        frame_op42 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame41=Button(frame_op42,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame41.bind("<Enter>",enter1)
        op_frame41.bind("<Leave>",leave1)
        lab42=Label(frame_op42, text="2", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-----------------------pregunta6--------------------------------------------------------------------

        def enter1(e):
            op_frame42["image"] =self.op_frame2
            op_frame42.image=self.op_frame2
        def leave1(e):
            op_frame42["image"] =self.op_frame1
            op_frame42.image=self.op_frame1
        frame_op43 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame42=Button(frame_op43,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame42.bind("<Enter>",enter1)
        op_frame42.bind("<Leave>",leave1)
        lab43 = Label(frame_op43, text="65", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame43["image"] =self.op_frame2
            op_frame43.image=self.op_frame2
        def leave1(e):
            op_frame43["image"] =self.op_frame1
            op_frame43.image=self.op_frame1
        frame_op44 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame43=Button(frame_op44,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame43.bind("<Enter>",enter1)
        op_frame43.bind("<Leave>",leave1)
        lab44 = Label(frame_op44, text="78", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

        def enter1(e):
            op_frame44["image"] =self.op_frame2
            op_frame44.image=self.op_frame2
        def leave1(e):
            op_frame44["image"] =self.op_frame1
            op_frame44.image=self.op_frame1
        frame_op45 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame44=Button(frame_op45,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame44.bind("<Enter>",enter1)
        op_frame44.bind("<Leave>",leave1)
        lab45 = Label(frame_op45, text="68", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        def enter1(e):
            op_frame45["image"] =self.op_frame2
            op_frame45.image=self.op_frame2
        def leave1(e):
            op_frame45["image"] =self.op_frame1
            op_frame45.image=self.op_frame1
        frame_op46 = Frame(self.page9, width=165, height=120,bg="#fff")
        op_frame45=Button(frame_op46,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=last1)
        op_frame45.bind("<Enter>",enter1)
        op_frame45.bind("<Leave>",leave1)
        lab46 = Label(frame_op46, text="87", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

################################################################PAGE TWO-THIRD TEST###############################################################
        progress_frame3 = Frame(self.page10, width=1325, height=70,bg ="white")
        progress_frame3.place(x=10,y=20)

        t2 = ttk.Style()
        t2.theme_use('default')
        t2.configure(
            "custom.Horizontal.TProgressbar",
            troughcolor='white',
            background='#FCBA40',
            darkcolor="light blue",
            bordercolor="#FCBA40"
        )
        self.progress_in2 = ttk.Progressbar(progress_frame3,style="custom.Horizontal.TProgressbar",orient="horizontal",length=1260,mode='determinate')
        self.progress_in2.place(x=45,y=40)

        def var_avan1():
            self.frame_text12.destroy()
            self.frame_text13.place(x=200,y=205)
            
            lab51.place(x=55,y=50)
            op_frame50.place(x=0,y=0)
            frame_op51.place(x=170,y=350)
            lab52.place(x=50,y=45)
            op_frame51.place(x=0,y=0)
            frame_op52.place(x=470,y=350)
            lab53.place(x=50,y=45)
            op_frame52.place(x=0,y=0)
            frame_op53.place(x=770,y=350)
            lab54.place(x=50,y=45)
            op_frame53.place(x=0,y=0)
            frame_op54.place(x=1070,y=350)

            frame_op47.destroy()
            op_frame46.destroy()
            lab47.destroy()
            frame_op48.destroy()
            op_frame47.destroy()
            lab48.destroy()
            frame_op49.destroy()
            op_frame48.destroy()
            lab49.destroy()
            frame_op50.destroy()
            op_frame49.destroy()
            lab50.destroy()

            aumento2()
        def var_avan1_fak():
            self.progress_in2['value']+=20
            self.frame_text12.destroy()
            self.frame_text13.place(x=200,y=205)
            
            lab51.place(x=55,y=50)
            op_frame50.place(x=0,y=0)
            frame_op51.place(x=170,y=350)
            lab52.place(x=50,y=45)
            op_frame51.place(x=0,y=0)
            frame_op52.place(x=470,y=350)
            lab53.place(x=50,y=45)
            op_frame52.place(x=0,y=0)
            frame_op53.place(x=770,y=350)
            lab54.place(x=50,y=45)
            op_frame53.place(x=0,y=0)
            frame_op54.place(x=1070,y=350)

            frame_op47.destroy()
            op_frame46.destroy()
            lab47.destroy()
            frame_op48.destroy()
            op_frame47.destroy()
            lab48.destroy()
            frame_op49.destroy()
            op_frame48.destroy()
            lab49.destroy()
            frame_op50.destroy()
            op_frame49.destroy()
            lab50.destroy()

        def var_avan2():
            self.frame_text13.destroy()
            self.frame_text14.place(x=200,y=205)

            lab55.place(x=55,y=50)
            op_frame54.place(x=0,y=0)
            frame_op55.place(x=170,y=350)
            lab56.place(x=50,y=45)
            op_frame55.place(x=0,y=0)
            frame_op56.place(x=470,y=350)
            lab57.place(x=50,y=45)
            op_frame56.place(x=0,y=0)
            frame_op57.place(x=770,y=350)
            lab58.place(x=50,y=45)
            op_frame57.place(x=0,y=0)
            frame_op58.place(x=1070,y=350)

            lab51.destroy()
            op_frame50.destroy()
            frame_op51.destroy()
            lab52.destroy()
            op_frame51.destroy()
            frame_op52.destroy()
            lab53.destroy()
            op_frame52.destroy()
            frame_op53.destroy()
            lab54.destroy()
            op_frame53.destroy()
            frame_op54.destroy()

            aumento2()
        def var_avan2_fak():
            self.progress_in2['value']+=20
            self.frame_text13.destroy()
            self.frame_text14.place(x=200,y=205)

            lab55.place(x=55,y=50)
            op_frame54.place(x=0,y=0)
            frame_op55.place(x=170,y=350)
            lab56.place(x=50,y=45)
            op_frame55.place(x=0,y=0)
            frame_op56.place(x=470,y=350)
            lab57.place(x=50,y=45)
            op_frame56.place(x=0,y=0)
            frame_op57.place(x=770,y=350)
            lab58.place(x=50,y=45)
            op_frame57.place(x=0,y=0)
            frame_op58.place(x=1070,y=350)

            lab51.destroy()
            op_frame50.destroy()
            frame_op51.destroy()
            lab52.destroy()
            op_frame51.destroy()
            frame_op52.destroy()
            lab53.destroy()
            op_frame52.destroy()
            frame_op53.destroy()
            lab54.destroy()
            op_frame53.destroy()
            frame_op54.destroy()
        def var_avan3():
            self.frame_text14.destroy()
            self.frame_text15.place(x=200,y=205)

            lab59.place(x=55,y=50)
            op_frame58.place(x=0,y=0)
            frame_op59.place(x=170,y=350)
            lab60.place(x=50,y=45)
            op_frame59.place(x=0,y=0)
            frame_op60.place(x=470,y=350)
            lab61.place(x=50,y=45)
            op_frame60.place(x=0,y=0)
            frame_op61.place(x=770,y=350)
            lab62.place(x=50,y=45)
            op_frame61.place(x=0,y=0)
            frame_op62.place(x=1070,y=350)

            lab55.destroy()
            op_frame54.destroy()
            frame_op55.destroy()
            lab56.destroy()
            op_frame55.destroy()
            frame_op56.destroy()
            lab57.destroy()
            op_frame56.destroy()
            frame_op57.destroy()
            lab58.destroy()
            op_frame57.destroy()
            frame_op58.destroy()

            aumento2()
        def var_avan3_fak():
            self.progress_in2['value']+=20
            self.frame_text14.destroy()
            self.frame_text15.place(x=200,y=205)

            lab59.place(x=55,y=50)
            op_frame58.place(x=0,y=0)
            frame_op59.place(x=170,y=350)
            lab60.place(x=50,y=45)
            op_frame59.place(x=0,y=0)
            frame_op60.place(x=470,y=350)
            lab61.place(x=50,y=45)
            op_frame60.place(x=0,y=0)
            frame_op61.place(x=770,y=350)
            lab62.place(x=50,y=45)
            op_frame61.place(x=0,y=0)
            frame_op62.place(x=1070,y=350)

            lab55.destroy()
            op_frame54.destroy()
            frame_op55.destroy()
            lab56.destroy()
            op_frame55.destroy()
            frame_op56.destroy()
            lab57.destroy()
            op_frame56.destroy()
            frame_op57.destroy()
            lab58.destroy()
            op_frame57.destroy()
            frame_op58.destroy()
        
        def var_avan4():
            self.frame_text15.destroy()
            self.frame_text16.place(x=200,y=205)

            
            lab64.place(x=50,y=45)
            op_frame63.place(x=0,y=0)
            frame_op64.place(x=470,y=350)
            lab65.place(x=50,y=45)
            op_frame64.place(x=0,y=0)
            frame_op65.place(x=770,y=350)
            

            lab59.destroy()
            op_frame58.destroy()
            frame_op59.destroy()
            lab60.destroy()
            op_frame59.destroy()
            frame_op60.destroy()
            lab61.destroy()
            op_frame60.destroy()
            frame_op61.destroy()
            lab62.destroy()
            op_frame61.destroy()
            frame_op62.destroy()

            aumento2()
        def var_avan4_fak():
            self.progress_in2['value']+=20
            self.frame_text15.destroy()
            self.frame_text16.place(x=200,y=105)

            
            lab64.place(x=50,y=45)
            op_frame63.place(x=0,y=0)
            frame_op64.place(x=470,y=350)
            lab65.place(x=50,y=45)
            op_frame64.place(x=0,y=0)
            frame_op65.place(x=770,y=350)
           

            lab59.destroy()
            op_frame58.destroy()
            frame_op59.destroy()
            lab60.destroy()
            op_frame59.destroy()
            frame_op60.destroy()
            lab61.destroy()
            op_frame60.destroy()
            frame_op61.destroy()
            lab62.destroy()
            op_frame61.destroy()
            frame_op62.destroy()
        def var_avan5():
            self.frame_text16.destroy()
            self.frame_text17.place(x=200,y=205)

            
            lab67.place(x=55,y=50)
            op_frame66.place(x=0,y=0)
            frame_op67.place(x=170,y=350)
            lab68.place(x=50,y=45)
            op_frame67.place(x=0,y=0)
            frame_op68.place(x=470,y=350)
            lab69.place(x=50,y=45)
            op_frame68.place(x=0,y=0)
            frame_op69.place(x=770,y=350)
            lab70.place(x=50,y=45)
            op_frame69.place(x=0,y=0)
            frame_op70.place(x=1070,y=350)
        

            
            lab64.destroy()
            op_frame63.destroy()
            frame_op64.destroy()
            lab65.destroy()
            op_frame64.destroy()
            frame_op65.destroy()
            

            aumento2()
        def var_avan5_fak():
            self.progress_in2['value']+=20
            self.frame_text16.destroy()
            self.frame_text17.place(x=200,y=205)

            
            lab67.place(x=55,y=50)
            op_frame66.place(x=0,y=0)
            frame_op67.place(x=170,y=350)
            lab68.place(x=50,y=45)
            op_frame67.place(x=0,y=0)
            frame_op68.place(x=470,y=350)
            lab69.place(x=50,y=45)
            op_frame68.place(x=0,y=0)
            frame_op69.place(x=770,y=350)
            lab70.place(x=50,y=45)
            op_frame69.place(x=0,y=0)
            frame_op70.place(x=1070,y=350)
        

            
            lab64.destroy()
            op_frame63.destroy()
            frame_op64.destroy()
            lab65.destroy()
            op_frame64.destroy()
            frame_op65.destroy()
            

        def last2():
            aumento2()
            self.home()
            
        def aumento2():
            global logic_score
            logic_score += 1
            self.progress_in2['value']+=20

        def enter1(e):
            op_frame46["image"] =self.op_frame2
            op_frame46.image=self.op_frame2
        def leave1(e):
            op_frame46["image"] =self.op_frame1
            op_frame46.image=self.op_frame1

        frame_op47 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame46=Button(frame_op47,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame46.bind("<Enter>",enter1)
        op_frame46.bind("<Leave>",leave1)
        lab47 = Label(frame_op47, text="First", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab47.place(x=55,y=50)
        op_frame46.place(x=0,y=0)
        frame_op47.place(x=170,y=350)

        def enter1(e):
            op_frame47["image"] =self.op_frame2
            op_frame47.image=self.op_frame2
        def leave1(e):
            op_frame47["image"] =self.op_frame1
            op_frame47.image=self.op_frame1
        frame_op48 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame47=Button(frame_op48,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1)
        op_frame47.bind("<Enter>",enter1)
        op_frame47.bind("<Leave>",leave1)
        lab48 = Label(frame_op48, text="Second", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab48.place(x=50,y=45)
        op_frame47.place(x=0,y=0)
        frame_op48.place(x=470,y=350)

        def enter1(e):
            op_frame48["image"] =self.op_frame2
            op_frame48.image=self.op_frame2
        def leave1(e):
            op_frame48["image"] =self.op_frame1
            op_frame48.image=self.op_frame1
        frame_op49 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame48=Button(frame_op49,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame48.bind("<Enter>",enter1)
        op_frame48.bind("<Leave>",leave1)
        lab49=Label(frame_op49, text="Third", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab49.place(x=50,y=45)
        op_frame48.place(x=0,y=0)
        frame_op49.place(x=770,y=350)
        
        def enter1(e):
            op_frame49["image"] =self.op_frame2
            op_frame49.image=self.op_frame2
        def leave1(e):
            op_frame49["image"] =self.op_frame1
            op_frame49.image=self.op_frame1
        frame_op50 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame49=Button(frame_op50,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan1_fak)
        op_frame49.bind("<Enter>",enter1)
        op_frame49.bind("<Leave>",leave1)
        lab50 = Label(frame_op50, text="Fourth", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        lab50.place(x=50,y=45)
        op_frame49.place(x=0,y=0)
        frame_op50.place(x=1070,y=350)
#......................................pregunta2-------------------------------------
        def enter1(e):
            op_frame50["image"] =self.op_frame2
            op_frame50.image=self.op_frame2
        def leave1(e):
            op_frame50["image"] =self.op_frame1
            op_frame50.image=self.op_frame1
        frame_op51 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame50=Button(frame_op51,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame50.bind("<Enter>",enter1)
        op_frame50.bind("<Leave>",leave1)
        lab51 = Label(frame_op51, text="30", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame51["image"] =self.op_frame2
            op_frame51.image=self.op_frame2
        def leave1(e):
            op_frame51["image"] =self.op_frame1
            op_frame51.image=self.op_frame1
        frame_op52 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame51=Button(frame_op52,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame51.bind("<Enter>",enter1)
        op_frame51.bind("<Leave>",leave1)
        lab52 = Label(frame_op52, text="60", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame52["image"] =self.op_frame2
            op_frame52.image=self.op_frame2
        def leave1(e):
            op_frame52["image"] =self.op_frame1
            op_frame52.image=self.op_frame1
        frame_op53 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame52=Button(frame_op53,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2)
        op_frame52.bind("<Enter>",enter1)
        op_frame52.bind("<Leave>",leave1)
        lab53 = Label(frame_op53, text="12", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame53["image"] =self.op_frame2
            op_frame53.image=self.op_frame2
        def leave1(e):
            op_frame53["image"] =self.op_frame1
            op_frame53.image=self.op_frame1
        frame_op54 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame53=Button(frame_op54,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan2_fak)
        op_frame53.bind("<Enter>",enter1)
        op_frame53.bind("<Leave>",leave1)
        lab54=Label(frame_op54, text="1", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------pregunta3--------------------------------------------------------------------------------------
        def enter1(e):
            op_frame54["image"] =self.op_frame2
            op_frame54.image=self.op_frame2
        def leave1(e):
            op_frame54["image"] =self.op_frame1
            op_frame54.image=self.op_frame1
        frame_op55 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame54=Button(frame_op55,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame54.bind("<Enter>",enter1)
        op_frame54.bind("<Leave>",leave1)
        lab55 = Label(frame_op55, text="8", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame55["image"] =self.op_frame2
            op_frame55.image=self.op_frame2
        def leave1(e):
            op_frame55["image"] =self.op_frame1
            op_frame55.image=self.op_frame1
        frame_op56 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame55=Button(frame_op56,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame55.bind("<Enter>",enter1)
        op_frame55.bind("<Leave>",leave1)
        lab56 = Label(frame_op56, text="13", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame56["image"] =self.op_frame2
            op_frame56.image=self.op_frame2
        def leave1(e):
            op_frame56["image"] =self.op_frame1
            op_frame56.image=self.op_frame1
        frame_op57 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame56=Button(frame_op57,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3_fak)
        op_frame56.bind("<Enter>",enter1)
        op_frame56.bind("<Leave>",leave1)
        lab57 = Label(frame_op57, text="12", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame57["image"] =self.op_frame2
            op_frame57.image=self.op_frame2
        def leave1(e):
            op_frame57["image"] =self.op_frame1
            op_frame57.image=self.op_frame1
        frame_op58 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame57=Button(frame_op58,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan3)
        op_frame57.bind("<Enter>",enter1)
        op_frame57.bind("<Leave>",leave1)
        lab58=Label(frame_op58, text="1", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

#---------------------------------------------------pregunta4------------------------------------------------------------------
        def enter1(e):
            op_frame58["image"] =self.op_frame2
            op_frame58.image=self.op_frame2
        def leave1(e):
            op_frame58["image"] =self.op_frame1
            op_frame58.image=self.op_frame1
        frame_op59 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame58=Button(frame_op59,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4)
        op_frame58.bind("<Enter>",enter1)
        op_frame58.bind("<Leave>",leave1)
        lab59 = Label(frame_op59, text="9", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame59["image"] =self.op_frame2
            op_frame59.image=self.op_frame2
        def leave1(e):
            op_frame59["image"] =self.op_frame1
            op_frame59.image=self.op_frame1
        frame_op60 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame59=Button(frame_op60,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame59.bind("<Enter>",enter1)
        op_frame59.bind("<Leave>",leave1)
        lab60 = Label(frame_op60, text="17", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame60["image"] =self.op_frame2
            op_frame60.image=self.op_frame2
        def leave1(e):
            op_frame60["image"] =self.op_frame1
            op_frame60.image=self.op_frame1
        frame_op61 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame60=Button(frame_op61,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame60.bind("<Enter>",enter1)
        op_frame60.bind("<Leave>",leave1)
        lab61 = Label(frame_op61, text="1", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        
        def enter1(e):
            op_frame61["image"] =self.op_frame2
            op_frame61.image=self.op_frame2
        def leave1(e):
            op_frame61["image"] =self.op_frame1
            op_frame61.image=self.op_frame1
        frame_op62 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame61=Button(frame_op62,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan4_fak)
        op_frame61.bind("<Enter>",enter1)
        op_frame61.bind("<Leave>",leave1)
        lab62=Label(frame_op62, text="None", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
#-------------------------------pregunta5-------------------------------------------

        def enter1(e):
            op_frame63["image"] =self.op_frame2
            op_frame63.image=self.op_frame2
        def leave1(e):
            op_frame63["image"] =self.op_frame1
            op_frame63.image=self.op_frame1
        frame_op64 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame63=Button(frame_op64,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5_fak)
        op_frame63.bind("<Enter>",enter1)
        op_frame63.bind("<Leave>",leave1)
        lab64 = Label(frame_op64, text="SI", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame64["image"] =self.op_frame2
            op_frame64.image=self.op_frame2
        def leave1(e):
            op_frame64["image"] =self.op_frame1
            op_frame64.image=self.op_frame1
        frame_op65 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame64=Button(frame_op65,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=var_avan5)
        op_frame64.bind("<Enter>",enter1)
        op_frame64.bind("<Leave>",leave1)
        lab65 = Label(frame_op65, text="NO", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

#-----------------------pregunta6--------------------------------------------------------------------

        def enter1(e):
            op_frame66["image"] =self.op_frame2
            op_frame66.image=self.op_frame2
        def leave1(e):
            op_frame66["image"] =self.op_frame1
            op_frame66.image=self.op_frame1
        frame_op67 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame66=Button(frame_op67,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame66.bind("<Enter>",enter1)
        op_frame66.bind("<Leave>",leave1)
        lab67 = Label(frame_op67, text="6", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        

        def enter1(e):
            op_frame67["image"] =self.op_frame2
            op_frame67.image=self.op_frame2
        def leave1(e):
            op_frame67["image"] =self.op_frame1
            op_frame67.image=self.op_frame1
        frame_op68 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame67=Button(frame_op68,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame67.bind("<Enter>",enter1)
        op_frame67.bind("<Leave>",leave1)
        lab68 = Label(frame_op68, text="9", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

        def enter1(e):
            op_frame68["image"] =self.op_frame2
            op_frame68.image=self.op_frame2
        def leave1(e):
            op_frame68["image"] =self.op_frame1
            op_frame68.image=self.op_frame1
        frame_op69 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame68=Button(frame_op69,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=self.home)
        op_frame68.bind("<Enter>",enter1)
        op_frame68.bind("<Leave>",leave1)
        lab69 = Label(frame_op69, text="3", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")
        
        def enter1(e):
            op_frame69["image"] =self.op_frame2
            op_frame69.image=self.op_frame2
        def leave1(e):
            op_frame69["image"] =self.op_frame1
            op_frame69.image=self.op_frame1
        frame_op70 = Frame(self.page10, width=165, height=120,bg="#fff")
        op_frame69=Button(frame_op70,image=self.op_frame1,bg="#fff",bd=0,activebackground="#fff",command=last2)
        op_frame69.bind("<Enter>",enter1)
        op_frame69.bind("<Leave>",leave1)
        lab70 = Label(frame_op70, text="4", fg="#035596",font=('Microsoft YaHei UI Light', 13),bg="#fff")

################################################################PAGE THREE###############################################################
        def refresh():
            global tamaño
            #tamaño = [coding_score,math_score,pseint_score,logic_score]
            tamaño = [2,math_score,5,6]
            axs[0].bar(nombres,tamaño,color=colores)
            axs[1].plot(nombres,tamaño,color="#035596")
            self.canvas = FigureCanvasTkAgg(fig,master=self.page3)
            self.canvas.get_tk_widget().place(x=30,y=30)

        rel = Button(self.page3, image=self.reload, bg="#fff",bd=0,activebackground="#fff",command=refresh)
        rel.place(x=1185,y=5)


        nombres = ['Coding','Math logic','PSeInt','logic']
        colores = ['#035596','#FCBA40','#035596','#FCBA40']
        tamaño = [coding_score,math_score,pseint_score,logic_score]
        #tamaño = [0,math_score,5,6]
        fig, axs = plt.subplots(1,2,dpi=80, figsize=(14,6), sharey=True, facecolor='white')
        plt.title('Graphic per category',color='#035596',size=16,family="Arial")

        axs[0].bar(nombres,tamaño,color=colores)
        axs[1].plot(nombres,tamaño,color="#035596")
        #axs[1].plot(nombres,tamaño,color="orange")
        
        self.canvas = FigureCanvasTkAgg(fig,master=self.page3)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=30,y=30)
        
###############################################################PAGE FOUR###############################################################
        lista_cuadros = [self.foto_grup1, self.foto_grup2, self.foto_grup3]
        def adelante(num_imagen):
            global label_pre
            global btn_adelante
            global btn_atras

            self.label_pre.place_forget()
            self.label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#fff")

            btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
            btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
            if num_imagen == 2:
                btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",state=DISABLED)

            self.label_pre.place(x=50,y=1)
            btn_atras.place(x=50,y=250)
            btn_adelante.place(x=1230,y=250)

        def atras(num_imagen):
            global label_pre
            global btn_adelante
            global btn_atras

            self.label_pre.place_forget()
            self.label_pre = Label(frame1,image=lista_cuadros[num_imagen], bg="#fff")

            btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", command=lambda: atras(num_imagen - 1))
            btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(num_imagen + 1))
            if num_imagen == 0:
                btn_atras = Button(frame_central,image=self.privius, bg="white",bd=0,activebackground="white",state=DISABLED)

            self.label_pre.place(x=50,y=1)
            btn_atras.place(x=50,y=250)
            btn_adelante.place(x=1230,y=250)


        frame_central = Frame(self.page4, height= 540, width=1355, bg="white")
        frame_central.place(x=1,y=20)
        #back_labe = Label(frame_central, image=self.plant_info, height=454, width=972,bg="white")
        #back_labe.place(x=180, y=70)
        #barra_lab = Label(frame_central, image=self.barra_info,height=45, width=582,bg="white")
        #barra_lab.place(x=370,y=10)

        btn_atras = Button(frame_central,image=self.privius,bg="white",bd=0,activebackground="white", state=DISABLED)
        btn_atras.place(x=50,y=250)
        btn_adelante = Button(frame_central,image=self.next1, bg="white",bd=0,activebackground="white",command=lambda: adelante(1))
        btn_adelante.place(x=1230,y=250)

        frame1 = Frame(frame_central, height=400, width=880, bg="#fff")
        frame1.place(x=240,y=90)
        self.label_pre = Label(frame1,image=self.foto_grup1, bg="#fff")
        self.label_pre.place(x=50,y=1)
        #self.page1.place(x=5,y=130)
        #self.page2.place(x=5,y=130)
        #self.page3.place(x=5,y=130)
###############################################################PAGE FIVE###############################################################
        frame_cen = Frame(self.page5, height= 540, width=1355, bg="#fff")
        frame_cen.place(x=0,y=20)
        #---------botones--------

        Label(self.page5,text="Coding",fg='#035596',font=('Microsoft YaHei UI Light', 23, 'bold'),bg="#fff").place(x=615,y=70)

        def enter(e):
            selabel_btn1["image"] =self.selimage2
            selabel_btn1.image=self.selimage2
        def leave(e):
            selabel_btn1["image"] =self.selimage
            selabel_btn1.image=self.selimage
        selabel1 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn1 = Button(selabel1,image=self.selimage,bd=0,bg="#fff",command=self.test1)
        tex1 = Label(selabel1, text="Basic definitions", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex1.place(x=35,y=3)
        selabel_btn1.pack()
        selabel_btn1.bind("<Enter>",enter)
        selabel_btn1.bind("<Leave>",leave)
        selabel1.place(x=180,y=170)


        def enter(e):
            selabel_btn2["image"] =self.selimage2
            selabel_btn2.image=self.selimage2
        def leave(e):
            selabel_btn2["image"] =self.selimage
            selabel_btn2.image=self.selimage
        selabel2 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn2 = Button(selabel2,image=self.selimage,bd=0,bg="#fff")
        tex2 = Label(selabel2, text="Python basic", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex2.place(x=35,y=3)
        selabel_btn2.pack()
        selabel_btn2.bind("<Enter>",enter)
        selabel_btn2.bind("<Leave>",leave)
        selabel2.place(x=180,y=250)

        def enter(e):
            selabel_btn3["image"] =self.selimage2
            selabel_btn3.image=self.selimage2
        def leave(e):
            selabel_btn3["image"] =self.selimage
            selabel_btn3.image=self.selimage
        selabel3 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn3 = Button(selabel3,image=self.selimage,bd=0,bg="#fff")
        tex3 = Label(selabel3, text="Python medium", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex3.place(x=35,y=3)
        selabel_btn3.pack()
        selabel_btn3.bind("<Enter>",enter)
        selabel_btn3.bind("<Leave>",leave)
        selabel3.place(x=180,y=330)

        def enter(e):
            selabel_btn4["image"] =self.selimage2
            selabel_btn4.image=self.selimage2
        def leave(e):
            selabel_btn4["image"] =self.selimage
            selabel_btn4.image=self.selimage
        selabel4 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn4 = Button(selabel4,image=self.selimage,bd=0,bg="#fff")
        tex4 = Label(selabel4, text="JS basic", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex4.place(x=35,y=3)
        selabel_btn4.pack()
        selabel_btn4.bind("<Enter>",enter)
        selabel_btn4.bind("<Leave>",leave)
        selabel4.place(x=716,y=170)

        def enter(e):
            selabel_btn5["image"] =self.selimage2
            selabel_btn5.image=self.selimage2
        def leave(e):
            selabel_btn5["image"] =self.selimage
            selabel_btn5.image=self.selimage
        selabel5 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn5 = Button(selabel5,image=self.selimage,bd=0,bg="#fff")
        tex5 = Label(selabel5, text="JS medium", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex5.place(x=35,y=3)
        selabel_btn5.pack()
        selabel_btn5.bind("<Enter>",enter)
        selabel_btn5.bind("<Leave>",leave)
        selabel5.place(x=716,y=250)

        def enter(e):
            selabel_btn6["image"] =self.selimage2
            selabel_btn6.image=self.selimage2
        def leave(e):
            selabel_btn6["image"] =self.selimage
            selabel_btn6.image=self.selimage
        selabel6 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn6 = Button(selabel6,image=self.selimage,bd=0,bg="#fff")
        tex6 = Label(selabel6, text="PHP basic", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex6.place(x=35,y=3)
        selabel_btn6.pack()
        selabel_btn6.bind("<Enter>",enter)
        selabel_btn6.bind("<Leave>",leave)
        selabel6.place(x=716,y=330)

####################################################################################PAGE SIX#####################################################################################

        frame_cen = Frame(self.page6, height= 540, width=1355, bg="#fff")
        frame_cen.place(x=0,y=20)
        #---------botones--------

        Label(self.page6,text="Logic",fg='#035596',font=('Microsoft YaHei UI Light', 23, 'bold'),bg="#fff").place(x=630,y=70)

        def enter(e):
            selabel_btn7["image"] =self.selimage2
            selabel_btn7.image=self.selimage2
        def leave(e):
            selabel_btn7["image"] =self.selimage
            selabel_btn7.image=self.selimage
        selabel7 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn7 = Button(selabel7,image=self.selimage,bd=0,bg="#fff",command=self.test3)
        tex7 = Label(selabel7,text="Psicotechnic 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex7.place(x=35,y=3)
        selabel_btn7.pack()
        selabel_btn7.bind("<Enter>",enter)
        selabel_btn7.bind("<Leave>",leave)
        selabel7.place(x=180,y=170)


        def enter(e):
            selabel_btn8["image"] =self.selimage2
            selabel_btn8.image=self.selimage2
        def leave(e):
            selabel_btn8["image"] =self.selimage
            selabel_btn8.image=self.selimage
        selabel8 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn8 = Button(selabel8,image=self.selimage,bd=0,bg="#fff")
        tex8 = Label(selabel8, text="Psicotechnic 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex8.place(x=35,y=3)
        selabel_btn8.pack()
        selabel_btn8.bind("<Enter>",enter)
        selabel_btn8.bind("<Leave>",leave)
        selabel8.place(x=180,y=250)

        def enter(e):
            selabel_btn9["image"] =self.selimage2
            selabel_btn9.image=self.selimage2
        def leave(e):
            selabel_btn9["image"] =self.selimage
            selabel_btn9.image=self.selimage
        selabel9 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn9 = Button(selabel9,image=self.selimage,bd=0,bg="#fff")
        tex9 = Label(selabel9, text="Logic in code", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex9.place(x=35,y=3)
        selabel_btn9.pack()
        selabel_btn9.bind("<Enter>",enter)
        selabel_btn9.bind("<Leave>",leave)
        selabel9.place(x=180,y=330)

        def enter(e):
            selabel_btn10["image"] =self.selimage2
            selabel_btn10.image=self.selimage2
        def leave(e):
            selabel_btn10["image"] =self.selimage
            selabel_btn10.image=self.selimage
        selabel10 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn10 = Button(selabel10,image=self.selimage,bd=0,bg="#fff")
        tex10 = Label(selabel10, text="Lateral thinking", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex10.place(x=35,y=3)
        selabel_btn10.pack()
        selabel_btn10.bind("<Enter>",enter)
        selabel_btn10.bind("<Leave>",leave)
        selabel10.place(x=716,y=170)

        def enter(e):
            selabel_btn11["image"] =self.selimage2
            selabel_btn11.image=self.selimage2
        def leave(e):
            selabel_btn11["image"] =self.selimage
            selabel_btn11.image=self.selimage
        selabel11 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn11 = Button(selabel11,image=self.selimage,bd=0,bg="#fff")
        tex11 = Label(selabel11, text="Daily life 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex11.place(x=35,y=3)
        selabel_btn11.pack()
        selabel_btn11.bind("<Enter>",enter)
        selabel_btn11.bind("<Leave>",leave)
        selabel11.place(x=716,y=250)

        def enter(e):
            selabel_btn12["image"] =self.selimage2
            selabel_btn12.image=self.selimage2
        def leave(e):
            selabel_btn12["image"] =self.selimage
            selabel_btn12.image=self.selimage
        selabel12 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn12 = Button(selabel12,image=self.selimage,bd=0,bg="#fff")
        tex12 = Label(selabel12, text="Daily life 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex12.place(x=35,y=3)
        selabel_btn12.pack()
        selabel_btn12.bind("<Enter>",enter)
        selabel_btn12.bind("<Leave>",leave)
        selabel12.place(x=716,y=330)
####################################################################################PAGE SEVEN#####################################################################################
        frame_cen = Frame(self.page7, height= 540, width=1355, bg="#fff")
        frame_cen.place(x=0,y=20)
        #---------botones--------

        Label(self.page7,text="PseInt",fg='#035596',font=('Microsoft YaHei UI Light', 23, 'bold'),bg="#fff").place(x=630,y=70)

        def enter(e):
            selabel_btn13["image"] =self.selimage2
            selabel_btn13.image=self.selimage2
        def leave(e):
            selabel_btn13["image"] =self.selimage
            selabel_btn13.image=self.selimage
        selabel13 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn13 = Button(selabel13,image=self.selimage,bd=0,bg="#fff")
        tex13 = Label(selabel13, text="Basic definitions", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex13.place(x=35,y=3)
        selabel_btn13.pack()
        selabel_btn13.bind("<Enter>",enter)
        selabel_btn13.bind("<Leave>",leave)
        selabel13.place(x=180,y=170)


        def enter(e):
            selabel_btn14["image"] =self.selimage2
            selabel_btn14.image=self.selimage2
        def leave(e):
            selabel_btn14["image"] =self.selimage
            selabel_btn14.image=self.selimage
        selabel14 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn14 = Button(selabel14,image=self.selimage,bd=0,bg="#fff")
        tex14 = Label(selabel14, text="Conditionals 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex14.place(x=35,y=3)
        selabel_btn14.pack()
        selabel_btn14.bind("<Enter>",enter)
        selabel_btn14.bind("<Leave>",leave)
        selabel14.place(x=180,y=250)

        def enter(e):
            selabel_btn15["image"] =self.selimage2
            selabel_btn15.image=self.selimage2
        def leave(e):
            selabel_btn15["image"] =self.selimage
            selabel_btn15.image=self.selimage
        selabel15 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn15 = Button(selabel15,image=self.selimage,bd=0,bg="#fff")
        tex15 = Label(selabel15, text="Conditionals 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex15.place(x=35,y=3)
        selabel_btn15.pack()
        selabel_btn15.bind("<Enter>",enter)
        selabel_btn15.bind("<Leave>",leave)
        selabel15.place(x=180,y=330)

        def enter(e):
            selabel_btn16["image"] =self.selimage2
            selabel_btn16.image=self.selimage2
        def leave(e):
            selabel_btn16["image"] =self.selimage
            selabel_btn16.image=self.selimage
        selabel16 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn16 = Button(selabel16,image=self.selimage,bd=0,bg="#fff")
        tex16 = Label(selabel16, text="Loop 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex16.place(x=35,y=3)
        selabel_btn16.pack()
        selabel_btn16.bind("<Enter>",enter)
        selabel_btn16.bind("<Leave>",leave)
        selabel16.place(x=716,y=170)

        def enter(e):
            selabel_btn17["image"] =self.selimage2
            selabel_btn17.image=self.selimage2
        def leave(e):
            selabel_btn17["image"] =self.selimage
            selabel_btn17.image=self.selimage
        selabel17 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn17 = Button(selabel17,image=self.selimage,bd=0,bg="#fff")
        tex17 = Label(selabel17, text="Loop 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex17.place(x=35,y=3)
        selabel_btn17.pack()
        selabel_btn17.bind("<Enter>",enter)
        selabel_btn17.bind("<Leave>",leave)
        selabel17.place(x=716,y=250)

        def enter(e):
            selabel_btn18["image"] =self.selimage2
            selabel_btn18.image=self.selimage2
        def leave(e):
            selabel_btn18["image"] =self.selimage
            selabel_btn18.image=self.selimage
        selabel18 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn18 = Button(selabel18,image=self.selimage,bd=0,bg="#fff")
        tex18 = Label(selabel18, text="Translations", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex18.place(x=35,y=3)
        selabel_btn18.pack()
        selabel_btn18.bind("<Enter>",enter)
        selabel_btn18.bind("<Leave>",leave)
        selabel18.place(x=716,y=330)
####################################################################################PAGE EIGHT#####################################################################################
        frame_cen = Frame(self.page8, height= 540, width=1355, bg="#fff")
        frame_cen.place(x=0,y=20)
        #---------botones--------

        Label(self.page8,text="Math Logic",fg='#035596',font=('Microsoft YaHei UI Light', 23, 'bold'),bg="#fff").place(x=590,y=70)

        def enter(e):
            selabel_btn19["image"] =self.selimage2
            selabel_btn19.image=self.selimage2
        def leave(e):
            selabel_btn19["image"] =self.selimage
            selabel_btn19.image=self.selimage
        selabel19 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn19 = Button(selabel19,image=self.selimage,bd=0,bg="#fff",command=self.test2)
        tex19 = Label(selabel19, text="Fast thinking", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex19.place(x=35,y=3)
        selabel_btn19.pack()
        selabel_btn19.bind("<Enter>",enter)
        selabel_btn19.bind("<Leave>",leave)
        selabel19.place(x=180,y=170)


        def enter(e):
            selabel_btn20["image"] =self.selimage2
            selabel_btn20.image=self.selimage2
        def leave(e):
            selabel_btn20["image"] =self.selimage
            selabel_btn20.image=self.selimage
        selabel20 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn20 = Button(selabel20,image=self.selimage,bd=0,bg="#fff")
        tex20 = Label(selabel20, text="Daily life 1", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex20.place(x=35,y=3)
        selabel_btn20.pack()
        selabel_btn20.bind("<Enter>",enter)
        selabel_btn20.bind("<Leave>",leave)
        selabel20.place(x=180,y=250)

        def enter(e):
            selabel_btn21["image"] =self.selimage2
            selabel_btn21.image=self.selimage2
        def leave(e):
            selabel_btn21["image"] =self.selimage
            selabel_btn21.image=self.selimage
        selabel21 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn21 = Button(selabel21,image=self.selimage,bd=0,bg="#fff")
        tex21 = Label(selabel21, text="Daily life 2", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex21.place(x=35,y=3)
        selabel_btn21.pack()
        selabel_btn21.bind("<Enter>",enter)
        selabel_btn21.bind("<Leave>",leave)
        selabel21.place(x=180,y=330)

        def enter(e):
            selabel_btn22["image"] =self.selimage2
            selabel_btn22.image=self.selimage2
        def leave(e):
            selabel_btn22["image"] =self.selimage
            selabel_btn22.image=self.selimage
        selabel22 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn22 = Button(selabel22,image=self.selimage,bd=0,bg="#fff")
        tex22 = Label(selabel22, text="Pitagoras basic", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex22.place(x=35,y=3)
        selabel_btn22.pack()
        selabel_btn22.bind("<Enter>",enter)
        selabel_btn22.bind("<Leave>",leave)
        selabel22.place(x=716,y=170)

        def enter(e):
            selabel_btn23["image"] =self.selimage2
            selabel_btn23.image=self.selimage2
        def leave(e):
            selabel_btn23["image"] =self.selimage
            selabel_btn23.image=self.selimage
        selabel23 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn23 = Button(selabel23,image=self.selimage,bd=0,bg="#fff")
        tex23 = Label(selabel23, text="Pitagoras medium", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex23.place(x=35,y=3)
        selabel_btn23.pack()
        selabel_btn23.bind("<Enter>",enter)
        selabel_btn23.bind("<Leave>",leave)
        selabel23.place(x=716,y=250)

        def enter(e):
            selabel_btn24["image"] =self.selimage2
            selabel_btn24.image=self.selimage2
        def leave(e):
            selabel_btn24["image"] =self.selimage
            selabel_btn24.image=self.selimage
        selabel24 = Frame(frame_cen, height=50, width=456,bg= "#fff")
        selabel_btn24 = Button(selabel24,image=self.selimage,bd=0,bg="#fff")
        tex24 = Label(selabel24, text="Definitions trivia", fg="#fff",bg="#035596",font=('Microsoft YaHei UI Light', 23, 'bold'))
        tex24.place(x=35,y=3)
        selabel_btn24.pack()
        selabel_btn24.bind("<Enter>",enter)
        selabel_btn24.bind("<Leave>",leave)
        selabel24.place(x=716,y=330)



        self.notebook.pack(padx=5,pady=5)
        self.window.mainloop()




    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
    
    
      
if __name__ == '__main__':
    app = Fullscreen_Example()
