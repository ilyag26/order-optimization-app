from src.util import *
from customtkinter import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
from src.util import get_data

def remove_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def log_page(root):
    #remove widget method
    remove_widgets(root)
    
    #create general frame
    frame=CTkFrame(master=root)
    frame.pack(fill=Y)
    bg_image = PhotoImage(file="static/img/form.png")
    CTkLabel(master=frame, image=bg_image).pack()

    #right panel content
    main_right = CTkFrame(master=frame, fg_color="#132138",width=600,height=600)
    pr_image = CTkImage(Image.open("static/img/login.png"),size = (150,155))
    profile_image = CTkLabel(main_right, text="",image=pr_image,fg_color="#132138",bg_color="#132138",corner_radius=10)
    entry_login = CTkEntry(master=main_right, placeholder_text="Логін", width=400, height=30, fg_color="#375174",font=("Arial Bold", 40))
    entry_pswd = CTkEntry(master=main_right, placeholder_text="Пароль", width=400, height=30, fg_color="#375174",font=("Arial Bold", 40))
    btn_login = CTkButton(master=main_right, text="Увійти", font=("Arial", 40),command=lambda: login_process(entry_login,entry_pswd,root))
    
    #left panel content
    main_left = CTkFrame(master=frame, fg_color="#132138",width=500,height=500)
    label_left = CTkLabel(main_left, text="Управління запасами\nта замовленнями для бізнесу",font=("Arial Bold", 30), text_color="#FFFFFF")
    label_left2 = CTkLabel(main_left, text="hello",font=("Arial Bold", 20), text_color="#FFFFFF")
    label = CTkLabel(main_right, text="Увійти в особистий кабінет",font=("Arial Bold", 40), text_color="#FFFFFF")

    #right panels pawn
    main_right.place(x=600,y=50)
    profile_image.place(x=213,y=10)
    label.place(x=50,y=170)
    entry_login.place(x=100,y=240)
    entry_pswd.place(x=100,y=310)
    btn_login.place(x=230,y=400)
    
    #left panel spawn
    main_left.place(x=50,y=70)
    label_left.place(x=33,y=20)
    label_left2.place(x=10,y=100)

def login_process(entry_login,entry_psw,root):
    if entry_login.get()=="" or entry_psw.get()=="":
        messagebox.showerror(title="ПОМИЛКА",message="ПОМИЛКА! Заповніть поля для вводу!")
    else:
        try:
            if entry_psw.get() == get_data(entry_login,2):
                login_name = entry_login.get()
                remove_widgets(root)
                page_general(root,login_name)
            else:
                messagebox.showerror(title="ПОМИЛКА",message="Помилка при вводі паролю!")
        except Exception as e:
            message = "ПОМИЛКА!Такого логіна не існує!"
            messagebox.showerror("ПОМИЛКА!",f"{e}")