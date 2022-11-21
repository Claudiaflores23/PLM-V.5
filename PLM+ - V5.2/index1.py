from ast import And 
from asyncio.proactor_events import _ProactorBasePipeTransport
from io import open_code
from PIL import ImageTk, Image
import pymysql
from tkinter import *
from tkinter import messagebox
from setuptools import Command
import util.generic as utl
from form_master import Fullscreen_Example
from loadscreen import load
class log_in:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry('925x500+300+200')
        self.root.iconbitmap("images/iconi.ico")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        def signin():
            bd1 = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="bd"
                )
            
            fcursor = bd1.cursor()
            fcursor.execute("SELECT password FROM login WHERE user='"+self.user.get()+"' and password='"+self.code.get()+"'")

            if fcursor.fetchall():
                #load()
                self.root.destroy()
                load()
            else:
                messagebox.showerror(title="Something failed", message="User or password are incorrect")
            bd1.close()

        frame_iz = Frame(bd = 0, width=475, relief=SOLID, padx=10, pady=10, bg = '#FCBA40')
        frame_iz.pack(side="right", expand=NO, fill=BOTH)
        '''frame_logo = Frame(bd=0, width=300, relief=SOLID, padx=10, pady=10, bg= 'red')
        frame_logo.pack(side="left", expand=NO,fill=BOTH)'''
        self.img = utl.leer_imagen("images/plm_logo.png", (355,200))
        Label(self.root, image=self.img, bg='white').place(x=50, y=150)

        frame=Frame(self.root, width=350, height=350, bg="#FCBA40")
        frame.place(x=480, y=70)

        heading=Label(frame, text='Sign in', fg='#035596', bg='#FCBA40', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=120, y=20)

        #-----------------------
        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            name = self.user.get()
            if name =="":
                self.user.insert(0,'Username')

        self.user = Entry(frame, width=25, fg='black', border = 0, bg="#FCBA40", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg='#035596').place(x=25, y=107)

        #-------------
        def on_enter(e):
            self.code.delete(0, 'end')
            self.code.config(show="*")

        def on_leave(e):
            name =self.code.get()
            if name == "":
                self.code.config(show="")
                self.code.insert(0,'Password')
        self.code = Entry(frame, width=25, fg='black', border = 0, bg="#FCBA40", font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        #code.config(show="*")
        self.code.bind("<FocusIn>", on_enter)
        self.code.bind("<FocusOut>", on_leave)


        Frame(frame, width=295, height=2, bg='#035596').place(x=25, y=177)

        #-----------------------------------------


        Button(frame, width=39, pady=7, text='Log in', bg="#035596", activebackground="#CFF7FF", cursor= 'hand2', fg='white', border=0, command=signin).place(x=35, y =204)
        label =Label(frame, text="Don´t have an account?", fg='black', bg="#FCBA40", font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)

        def signup():
            self.root.destroy()
            

        sign_up= Button(frame, width=6, text='Sign up', border=0, bg='#FCBA40', cursor='hand2', fg="#005697", command=signup)
        sign_up.place(x=215, y= 270)
        #---------------------------------------

        def show():
            hide_button = Button(frame, image=hide_photo, bg='#FCBA40', activebackground='#FCBA40', cursor='hand2', bd=0, command=hide)
            hide_button.place(x=298, y=158)
            self.code.config(show='')
        def hide():
            show_button = Button(frame, image=photo, bg='#FCBA40', activebackground='#FCBA40', cursor='hand2', bd=0, command=show)
            show_button.place(x=298, y=158)
            self.code.config(show='*')
        photo= utl.leer_imagen('images/show.png', (16,16))
        #photo = ImageTk.PhotoImage(show_image)
        show_button = Button(frame, image=photo, bg='#FCBA40', activebackground='#FCBA40', cursor='hand2', bd=0, command=show)
        show_button.place(x=298, y=158)

        hide_photo= utl.leer_imagen('images/esconder.png', (16,16))
        #photo = ImageTk.PhotoImage(show_image)


        self.root.mainloop()

#log_in()