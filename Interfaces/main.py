from customtkinter import *
from PIL import Image
import os


class Pruebas(CTk):
    def __init__(self):
        super().__init__()
        self.ancho = 1280; self.alto = 720;
        screen_width = self.winfo_screenwidth()  
        screen_height = self.winfo_screenheight() 

        self.configure(fg_color="#3f3941")

        x = (screen_width/2) - (self.ancho/2)
        y = (screen_height/2) - (self.alto/2)

        self.geometry('%dx%d+%d+%d' % 
			(self.ancho, self.alto, x, y-50))
        
        self.resizable(False, False)

        self.title("Laboratorio de investigación científica")

        icono = os.path.join(os.path.dirname(__file__), "Img", "Laboratorio.ico")
        icono_path = os.path.join(icono)
        self.iconbitmap(icono_path)

        self.back = CTkFrame(self, width=500, height=600)
        self.back.place(x=400, y=60)

        icon_path = os.path.join(os.path.dirname(__file__), "Img", "Acceso.png")
        Imagen = Image.open(icon_path)
        self.AccesoImage = CTkImage(light_image=Imagen, dark_image=Imagen, size=(200, 200))
        self.AccesoLabel = CTkLabel(self.back, image=self.AccesoImage, text="")
        self.AccesoLabel.pack(pady=20)
        self.AccesoLabel.place(x=150, y=50)
    
        self.entry = CTkEntry(self.back, width=200, placeholder_text="Usuario")
        self.entry.pack(pady=3)
        self.entry.place(x=150, y=300)

        self.entry_password = CTkEntry(self.back, width=200, placeholder_text="Contraseña", show="*")
        self.entry_password.pack(pady=3)
        self.entry_password.place(x=150, y=350)

        self.boton = CTkButton(self.back, text="Iniciar sesión", command=self.boton_IniciarSesion)
        self.boton.configure(fg_color="#99949C")
        self.boton.pack(pady=20)
        self.boton.place(x=180, y=400)

        self.boton2 = CTkButton(self.back, text="Registrarse", command=self.boton_Registrarse)
        self.boton2.pack(pady=20)
        self.boton2.place(x=180, y=450)
    
    def boton_IniciarSesion(self):
        pass

    def boton_Registrarse(self):
        pass

    def iniciar(self):
        self.mainloop()


if __name__ == "__main__":
    app = Pruebas()
    app.iniciar()