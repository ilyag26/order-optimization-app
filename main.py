from customtkinter import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import src.app.database_sqlite as database_sqlite
import src.login_page as login_page

if __name__ == "__main__":
    root = CTk()
    root.title("Diplom")
    root.geometry("1250x700+210+100")
    root.resizable(False,False)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    login_page.login(root)
    root.mainloop()