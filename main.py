from customtkinter import *

from db import BDD

from frameLogin import frameLogin
from frameMain import frameMain
from frameRegister import frameRegister
from frameAdmin import frameAdmin
from FrameCoordinador import FrameCoordinador

set_default_color_theme("blue")

class App:
    def __init__(self):
        self.ventana = CTk()
        self.bdd = BDD()
        self.ventana.geometry("1280x720")
        self.ventana.resizable(False, False)
        self.ventana.title("Laboratorio de investigación científica")
        
        icono = "Img/Laboratorio.ico"
        self.ventana.iconbitmap(icono)
        self.ventana_actual = None
        self.usuario_actual = None

        self.frameLogin = frameLogin(self.ventana, self)
        self.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )

        self.frameMain = None
        self.frameRegister = None
        self.frameAdmin = None
        self.FrameCoordinador = None

        self.ventana_actual = self.frameLogin

    def mostrar_main(self, data=None):
        self.cerrar_ventanas()

        if data:
            self.usuario_actual = data
        
        if self.usuario_actual:
            self.frameLogin.place_forget()
            self.frameMain = frameMain(self.ventana, self)
            self.frameMain.place(
                relx=0, rely=0,
                relwidth=1, relheight=1
            )
            self.ventana_actual = self.frameMain

    def mostrar_register(self):
        self.cerrar_ventanas()
        self.frameLogin.place_forget()
        self.frameRegister = frameRegister(self.ventana, self)
        self.frameRegister.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
        self.ventana_actual = self.frameRegister

    def mostrar_coordinador(self):
        self.cerrar_ventanas()
        self.frameLogin.place_forget()
        self.FrameCoordinador = FrameCoordinador(self.ventana, self)
        self.FrameCoordinador.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
        self.ventana_actual = self.FrameCoordinador

    def mostrar_admin(self):
        self.cerrar_ventanas()
        self.frameLogin.place_forget()
        self.frameAdmin = frameAdmin(self.ventana, self)
        self.frameAdmin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
        self.ventana_actual = self.frameAdmin

    def mostrar_login(self):
        self.cerrar_ventanas()
        self.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
        self.ventana_actual = self.frameLogin

    def cerrar_ventanas(self):
        ventanas = [
            self.frameMain, 
            self.frameRegister,
            self.frameAdmin, 
            self.FrameCoordinador
        ]

        for ventana in ventanas:
            if ventana is not None:
                ventana.place_forget()

        self.ventana_actual = None

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    App().iniciar()