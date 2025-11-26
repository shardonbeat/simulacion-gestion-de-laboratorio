from customtkinter import *

class SolicitudesAcceso(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        self.labelFondo = CTkLabel(
			master=self,
			text="",
			fg_color="#2b2b39",
			bg_color="#A79D8A",
			corner_radius=15
		)
        self.labelFondo.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)

        self.labelContenido = CTkLabel(
			master=self,
			text="Solicitudes de Acceso",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.6, relheight=0.2,
			anchor=CENTER
		)
