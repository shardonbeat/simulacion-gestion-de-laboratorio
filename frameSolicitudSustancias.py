from customtkinter import *

class solicitudSustancia(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        self.labelFondo = CTkLabel(
			master = self,
			text = "",
			fg_color = "#2b2b39",
			bg_color= "#A79D8A",
			corner_radius=15
		)
        self.labelFondo.place(
			relx=0, rely=0,
            relwidth=1, relheight=1
		)
        
        self.labelContenido = CTkLabel(
			master = self,
			text = "Solicitud de Sustancias Peligrosas",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 20, "bold"), corner_radius = 15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
            relwidth=0.6, relheight=0.2,
            anchor=CENTER
		)
        
        self.labelJustificacion = CTkLabel(
			master = self,
			text = "Justificación:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelJustificacion.place(
			relx=0.10, rely=0.35,
            relwidth=0.25, relheight=0.06,
		)
        
        self.Justificacion = CTkTextbox(master=self,
		 	fg_color="#5e5e72",
			bg_color="#2b2b39",
			font = ("Times New Roman", 15),
			corner_radius=10
		)
        self.Justificacion.place(
			relx=0.16, rely=0.45,
			relwidth=0.7, relheight=0.15,
		)
        
        self.enviarButton = CTkButton(
			master = self, text = "Enviar Solicitud",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
		)
        self.enviarButton.place(
			relx=0.4, rely=0.85,
			relwidth=0.2, relheight=0.1,
		)