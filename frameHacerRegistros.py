from customtkinter import *

class HacerRegistros(CTkFrame):
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
			text = "Hacer Registros de Sustancias Peligrosas",
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

        self.labelSustancias = CTkLabel(
			master = self,
			text = "Ingresar sustancias separadas por comas:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelSustancias.place(
			relx=0.12, rely=0.2,
            relwidth=0.4, relheight=0.06,
		)

        self.Sustancias = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font = ("Times New Roman", 15),
            corner_radius=10
        )
        self.Sustancias.place(
			relx=0.16, rely=0.25,
            relwidth=0.5, relheight=0.06,
		)

        self.labelCantidad = CTkLabel(
			master = self,
			text = "Ingresar cantidades separadas por comas:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelCantidad.place(
			relx=0.12, rely=0.35,
            relwidth=0.4, relheight=0.06,
		)

        self.Cantidades = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font = ("Times New Roman", 15),
            corner_radius=10
        )
        self.Cantidades.place(
			relx=0.16, rely=0.4,
            relwidth=0.5, relheight=0.06,
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
			relx=0.085, rely=0.5,
            relwidth=0.25, relheight=0.06,
		)
        
        self.Justificacion = CTkTextbox(master=self,
		 	fg_color="#5e5e72",
			bg_color="#2b2b39",
			font = ("Times New Roman", 15),
			corner_radius=10
		)
        self.Justificacion.place(
			relx=0.16, rely=0.55,
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