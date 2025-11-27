from customtkinter import *
from datetime import datetime

class GenerarReportes(CTkFrame):
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
			text="Generación De Reportes de Cumplimiento",
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

        # Selector de tipo de reporte
        self.labelTipoReporte = CTkLabel(
            master=self,
            text="Tipo de Reporte:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelTipoReporte.place(
            relx=0.1, rely=0.25,
            relwidth=0.3, relheight=0.05
        )

        self.comboTipoReporte = CTkComboBox(
            master=self,
            values=[
                "ISO 45001 - Seguridad Ocupacional",
                "REACH - Sustancias Químicas", 
                "Normas Locales - Manejo de Residuos",
                "Reporte General"
            ],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            corner_radius=10,
            state="readonly"
        )
        self.comboTipoReporte.place(
            relx=0.4, rely=0.25,
            relwidth=0.5, relheight=0.05
        )
        self.comboTipoReporte.set("Seleccione tipo de reporte")

        # Campos de fecha
        self.labelMes = CTkLabel(
            master=self,
            text="Mes:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelMes.place(
            relx=0.1, rely=0.35,
            relwidth=0.3, relheight=0.05
        )

        self.comboMes = CTkComboBox(
            master=self,
            values=[f"{i:02d}" for i in range(1, 13)],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            corner_radius=10
        )
        self.comboMes.place(
            relx=0.4, rely=0.35,
            relwidth=0.2, relheight=0.05
        )
        self.comboMes.set(f"{datetime.now().month:02d}")

        self.labelAño = CTkLabel(
            master=self,
            text="Año:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelAño.place(
            relx=0.65, rely=0.35,
            relwidth=0.1, relheight=0.05
        )

        año_actual = datetime.now().year
        self.comboAño = CTkComboBox(
            master=self,
            values=[str(año_actual-1), str(año_actual), str(año_actual+1)],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            corner_radius=10
        )
        self.comboAño.place(
            relx=0.75, rely=0.35,
            relwidth=0.15, relheight=0.05
        )
        self.comboAño.set(str(año_actual))

        # Área de visualización del reporte
        self.labelReporte = CTkLabel(
            master=self,
            text="Reporte Generado:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelReporte.place(
            relx=0.1, rely=0.45,
            relwidth=0.3, relheight=0.05
        )

        self.textoReporte = CTkTextbox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Courier New", 11),
            corner_radius=10
        )
        self.textoReporte.place(
            relx=0.1, rely=0.5,
            relwidth=0.8, relheight=0.3
        )

        # Botones
        self.botonGenerar = CTkButton(
            master=self,
            text="Generar Reporte",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.generar_reporte
        )
        self.botonGenerar.place(
            relx=0.25, rely=0.85,
            relwidth=0.2, relheight=0.07
        )

        self.botonExportar = CTkButton(
            master=self,
            text="Exportar a Archivo",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#3a3a4a",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.exportar_reporte
        )
        self.botonExportar.place(
            relx=0.55, rely=0.85,
            relwidth=0.2, relheight=0.07
        )

        # Labels de mensajes
        self.mensaje_exito = CTkLabel(
            master=self,
            text="Reporte exportado correctamente",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.mensaje_error = CTkLabel(
            master=self,
            text="",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def generar_reporte(self):
        tipo_reporte = self.comboTipoReporte.get()
        mes = int(self.comboMes.get())
        año = int(self.comboAño.get())

        if not tipo_reporte or tipo_reporte == "Seleccione tipo de reporte":
            self.mostrar_error("Seleccione el tipo de reporte")
            return

        try:
            if tipo_reporte == "ISO 45001 - Seguridad Ocupacional":
                reporte = self.main.bdd.generar_reporte_iso45001(mes, año)
            elif tipo_reporte == "REACH - Sustancias Químicas":
                reporte = self.main.bdd.generar_reporte_reach(mes, año)
            elif tipo_reporte == "Normas Locales - Manejo de Residuos":
                reporte = self.main.bdd.generar_reporte_residuos(mes, año)
            else:
                reporte = self.main.bdd.generar_reporte_mensual(mes, año, "General")
            
            if reporte and not reporte.startswith("Error"):
                self.textoReporte.delete("1.0", "end")
                self.textoReporte.insert("1.0", reporte)
                self.mensaje_error.place_forget()
            else:
                self.mostrar_error("Error al generar el reporte")
        except Exception as e:
            self.mostrar_error(f"Error: {e}")

    def exportar_reporte(self):
        contenido = self.textoReporte.get("1.0", "end-1c")
        if not contenido.strip():
            self.mostrar_error("Genere un reporte primero")
            return

        try:
            tipo_reporte = self.comboTipoReporte.get()
            mes = self.comboMes.get()
            año = self.comboAño.get()
            
            # Crear nombre de archivo según el tipo de reporte
            if "ISO 45001" in tipo_reporte:
                nombre_archivo = f"Reporte_ISO45001_{mes}_{año}.txt"
            elif "REACH" in tipo_reporte:
                nombre_archivo = f"Reporte_REACH_{mes}_{año}.txt"
            elif "Residuos" in tipo_reporte:
                nombre_archivo = f"Reporte_Residuos_{mes}_{año}.txt"
            else:
                nombre_archivo = f"Reporte_General_{mes}_{año}.txt"
            
            success = self.main.bdd.exportar_informe_archivo(contenido, nombre_archivo)
            if success:
                self.mostrar_exito(f"✅ Reporte exportado: {nombre_archivo}")
            else:
                self.mostrar_error("❌ Error al exportar el reporte")
        except Exception as e:
            self.mostrar_error(f"❌ Error: {e}")

    def mostrar_error(self, mensaje):
        self.mensaje_error.configure(text=mensaje)
        self.mensaje_error.place(relx=0.5, rely=0.95, anchor=CENTER)
        self.mensaje_exito.place_forget()

    def mostrar_exito(self, mensaje):
        self.mensaje_exito.configure(text=mensaje)
        self.mensaje_exito.place(relx=0.5, rely=0.95, anchor=CENTER)
        self.mensaje_error.place_forget()