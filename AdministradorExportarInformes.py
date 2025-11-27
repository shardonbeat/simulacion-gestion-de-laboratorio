from customtkinter import *
from datetime import datetime

class ExportarInformes(CTkFrame):
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
			text="Exportación De Informes",
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

        # Campos para el informe
        self.labelFechaInicio = CTkLabel(
            master=self,
            text="Fecha Inicio:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaInicio.place(
            relx=0.1, rely=0.3,
            relwidth=0.2, relheight=0.05
        )

        inicio_mes = datetime.now().replace(day=1).strftime("%Y-%m-%d")
        self.entryFechaInicio = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.entryFechaInicio.place(
            relx=0.3, rely=0.3,
            relwidth=0.15, relheight=0.05
        )
        self.entryFechaInicio.insert(0, inicio_mes)

        self.labelFechaFin = CTkLabel(
            master=self,
            text="Fecha Fin:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaFin.place(
            relx=0.5, rely=0.3,
            relwidth=0.2, relheight=0.05
        )

        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        self.entryFechaFin = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.entryFechaFin.place(
            relx=0.7, rely=0.3,
            relwidth=0.15, relheight=0.05
        )
        self.entryFechaFin.insert(0, fecha_hoy)

        # Área de visualización del informe
        self.labelInforme = CTkLabel(
            master=self,
            text="Informe de Cumplimiento:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelInforme.place(
            relx=0.1, rely=0.4,
            relwidth=0.3, relheight=0.05
        )

        self.textoInforme = CTkTextbox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.textoInforme.place(
            relx=0.1, rely=0.45,
            relwidth=0.8, relheight=0.3
        )

        self.botonGenerar = CTkButton(
            master=self,
            text="Generar Informe",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.generar_informe
        )
        self.botonGenerar.place(
            relx=0.25, rely=0.8,
            relwidth=0.2, relheight=0.07
        )

        self.botonExportar = CTkButton(
            master=self,
            text="Exportar con Firma",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#3a3a4a",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.exportar_con_firma
        )
        self.botonExportar.place(
            relx=0.55, rely=0.8,
            relwidth=0.2, relheight=0.07
        )

        # Labels de mensajes
        self.mensaje_exito = CTkLabel(
            master=self,
            text="Informe exportado correctamente",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.mensaje_error = CTkLabel(
            master=self,
            text="",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def generar_informe(self):
        fecha_inicio = self.entryFechaInicio.get()
        fecha_fin = self.entryFechaFin.get()

        try:
            # Validar fechas
            datetime.strptime(fecha_inicio, "%Y-%m-%d")
            datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            self.mostrar_error("Formato de fecha inválido. Use AAAA-MM-DD")
            return

        try:
            informe = self.main.bdd.generar_informe_cumplimiento(fecha_inicio, fecha_fin)
            if informe:
                self.textoInforme.delete("1.0", "end")
                self.textoInforme.insert("1.0", informe)
                self.mensaje_error.place_forget()
            else:
                self.mostrar_error("Error al generar el informe")
        except Exception as e:
            self.mostrar_error(f"Error: {e}")

    def exportar_con_firma(self):
        contenido = self.textoInforme.get("1.0", "end-1c")
        if not contenido.strip():
            self.mostrar_error("Genere un informe primero")
            return

        try:
            # Generar nombre de archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"Informe_Cumplimiento_{timestamp}.txt"
            
            success = self.main.bdd.exportar_informe_archivo(contenido, nombre_archivo)
            if success:
                self.mostrar_exito(f"Informe exportado: {nombre_archivo}")
            else:
                self.mostrar_error("Error al exportar el informe")
        except Exception as e:
            self.mostrar_error(f"Error: {e}")

    def mostrar_error(self, mensaje):
        self.mensaje_error.configure(text=mensaje)
        self.mensaje_error.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_exito.place_forget()

    def mostrar_exito(self, mensaje):
        self.mensaje_exito.configure(text=mensaje)
        self.mensaje_exito.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.mensaje_error.place_forget()