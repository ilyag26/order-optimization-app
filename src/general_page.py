from customtkinter import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from src.counting import count
from src.login_page import log_page

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

    CTkButton(master=sidebar_frame, image=analytics_img, text="Панель", fg_color="#fff", font=("Arial Bold", 14), text_color="#132138", hover_color="#eee", anchor="w").pack(anchor="center", ipady=5, pady=(60, 0))

    person_img_data = Image.open("static/img/logout.png")
    person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, text="Вийти", fg_color="transparent", font=("Arial Bold", 14), hover_color="#3B8ED0", anchor="w",command=lambda: log_page(root,login_name)).pack(anchor="center", ipady=5, pady=(160, 0))

    #main canvas
    main_view = CTkFrame(master=root, fg_color="#fff",  width=1074, height=700, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Панель", font=("Arial Black", 25), text_color="#132138").pack(anchor="nw", side="left")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(36, 0))

    orders_metric = CTkFrame(master=metrics_frame, fg_color="#E3E3E3", width=1050, height=550)
    orders_metric.grid_propagate(0)
    orders_metric.pack(side="left")

    logitics_img_data = Image.open("static/img/logistics_icon.png")
    logistics_img = CTkImage(light_image=logitics_img_data, dark_image=logitics_img_data, size=(43, 43))

    CTkLabel(master=orders_metric, text="Введить входні данні:", text_color="#132138", font=("Arial Black", 15)).grid(row=0, column=0, sticky="sw",padx=(6,0))

    #first row
    CTkLabel(master=orders_metric, text="z - обсяг товару", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=2, column=0, sticky="w",padx=(6,0))
    entry_z = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_z.grid(row=3, column=0, ipady=10,padx=(5,0))

    CTkLabel(master=orders_metric, text="t - період", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=2, column=1, sticky="w", padx=(30,0))
    entry_t = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_t.grid(row=3, column=1, ipady=10, padx=(29,0))

    CTkLabel(master=orders_metric, text="K_t - фіксовані \nвитрати замовлення", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=2, column=2, sticky="w", padx=(55,0))
    entry_kt = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_kt.grid(row=3, column=2, ipady=10, padx=(54,0))

    #second row
    CTkLabel(master=orders_metric, text="c_t(z) - змінні витрати на продукцію ", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=7, column=0, sticky="w", padx=(6,0))
    entry_ctz = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_ctz.grid(row=8, column=0, ipady=10, padx=(5,0))

    CTkLabel(master=orders_metric, text="h_t - відсотків \nвід ціни товару", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=7, column=1, sticky="w",padx=(30,0))
    entry_ht = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_ht.grid(row=8, column=1, ipady=10,padx=(29,0))

    CTkLabel(master=orders_metric, text="It – запас в кінці періоду t", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=7, column=2, sticky="w", padx=(55,0))
    entry_it =  CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_it.grid(row=8, column=2, ipady=10, padx=(54,0))

    #third row
    CTkLabel(master=orders_metric, text="zt – обсяг замовлення у період t", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=10, column=0, sticky="w",padx=(6,0))
    entry_zt = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_zt.grid(row=11, column=0, ipady=10,padx=(5,0))

    CTkLabel(master=orders_metric, text="x(t) - об'єм виробленої\n продукції потреб у t", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=10, column=1, sticky="w", padx=(30,0))
    entry_xt = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_xt.grid(row=11, column=1, ipady=10, padx=(29,0))

    CTkLabel(master=orders_metric, text="y(t) - об'єм потреб потреб у  t", font=("Arial Bold", 17), text_color="#132138", justify="left").grid(row=10, column=2, sticky="w", padx=(55,0))
    entry_yt = CTkEntry(master=orders_metric, fg_color="#F0F0F0", border_width=0, width=150)
    entry_yt.grid(row=11, column=2, ipady=10, padx=(54,0))

    CTkButton(master=orders_metric, text="Розрахувати", width=300, font=("Arial Bold", 17), hover_color="#1B2F50", fg_color="#132138", text_color="#fff", command=lambda: count(entry_z.get(),entry_t.get(),entry_kt.get(),entry_ctz.get(),entry_ht.get(),entry_it.get(),entry_zt.get(),entry_xt.get(),entry_yt.get())).grid(row=20, column=0,padx=(10,0))