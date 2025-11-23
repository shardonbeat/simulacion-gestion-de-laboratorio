from customtkinter import *
from PIL import Image
<<<<<<< HEAD

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
        self.ventana.geometry("400x300")
        self.ventana.title("Laboratorio de investigación científica")
=======
from Frame_Registro import frame_registro
import os

class Pruebas(CTk):
    def __init__(self):
        super().__init__()
        self.ancho = 1280; self.alto = 720;
        screen_width = self.winfo_screenwidth()  
        screen_height = self.winfo_screenheight() 

        self.configure(fg_color="#1d1c1c")

        x = (screen_width/2) - (self.ancho/2)
        y = (screen_height/2) - (self.alto/2)

        self.geometry('%dx%d+%d+%d' % 
			(self.ancho, self.alto, x, y-50))
        
        self.resizable(False, False)

        self.title("Laboratorio de investigación científica")
>>>>>>> 6537aa8316375910b7f493e1a5f61b5e2f03b245

        icono = os.path.join(os.path.dirname(__file__), "Img", "Laboratorio.ico")
        icono_path = os.path.join(icono)
        self.ventana.iconbitmap(icono_path)

<<<<<<< HEAD
        ## Frames
        self.frameLogin = frameLogin(self.ventana, self)
        self.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
        self.frameMain = frameMain(self.ventana, self)

        self.frameRegister = frameRegister(self.ventana, self)
=======
        self.back = CTkFrame(self, width=500, height=600, fg_color="#E4D7D7")
        self.back.place(x=400, y=60)

        icon_path = os.path.join(os.path.dirname(__file__), "Img", "Acceso.png")
        Imagen = Image.open(icon_path)
        self.AccesoImage = CTkImage(light_image=Imagen, dark_image=Imagen, size=(200, 200))
        self.AccesoLabel = CTkLabel(self.back, image=self.AccesoImage, text="")
        self.AccesoLabel.pack(pady=20)
        self.AccesoLabel.place(x=150, y=50)
    
        self.entry = CTkEntry(self.back, width=200, placeholder_text="Cédula")
        self.entry.pack(pady=3)
        self.entry.place(x=150, y=300)

        self.entry_password = CTkEntry(self.back, width=200, placeholder_text="Contraseña", show="*")
        self.entry_password.pack(pady=3)
        self.entry_password.place(x=150, y=350)
        
        self.boton = CTkButton(self.back, text="Iniciar sesión", command=self.boton_IniciarSesion)
        self.boton.configure(fg_color="#625B66")
        self.boton._hover_color = "#7A7282"
        self.boton.pack(pady=20)
        self.boton.place(x=180, y=400)

        self.boton2 = CTkButton(self.back, text="Registrarse", command=self.boton_Registrarse)
        self.boton2.configure(fg_color="#625B66")
        self.boton2._hover_color = "#7A7282"
        self.boton2.pack(pady=20)
        self.boton2.place(x=180, y=450)
    
    def boton_IniciarSesion(self):
        Cedula = self.entry.get()
        Contraseña = self.entry_password.get()
        print(f"Cedula: {Cedula} | Contraseña: {Contraseña}")

    def boton_Registrarse(self):
        self.frame_registro = frame_registro(self)
>>>>>>> 6537aa8316375910b7f493e1a5f61b5e2f03b245

        self.frameAdmin = frameAdmin(self.ventana, self)
        
    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    App().iniciar()