from customtkinter import *
from datetime import datetime

class DefinirPoliticas(CTkFrame):
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
			text="Definición De Políticas",
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

        # Campos para definir políticas
        self.labelTipoLab = CTkLabel(
            master=self,
            text="Tipo de Laboratorio:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelTipoLab.place(
            relx=0.1, rely=0.3,
            relwidth=0.3, relheight=0.05
        )

        self.comboTipoLab = CTkComboBox(
            master=self,
            values=["Químico", "Biológico", "Físico", "Investigación", "Docencia"],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            corner_radius=10
        )
        self.comboTipoLab.place(
            relx=0.4, rely=0.3,
            relwidth=0.5, relheight=0.05
        )

        self.labelNivelRiesgo = CTkLabel(
            master=self,
            text="Nivel de Riesgo:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelNivelRiesgo.place(
            relx=0.1, rely=0.4,
            relwidth=0.3, relheight=0.05
        )

        self.comboNivelRiesgo = CTkComboBox(
            master=self,
            values=["1 - Bajo", "2 - Medio", "3 - Alto", "4 - Muy Alto"],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            corner_radius=10
        )
        self.comboNivelRiesgo.place(
            relx=0.4, rely=0.4,
            relwidth=0.5, relheight=0.05
        )

        self.labelPolitica = CTkLabel(
            master=self,
            text="Política:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelPolitica.place(
            relx=0.1, rely=0.5,
            relwidth=0.3, relheight=0.05
        )

        self.entryPolitica = CTkTextbox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.entryPolitica.place(
            relx=0.4, rely=0.5,
            relwidth=0.5, relheight=0.2
        )

        self.botonRegistrar = CTkButton(
            master=self,
            text="Definir Política",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.definir_politica
        )
        self.botonRegistrar.place(
            relx=0.35, rely=0.8,
            relwidth=0.3, relheight=0.07
        )

        # Labels de mensajes
        self.mensaje_exito = CTkLabel(
            master=self,
            text="Política definida correctamente",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.mensaje_error = CTkLabel(
            master=self,
            text="",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def definir_politica(self):
        tipo_lab = self.comboTipoLab.get()
        nivel_riesgo = self.comboNivelRiesgo.get()
        politica_text = self.entryPolitica.get("1.0", "end-1c").strip()

        if not all([tipo_lab, nivel_riesgo, politica_text]):
            self.mostrar_error("Complete todos los campos")
            return

        try:
            creador = self.main.usuario_actual.get('username', 'Admin')
            success = self.main.bdd.guardar_politica(tipo_lab, nivel_riesgo, politica_text, creador)
            
            if success:
                self.mostrar_exito()
                self.limpiar_campos()
            else:
                self.mostrar_error("Error al guardar la política")
        except Exception as e:
            self.mostrar_error(f"Error: {e}")

    def mostrar_error(self, mensaje):
        self.mensaje_error.configure(text=mensaje)
        self.mensaje_error.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_exito.place_forget()

    def mostrar_exito(self):
        self.mensaje_exito.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_error.place_forget()

    def limpiar_campos(self):
        self.comboTipoLab.set("")
        self.comboNivelRiesgo.set("")
        self.entryPolitica.delete("1.0", "end")