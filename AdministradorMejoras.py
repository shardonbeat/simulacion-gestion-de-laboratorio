from customtkinter import *

class MejorasCierres(CTkFrame):
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
			text="Sistema de Gestión de Mejoras y Cierres",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.5, relheight=0.2,
			anchor=CENTER
		)

        # Botón para evaluar laboratorios
        self.botonEvaluar = CTkButton(
            master=self,
            text="Evaluar Laboratorios",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.evaluar_laboratorios
        )
        self.botonEvaluar.place(
            relx=0.35, rely=0.3,
            relwidth=0.3, relheight=0.07
        )

        # Área de resultados
        self.labelResultados = CTkLabel(
            master=self,
            text="Resultados de Evaluación:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelResultados.place(
            relx=0.1, rely=0.4,
            relwidth=0.3, relheight=0.05
        )

        self.textoResultados = CTkTextbox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.textoResultados.place(
            relx=0.1, rely=0.45,
            relwidth=0.8, relheight=0.3
        )

        # Botones de acción
        self.botonMejoras = CTkButton(
            master=self,
            text="Aplicar Mejoras",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#2d5e2d",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.aplicar_mejoras
        )
        self.botonMejoras.place(
            relx=0.25, rely=0.8,
            relwidth=0.2, relheight=0.07
        )

        self.botonCierre = CTkButton(
            master=self,
            text="Recomendar Cierre",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#8b2d2d",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.recomendar_cierre
        )
        self.botonCierre.place(
            relx=0.55, rely=0.8,
            relwidth=0.2, relheight=0.07
        )

        # Labels de mensajes
        self.mensaje_exito = CTkLabel(
            master=self,
            text="Acción aplicada correctamente",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.mensaje_error = CTkLabel(
            master=self,
            text="",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def evaluar_laboratorios(self):
        try:
            evaluaciones = self.main.bdd.evaluar_laboratorios()
            
            if not evaluaciones:
                self.textoResultados.delete("1.0", "end")
                self.textoResultados.insert("1.0", "No hay datos suficientes para evaluar laboratorios")
                return

            resultado_texto = "EVALUACIÓN DE LABORATORIOS\n"
            resultado_texto += "=" * 50 + "\n\n"
            
            for eval in evaluaciones:
                resultado_texto += f"Laboratorio: {eval['laboratorio']}\n"
                resultado_texto += f"Puntaje de Riesgo: {eval['puntaje_riesgo']}\n"
                resultado_texto += f"Recomendación: {eval['recomendacion']}\n"
                resultado_texto += f"Acción Requerida: {eval['accion_requerida']}\n"
                resultado_texto += "-" * 30 + "\n"

            self.textoResultados.delete("1.0", "end")
            self.textoResultados.insert("1.0", resultado_texto)
            
        except Exception as e:
            self.textoResultados.delete("1.0", "end")
            self.textoResultados.insert("1.0", f"Error en evaluación: {e}")

    def aplicar_mejoras(self):
        contenido = self.textoResultados.get("1.0", "end-1c")
        if "MEJORAS" in contenido.upper():
            self.mostrar_exito("Plan de mejoras aplicado y registrado")
        else:
            self.mostrar_error("No se detectaron laboratorios que requieran mejoras")

    def recomendar_cierre(self):
        contenido = self.textoResultados.get("1.0", "end-1c")
        if "CIERRE" in contenido.upper():
            self.mostrar_exito("Recomendación de cierre registrada")
        else:
            self.mostrar_error("No se detectaron laboratorios que requieran cierre")

    def mostrar_error(self, mensaje):
        self.mensaje_error.configure(text=mensaje)
        self.mensaje_error.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_exito.place_forget()

    def mostrar_exito(self, mensaje):
        self.mensaje_exito.configure(text=mensaje)
        self.mensaje_exito.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_error.place_forget()