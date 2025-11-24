from customtkinter import *
import os
from db import BDD

from frameLogin import frameLogin
from frameMain import frameMain
from frameRegister import frameRegister
from frameAdmin import frameAdmin


set_default_color_theme("blue")

class App:
    def __init__(self):
        self.ventana = CTk()
        self.bdd = BDD()
        self.ventana.geometry("1280x720")
        self.ventana.resizable(False, False)
        self.ventana.title("Laboratorio de investigación científica")
        
        icono = os.path.join(os.path.dirname(__file__), "Img", "Laboratorio.ico")
        icono_path = os.path.join(icono)
        self.ventana.iconbitmap(icono_path)

        self.frameLogin = frameLogin(self.ventana, self)
        self.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )

        self.frameAdmin = frameAdmin(self.ventana, self)
        self.frameMain = frameMain(self.ventana, self)
        self.frameRegister = frameRegister(self.ventana, self)

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    App().iniciar()