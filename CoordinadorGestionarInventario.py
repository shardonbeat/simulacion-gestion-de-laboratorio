from customtkinter import *

class GestionarInventario(CTkFrame):
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
			text="Gestionar Inventario De Sustancias Peligrosas",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.5, relheight=0.1,
			anchor=CENTER
		)

        self.labelFondo2 = CTkLabel(
            master=self,
            text="",
            fg_color="#72728b",
            bg_color="#2b2b39",
            corner_radius=15
        )
        self.labelFondo2.place( 
            relx=0.3, rely=0.2,
            relwidth=0.4, relheight=0.7
        )

        self.BotonAñadir= CTkButton(
            master=self,
            text="Añadir Sustancia",
            fg_color="#50505e",
            bg_color="#72728b",
            corner_radius=15
        )
        self.BotonAñadir.place( 
            relx=0.4, rely=0.25,
            relwidth=0.2, relheight=0.1
        )

        self.BotonModificar= CTkButton(
            master=self,
            text="Modificar Sustancia",
            fg_color="#50505e",
            bg_color="#72728b",
            corner_radius=15
        )
        self.BotonModificar.place(
            relx=0.4, rely=0.4,
            relwidth=0.2, relheight=0.1
        )

        self.BotonEliminar= CTkButton(
            master=self,
            text="Eliminar Sustancia",
            fg_color="#50505e",
            bg_color="#72728b",
            corner_radius=15
        )
        self.BotonEliminar.place(
            relx=0.4, rely=0.55,
            relwidth=0.2, relheight=0.1
        )