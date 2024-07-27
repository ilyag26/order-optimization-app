from customtkinter import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from src.counting import count
from src.util import get_data

def remove_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def page_general(root,login_name):
    remove_widgets(root)
    sidebar_frame = CTkFrame(master=root, fg_color="#132138",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img_data = Image.open("static/img/logo.png")
    logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

    CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

    analytics_img_data = Image.open("static/img/analytics_icon_active.png")
    analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)

    CTkButton(master=sidebar_frame, image=analytics_img, text="Panel", fg_color="#fff", font=("Arial Bold", 14), text_color="#132138", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    person_img_data = Image.open("static/img/logout.png")
    person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, text="Exit", fg_color="transparent", font=("Arial Bold", 14), hover_color="#3B8ED0", anchor="w",command=lambda: log_page(root)).pack(anchor="center", ipady=5, pady=(160, 0))

    #main canvas
    main_view = CTkFrame(master=root, fg_color="#fff",  width=1074, height=700, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Panel", font=("Arial Black", 25), text_color="#132138").pack(anchor="nw", side="left")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame, fg_color="#E3E3E3", width=1050, height=550)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    logitics_img_data = Image.open("static/img/logistics_icon.png")
    logistics_img = CTkImage(light_image=logitics_img_data, dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, text="Enter the input data:", text_color="#132138", font=("Arial Black", 15)).grid(row=0, column=0, sticky="sw",padx=(6,0))

    #first row
    CTkLabel(master=orders_metric, text="Fixed order costs for each period(Values are entered separated by commas for the period - 4)", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=2, column=0, sticky="w",padx=(6,0))
    entry_k = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_k.grid(row=3, column=0, ipady=10,padx=(5,0))

    #second row
    CTkLabel(master=orders_metric, text="Variable product costs for each period(Values are entered separated by commas for the period - 4)", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=7, column=0, sticky="w", padx=(6,0))
    entry_c = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_c.grid(row=8, column=0, ipady=10, padx=(5,0))

    #third row
    CTkLabel(master=orders_metric, text="Storage costs for each period in %.(Values are entered separated by commas for the period - 4)", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=10, column=0, sticky="w",padx=(6,0))
    entry_h = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_h.grid(row=11, column=0, ipady=10,padx=(5,0))

    #fourth row
    CTkLabel(master=orders_metric, text="Demand for each period in boxes(Values are entered separated by commas for the period - 4)", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=14, column=0, sticky="w",padx=(6,0))
    entry_d = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_d.grid(row=15, column=0, ipady=10,padx=(5,0))

    #fourth row
    CTkLabel(master=orders_metric, text="The lack of goods in %(Values are entered separated by commas for the period - 4)", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=18, column=0, sticky="w",padx=(6,0))
    entry_s = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_s.grid(row=19, column=0, ipady=10,padx=(5,0))

    CTkButton(master=orders_metric, text="Calculate", width=300, font=("Arial Bold", 17), hover_color="#1B2F50", fg_color="#132138", text_color="#fff", command=lambda: count(entry_k.get(),entry_c.get(),entry_h.get(),entry_d.get(),entry_s.get())).grid(row=20, column=0,padx=(10,0))

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
    entry_login = CTkEntry(master=main_right, placeholder_text="Login", width=400, height=30, fg_color="#375174",font=("Arial Bold", 40))
    entry_pswd = CTkEntry(master=main_right, placeholder_text="Password", width=400, height=30, fg_color="#375174",font=("Arial Bold", 40))
    btn_login = CTkButton(master=main_right, text="Увійти", font=("Arial", 40),command=lambda: login_process(entry_login,entry_pswd,root))
    
    #left panel content
    main_left = CTkFrame(master=frame, fg_color="#132138",width=500,height=500)
    label_left = CTkLabel(main_left, text="Optimization of order volume",font=("Arial Bold", 28), text_color="#FFFFFF")
    label_left2 = CTkLabel(main_left, text="",font=("Arial Bold", 20), text_color="#FFFFFF")
    label = CTkLabel(main_right, text="Login",font=("Arial Bold", 40), text_color="#FFFFFF")

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
        messagebox.showerror(title="ERROR",message="ERROR! Fill in the input fields!")
    else:
        try:
            if entry_psw.get() == get_data(entry_login,2):
                login_name = entry_login.get()
                remove_widgets(root)
                page_general(root,login_name)
            else:
                messagebox.showerror(title="ERROR",message="Error entering password!")
        except Exception as e:
            message = "ERROR! This login does not exist!"
            messagebox.showerror("ERROR!",f"{e}")