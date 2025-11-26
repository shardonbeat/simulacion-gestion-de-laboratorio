from customtkinter import *

class EmitirAlertas(CTkFrame):
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
			text="Alertas de Seguridad",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.4, relheight=0.2,
			anchor=CENTER
		)

        self.labelAlerta = CTkLabel(
            master=self,
            text="Tipo de Alerta:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelAlerta.place(
            relx=0.1, rely=0.3,
            relwidth=0.3, relheight=0.05
        )

        self.entryAlerta = CTkEntry(
            master=self,
            fg_color="#5e5e72",
			bg_color="#2b2b39",
            placeholder_text="Alerta de vencimiento | stock critico | riesgo de exposición",
			font=("Times New Roman", 15),
			corner_radius=10
        )
        self.entryAlerta.place(
            relx=0.35, rely=0.3,
            relwidth=0.6, relheight=0.05
        )

        self.labelMensaje = CTkLabel(
            master=self,
            text="Mensaje:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelMensaje.place(
            relx=0.072, rely=0.4,
            relwidth=0.4, relheight=0.05
        )

        self.entryMensaje = CTkTextbox(
            master=self,
            fg_color="#5e5e72",
			bg_color="#2b2b39",
			font = ("Times New Roman", 15),
			corner_radius=10
        )
        self.entryMensaje.place(
            relx=0.35, rely=0.4,
            relwidth=0.6, relheight=0.3
        )

        self.botonRegistrar = CTkButton(
            master=self,
            text="Emitir Alerta",
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