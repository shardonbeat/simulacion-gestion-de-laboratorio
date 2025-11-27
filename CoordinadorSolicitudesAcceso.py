from customtkinter import *
from tkinter import ttk

from PIL import Image

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

		self.texto_exito = CTkLabel(
			master=self,
			text="Estado actualizado con éxito",
			text_color="#00FF00",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=15
		)

		self.texto_error = CTkLabel(
			master=self,
			text="",
			text_color="#FF0000",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=15
		)
		
		columnas = ("ID", "Usuario", "Fecha Solicitud", "Estado", "Accion")

		self.tablaSolicitudes_acceso = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes_acceso.heading("Usuario", text="Usuario")
		self.tablaSolicitudes_acceso.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes_acceso.heading("Estado", text="Estado")
		self.tablaSolicitudes_acceso.heading("Accion", text="Accion")
		self.tablaSolicitudes_acceso.column("Accion", width=100, anchor=CENTER)
		self.tablaSolicitudes_acceso.place(
			relx=0.5, rely=0.55,
			relwidth=1, relheight=0.6,
			anchor=CENTER
		)
		self.cargar_solicitudes()

	def cargar_solicitudes(self):
		self.tablaSolicitudes_acceso.destroy()
		columnas = ("ID", "Usuario", "Nivel Solicitado", "Descripción", "Fecha Solicitud", "Capacitacion", "Estado")
		self.tablaSolicitudes_acceso = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes_acceso.heading("ID", text="ID")
		self.tablaSolicitudes_acceso.heading("Usuario", text="Usuario")
		self.tablaSolicitudes_acceso.heading("Nivel Solicitado", text="Nivel Solicitado")
		self.tablaSolicitudes_acceso.heading("Descripción", text="Descripción")
		self.tablaSolicitudes_acceso.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes_acceso.heading("Capacitacion", text="Capacitacion")
		self.tablaSolicitudes_acceso.heading("Estado", text="Estado")
		self.tablaSolicitudes_acceso.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.5, anchor="center")
		
		solicitudes = self.main.bdd.obtener_solicitudes_acceso()
		print(solicitudes)

		# Validate response: handle None, 0 or non-iterable results
		if not solicitudes:
			self.texto_error.configure(
				text="No hay solicitudes para mostrar."
			)
			self.texto_error.place(
				relx=0.5, rely=0.75,
				anchor=CENTER
			)
			return

		try:
			for solicitud in solicitudes:
				# Support both dict-like rows and sequence (tuple/list) rows
				if isinstance(solicitud, dict):
					id_val = solicitud.get('id_solicitud_a') or solicitud.get('id_solicitud') or solicitud.get('id')
					user = solicitud.get('username') or solicitud.get('user') or ""
					nivel = solicitud.get('nivel_solicitud') or solicitud.get('nivel') or ""
					motivo = solicitud.get('motivo') or solicitud.get('descripcion') or ""
					fecha = solicitud.get('fecha_solicitud') or solicitud.get('fecha') or ""
					capacitacion = solicitud.get('capacitacion') or ""
					estado = solicitud.get('estado') or ""
				else:
					# assume sequence-like
					try:
						id_val = solicitud[0]
						user = solicitud[1]
						nivel = solicitud[2]
						motivo = solicitud[3]
						fecha = solicitud[4]
						capacitacion = solicitud[5]
						estado = solicitud[6]
					except Exception as e:
						# If a single row doesn't match expected shape, skip it and log
						print(f"Fila de solicitud con formato inesperado, se omite: {e} -> {solicitud}")
						continue

				self.tablaSolicitudes_acceso.insert(
					"", "end",
					values=(id_val, user, nivel, motivo, fecha, capacitacion, estado)
				)
		except Exception as e:
			# Fallback: show clear error message
			self.texto_error.configure(
				text=f"Error al cargar solicitudes: {e}"
			)
			self.texto_error.place(
				relx=0.5, rely=0.75,
				anchor=CENTER
			)
		
	def actualizar_estado_solicitud(self):
		solicitud = self.tablaSolicitudes_acceso.focus()
		datos_solicitud = self.tablaSolicitudes_acceso.item(solicitud)

		if not datos_solicitud['values']:
			print("No se ha seleccionado ninguna solicitud.")
			return
		
		id_solicitud = datos_solicitud['values'][0]
		# Guardar en variable segura (evitar IndexError si cambia la estructura)
		estado_actual = datos_solicitud['values'][6] if len(datos_solicitud['values']) > 6 else None

		if estado_actual is None:
			# si no hay estado, evitar cambiarlo y notificar
			self.texto_error.configure(
				text="No se pudo leer el estado de la solicitud seleccionada."
			)
			self.texto_error.place(
				relx=0.5, rely=0.75,
				anchor=CENTER
			)
			return

		nuevo_estado = "Aprobada" if estado_actual == "Pendiente" else "Pendiente"
		self.main.bdd.actualizar_estado_solicitud(id_solicitud, nuevo_estado)
		self.cargar_solicitudes()
		self.texto_exito.place(
			relx=0.5, rely=0.75,
			anchor=CENTER
		)