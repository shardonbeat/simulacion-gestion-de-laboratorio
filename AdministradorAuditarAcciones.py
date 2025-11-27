from customtkinter import *
from datetime import datetime, timedelta

class AuditarAcciones(CTkFrame):
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
			text="Auditoría De Acciones",
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

        # Filtros de auditoría
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

        fecha_hace_7_dias = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
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
        self.entryFechaInicio.insert(0, fecha_hace_7_dias)

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

        self.labelUsuario = CTkLabel(
            master=self,
            text="Usuario:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelUsuario.place(
            relx=0.1, rely=0.4,
            relwidth=0.2, relheight=0.05
        )

        self.entryUsuario = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Opcional - dejar vacío para todos",
            font=("Times New Roman", 12),
            corner_radius=10
        )
        self.entryUsuario.place(
            relx=0.3, rely=0.4,
            relwidth=0.3, relheight=0.05
        )

        # Tabla de auditoría
        self.frameTabla = CTkScrollableFrame(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            scrollbar_fg_color="#5e5e72",
            height=200
        )
        self.frameTabla.place(
            relx=0.1, rely=0.5,
            relwidth=0.8, relheight=0.3
        )

        # Headers de la tabla
        headers = ["Fecha", "Usuario", "Acción", "Tabla", "Descripción"]
        for i, header in enumerate(headers):
            label = CTkLabel(
                self.frameTabla,
                text=header,
                text_color="#ffffff",
                fg_color="#3a3a4a",
                font=("Arial", 12, "bold"),
                width=120,
                height=30
            )
            label.grid(row=0, column=i, padx=2, pady=2, sticky="ew")

        self.botonAuditar = CTkButton(
            master=self,
            text="Auditar Acciones",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.auditar_acciones
        )
        self.botonAuditar.place(
            relx=0.35, rely=0.85,
            relwidth=0.3, relheight=0.07
        )

    def auditar_acciones(self):
        fecha_inicio = self.entryFechaInicio.get()
        fecha_fin = self.entryFechaFin.get()
        usuario = self.entryUsuario.get().strip() or None

        # Validar fechas
        try:
            if fecha_inicio:
                datetime.strptime(fecha_inicio, "%Y-%m-%d")
            if fecha_fin:
                datetime.strptime(fecha_fin, "%Y-%m-%d")
        except ValueError:
            return

        try:
            # Obtener datos de auditoría
            registros = self.main.bdd.obtener_log_auditoria(fecha_inicio, fecha_fin, usuario)
            
            # Limpiar tabla (excepto headers)
            for widget in self.frameTabla.winfo_children():
                if widget.grid_info()['row'] > 0:
                    widget.destroy()

            # Llenar tabla con datos
            for i, registro in enumerate(registros, 1):
                fecha = registro[5] if len(registro) > 5 else "N/A"
                usuario_reg = registro[1] if len(registro) > 1 else "N/A"
                accion = registro[2] if len(registro) > 2 else "N/A"
                tabla = registro[3] if len(registro) > 3 else "N/A"
                descripcion = registro[4] if len(registro) > 4 else "N/A"

                # Crear filas
                CTkLabel(self.frameTabla, text=fecha, 
                        text_color="#ffffff", font=("Arial", 10)).grid(row=i, column=0, padx=2, pady=1, sticky="w")
                CTkLabel(self.frameTabla, text=usuario_reg, 
                        text_color="#ffffff", font=("Arial", 10)).grid(row=i, column=1, padx=2, pady=1, sticky="w")
                CTkLabel(self.frameTabla, text=accion, 
                        text_color="#ffffff", font=("Arial", 10)).grid(row=i, column=2, padx=2, pady=1, sticky="w")
                CTkLabel(self.frameTabla, text=tabla, 
                        text_color="#ffffff", font=("Arial", 10)).grid(row=i, column=3, padx=2, pady=1, sticky="w")
                CTkLabel(self.frameTabla, text=descripcion, 
                        text_color="#ffffff", font=("Arial", 10)).grid(row=i, column=4, padx=2, pady=1, sticky="w")

        except Exception as e:
            print(f"Error en auditoría: {e}")