from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
from PIL import Image, ImageTk
from src.app import database_sqlite
from src.login_page import log_page
from src.util import *
from src.util import remove_widgets

if __name__ == "__main__":
    root = CTk()
    root.title("Diplom")
    root.geometry("1250x700+210+100")
    root.resizable(False,False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    set_appearance_mode("light")
    log_page(root)
    root.mainloop()