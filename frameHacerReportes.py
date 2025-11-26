from datetime import datetime
from customtkinter import *

class HacerReportes(CTkFrame):
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
			text = "Reportes de incidentes",
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

        self.labelNombre = CTkLabel(
			master = self,
			text = "Nombre del incidente:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelNombre.place(
			relx=0.285, rely=0.2,
            relwidth=0.4, relheight=0.06,
		)

        self.Nombre = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font = ("Times New Roman", 15),
            corner_radius=10
        )
        self.Nombre.place(
			relx=0.4, rely=0.25,
            relwidth=0.2, relheight=0.06,
		)

        self.labelTipo = CTkLabel(
			master = self,
			text = "Tipo de incidente:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelTipo.place(
			relx=0.27, rely=0.35,
            relwidth=0.4, relheight=0.06,
		)

        self.Tipo = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font = ("Times New Roman", 15),
            corner_radius=10
        )
        self.Tipo.place(
			relx=0.4, rely=0.4,
            relwidth=0.2, relheight=0.06,
		)

        self.labelDescripcion = CTkLabel(
			master = self,
			text = "Descripción del incidente:",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15
		)
        self.labelDescripcion.place(
			relx=0.13, rely=0.5,
            relwidth=0.25, relheight=0.06,
		)
        
        self.Descripcion = CTkTextbox(master=self,
		 	fg_color="#5e5e72",
			bg_color="#2b2b39",
			font = ("Times New Roman", 15),
			corner_radius=10
		)
        self.Descripcion.place(
			relx=0.16, rely=0.55,
			relwidth=0.7, relheight=0.15,
		)
        
        self.enviarButton = CTkButton(
			master = self, text = "Enviar Reporte",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
            command= self.hacer_reporte
		)
        self.enviarButton.place(
			relx=0.4, rely=0.80,
			relwidth=0.2, relheight=0.1,
		)
        
        self.mensaje_exito_label = CTkLabel(
			master=self,
			text="Reporte enviado exitosamente.",
			text_color="#00ff00",
			font=("Times New Roman", 12, "bold"),
		)
        
    def hacer_reporte(self):
        self.limpiar_campos()
        try:
            titulo = self.Nombre.get()
            tipo = self.Tipo.get()
            descripcion = self.Descripcion.get("1.0", "end-1c")
            fecha = datetime.now().date()
            autor = self.main.usuario_actual['username']
            
            self.main.bdd.guardar_reporte_incidente(
				titulo, tipo, descripcion, fecha, autor
			)
            self.mensaje_exito_label.place(
				relx=0.4, rely=0.93,
			)
            print("Reporte enviado exitosamente.")
        except Exception as e:
            print(f'Error al enviar el reporte: {e}')
            
    def limpiar_campos(self):
        self.Nombre.delete(0, 'end')
        self.Tipo.delete(0, 'end')
        self.Descripcion.delete("1.0", "end")