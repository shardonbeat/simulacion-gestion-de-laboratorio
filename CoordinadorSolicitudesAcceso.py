from customtkinter import *
from tkinter import ttk

class SolicitudesAcceso(CTkFrame):
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
			text="Solicitudes de Acceso",
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
		
		self.boton_cambiar_estado = CTkButton(
			master=self,
			text="Cambiar Estado",
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=10,
			command=lambda: self.actualizar_estado_solicitud()
		)
		self.boton_cambiar_estado.place(
			relx=0.5, rely=0.85,
			anchor=CENTER,
		)
		
		columnas = ("Usuario", "Fecha Solicitud", "Estado", "Accion")

		self.tablaSolicitudes = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes.heading("Usuario", text="Usuario")
		self.tablaSolicitudes.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes.heading("Estado", text="Estado")
		self.tablaSolicitudes.heading("Accion", text="Accion")
		self.tablaSolicitudes.place(
			relx=0.5, rely=0.55,
			relwidth=0.8, relheight=0.6,
			anchor=CENTER
		)
		self.cargar_solicitudes()

	def cargar_solicitudes(self):
		self.tablaSolicitudes.destroy()
		columnas = ("ID", "Usuario", "Fecha Solicitud", "Estado")
		self.tablaSolicitudes = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes.heading("ID", text="ID")
		self.tablaSolicitudes.heading("Usuario", text="Usuario")
		self.tablaSolicitudes.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes.heading("Estado", text="Estado")
		self.tablaSolicitudes.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.5, anchor="center")
		
		solicitudes = self.main.bdd.obtener_solicitudes_acceso()
		print(solicitudes)
		try:
			for solicitud in solicitudes:
				self.tablaSolicitudes.insert(
				"", "end",
				values=(solicitud['id_solicitud'], solicitud['username'], solicitud['fecha_solicitud'], solicitud['estado'])
			)
		except Exception:
			try:
				for solicitud in solicitudes:
					self.tablaSolicitudes.insert(
					"", "end",
					values=(solicitud[0], solicitud[1], solicitud[2], solicitud[3])
				)
			except Exception as e:
				print(f'Error al cargar solicitudes: {e}')
		
	def actualizar_estado_solicitud(self):
		solicitud = self.tablaSolicitudes.focus()
		datos_solicitud = self.tablaSolicitudes.item(solicitud)

		if not datos_solicitud['values']:
			print("No se ha seleccionado ninguna solicitud.")
			return
		
		id_solicitud = datos_solicitud['values'][0]
		estado_actual = datos_solicitud['values'][3]

		nuevo_estado = "Aprobada" if estado_actual == "Pendiente" else "Pendiente"
		self.main.bdd.actualizar_estado_solicitud(id_solicitud, nuevo_estado)
		self.cargar_solicitudes()
	