from customtkinter import *
from PIL import Image
import os


class Pruebas(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Laboratorio de investigación científica")

        icono = os.path.join(os.path.dirname(__file__), "Img", "Laboratorio.ico")
        icono_path = os.path.join(icono)
        self.iconbitmap(icono_path)

        self.configure(fg_color="#98939f")

        self.label = CTkLabel(self, text="Interfaz de Pruebas")
        self.label.pack(pady=20)

        self.boton = CTkButton(self, text="Presioname", command=self.boton_presionado)
        self.boton.pack(pady=20)
    
    def boton_presionado(self):
        print("Botón presionado!")

    def iniciar(self):
        self.mainloop()


if __name__ == "__main__":
    app = Pruebas()
    app.iniciar()