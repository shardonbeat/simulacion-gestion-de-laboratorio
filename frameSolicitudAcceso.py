from customtkinter import *

from datetime import datetime

class solicitudAcceso(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )
        self.nivel = None

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
			text = "Solicitud de Acceso al Laboratorio",
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
        
        self.nivel2Button = CTkButton(
			master = self, text = "Acceso al Nivel 2",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
            command = lambda: self.seleccion_nivel(2)
		)
        self.nivel2Button.place(
			relx=0.20, rely=0.20,
            relwidth=0.22, relheight=0.12,
		)
        
        self.nivel3Button = CTkButton(
			master = self, text = "Acceso al Nivel 3",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
            command = lambda: self.seleccion_nivel(3)
		)
        self.nivel3Button.place(
			relx=0.60, rely=0.20,
            relwidth=0.22, relheight=0.12,
		)
        self.labelMotivo = CTkLabel(
			master = self,
			text = "Motivo de la solicitud:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelMotivo.place(
			relx=0.12, rely=0.35,
            relwidth=0.25, relheight=0.06,
		)
        
        self.Motivo = CTkTextbox(
            master=self,
		 	fg_color="#5e5e72",
			bg_color="#2b2b39",
			font = ("Times New Roman", 15),
			corner_radius=10
		)
        self.Motivo.place(
			relx=0.16, rely=0.40,
			relwidth=0.7, relheight=0.3,
		)
        
        self.enviarButton = CTkButton(
			master = self, text = "Enviar Solicitud",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
            command = self.enviar_solicitud
		)
        self.enviarButton.place(
			relx=0.4, rely=0.85,
			relwidth=0.2, relheight=0.1,
		)

    def seleccion_nivel(self, nivel):
        self.nivel = nivel

    def enviar_solicitud(self):
        nivel = self.nivel
        motivo = self.Motivo.get("1.0", "end-1c")
        id_usuario = self.main.frameMain.id
        fecha_solicitud = datetime.now().date()
        print(f"Solicitud enviada por usuario de id {id_usuario} para nivel {nivel} con motivo: {motivo}")

        self.main.bdd.crear_solicitud_acceso(
            id_usuario, nivel, motivo, fecha_solicitud, "Pendiente"
        )