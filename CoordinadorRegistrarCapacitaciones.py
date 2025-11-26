from customtkinter import *

class RegistrarCapacitaciones(CTkFrame):
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
			text="Registrar Capacitaciones De Usuarios",
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

        self.labelCapacitacion = CTkLabel(
            master=self,
            text="Tipo de capacitación:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelCapacitacion.place(
            relx=0.1, rely=0.3,
            relwidth=0.3, relheight=0.05
        )

        self.entryCapacitacion = CTkEntry(
            master=self,
            fg_color="#5e5e72",
			bg_color="#2b2b39",
            placeholder_text="Capacitación en manejo de solventes | Certificación en manejo de carcinógenos",
			font=("Times New Roman", 15),
			corner_radius=10
        )
        self.entryCapacitacion.place(
            relx=0.35, rely=0.3,
            relwidth=0.6, relheight=0.05
        )

        self.labelFecha = CTkLabel(
            master=self,
            text="Fecha De Vigencia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFecha.place(
            relx=0.048, rely=0.4,
            relwidth=0.4, relheight=0.05
        )

        self.entryFecha = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryFecha.place(
            relx=0.35, rely=0.4,
            relwidth=0.15, relheight=0.05
        )

        self.labelFechaCaducidad = CTkLabel(
            master=self,
            text="Fecha de Caducidad:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaCaducidad.place(
            relx=0.052, rely=0.5,
            relwidth=0.4, relheight=0.05
        )

        self.entryFechaCaducidad = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryFechaCaducidad.place(
            relx=0.35, rely=0.5,
            relwidth=0.15, relheight=0.05
        )

        self.botonRegistrar = CTkButton(
            master=self,
            text="Registrar Capacitación",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10
        )
        self.botonRegistrar.place(
            relx=0.35, rely=0.8,
            relwidth=0.3, relheight=0.07
        )