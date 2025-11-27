from customtkinter import *
from datetime import datetime

class GestionarInventario(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )
        self.frame_actual = GestionarInventario
        self.AgregarSustancia = None
        self.ModificarSustancia = None
        self.EliminarSustancia = None

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
            corner_radius=15,
            command = lambda: self.frame_manager(1)
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
            corner_radius=15,
            command = lambda: self.frame_manager(2)
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
            corner_radius=15,
            command = lambda: self.frame_manager(3)
        )
        self.BotonEliminar.place(
            relx=0.4, rely=0.55,
            relwidth=0.2, relheight=0.1
        )

    def frame_manager(self, frame):
        self.cerrar_ventanas()
        
        if frame == 1:
            print('Agregar...')
            self.AgregarSustancia = AgregarSustancia(self.main.ventana, self.main)
            self.AgregarSustancia.place(relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75)
            self.frame_actual = self.AgregarSustancia
        elif frame == 2:
            print('Modificar...')
            self.ModificarSustancia = ModificarSustancia(self.main.ventana, self.main)
            self.ModificarSustancia.place(relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75)
            self.frame_actual = self.ModificarSustancia
        elif frame == 3:
            print('Eliminar...')
            self.EliminarSustancia = EliminarSustancia(self.main.ventana, self.main)
            self.EliminarSustancia.place(relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75)
            self.frame_actual = self.EliminarSustancia

    def cerrar_ventanas(self):
        ventanas = [
            self.AgregarSustancia,
            self.ModificarSustancia,
            self.EliminarSustancia
        ]
        
        for ventana in ventanas:
            if ventana is not None:
                ventana.place_forget()

        self.frame_actual = None

class AgregarSustancia(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main

        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        self.labelContenido = CTkLabel(
			master=self,
			text="Inventario De Sustancias | Agregar",
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

        self.labelNombre = CTkLabel(
            master=self,
            text="Nombre de Sustancia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelNombre.place(
            relx=0.05, rely=0.25,
            relwidth=0.3, relheight=0.05
        )

        self.entryNombre = CTkEntry(
            master=self,
            fg_color="#5e5e72",
			bg_color="#2b2b39",
            placeholder_text="Ej: Ácidos diluidos | Solventes Orgánicos | Neurotóxicos",
			font=("Times New Roman", 15),
			corner_radius=10
        )
        self.entryNombre.place(
            relx=0.1, rely=0.3,
            relwidth=0.4, relheight=0.05
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
            relx=0.47, rely=0.25,
            relwidth=0.4, relheight=0.05
        )

        self.entryNivelRiesgo = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="1 | 2 | 3",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryNivelRiesgo.place(
            relx=0.6, rely=0.3,
            relwidth=0.15, relheight=0.05
        )

        self.error_nivelRiesgo = CTkLabel(
			master=self,
			text="Nivel invalido",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
		)

        self.labelCantidad = CTkLabel(
            master=self,
            text="Cantidad:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelCantidad.place(
            relx=0.1, rely=0.4,
            relwidth=0.1, relheight=0.05
        )

        self.entryCantidad = CTkEntry(
            master=self,
            fg_color="#5e5e72",
			bg_color="#2b2b39",
            placeholder_text="Cantidad",
			font=("Times New Roman", 15),
			corner_radius=10
        )
        self.entryCantidad.place(
            relx=0.10, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.error_cantidad = CTkLabel(
			master=self,
			text="Cantidad invalida",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
		)


        self.labelUbicacion = CTkLabel(
            master=self,
            text="Ubicacion: ",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelUbicacion.place(
            relx=0.47, rely=0.4,
            relwidth=0.4, relheight=0.05
        )

        self.entryUbicacion = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Ej: 294 | 301 | 067",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryUbicacion.place(
            relx=0.6, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.labelFechaVencimiento = CTkLabel(
            master=self,
            text="Fecha de Vencimiento:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaVencimiento.place(
            relx=0.01, rely=0.55,
            relwidth=0.35, relheight=0.05
        )

        self.entryFechaVencimiento = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryFechaVencimiento.place(
            relx=0.1, rely=0.6,
            relwidth=0.15, relheight=0.05
        )
        
        self.error_fecha = CTkLabel(
			master=self,
			text="Fecha invalida",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
		)

        self.labelLote = CTkLabel(
            master=self,
            text="Lote: ",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelLote.place(
            relx=0.53, rely=0.55,
            relwidth=0.2, relheight=0.05
        )

        self.entryLote = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Ej: B2025",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryLote.place(
            relx=0.6, rely=0.6,
            relwidth=0.15, relheight=0.05
        )

        self.texto_exito = CTkLabel(
			master=self,
			text="Sustancia agregada con éxito.",
			text_color="#00ff00",
			font=("Times New Roman", 12, "bold"),
            )
        
        self.error_vacios = CTkLabel(
			master=self,
			text="Todos los campos son obligatorios.",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
        )

        self.botonRegistrar = CTkButton(
            master=self,
            text="Agregar Sustancia",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command = self.agregar_sustancia
        )
        self.botonRegistrar.place(
            relx=0.35, rely=0.8,
            relwidth=0.3, relheight=0.07
        )

    def agregar_sustancia(self):
        self.quitar_errores()
    
        nombre_sustancia = self.entryNombre.get()
        nivel_riesgo = self.entryNivelRiesgo.get()
        cantidad = self.entryCantidad.get()
        ubicacion = self.entryUbicacion.get()
        fecha_vencimiento = self.entryFechaVencimiento.get()
        lote = self.entryLote.get()

        paso = True
        if not nombre_sustancia:
            self.mensaje_vacios()
            paso = False
        if not self.validar_fecha():
            paso = False
        if not self.validar_nivelRiesgo():
            paso = False
        if not self.validar_cantidad():
            paso = False
        if not ubicacion:
            self.mensaje_vacios()
            paso = False
        if not lote:
            self.mensaje_vacios()
            paso = False

        if not paso:
            print('Datos incorrectos.')
            return False
        
        success = self.main.bdd.agregar_sustancia(
			nombre_sustancia, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote
		)

        if success and paso:
            self.mensaje_exito()
            self.quitar_errores()

    def validar_nivelRiesgo(self):
        nivel_riesgo_text = self.entryNivelRiesgo.get()

        try:
            if not nivel_riesgo_text:
                self.mensaje_vacios()
                return False

            nr = int(nivel_riesgo_text)
            if nr in (1, 2, 3):
                return True
            else:
                self.error_nivelRiesgo.place(
                    relx=0.6, rely=0.35,
                    relwidth=0.15, relheight=0.05
                )
                return False
        except ValueError:
            # Not an integer
            self.error_nivelRiesgo.place(
                relx=0.6, rely=0.35,
                relwidth=0.15, relheight=0.05
            )
            return False
        except Exception as e:
            print(f'Error validating nivel_riesgo: {e}')
            return False

    def validar_cantidad(self):
        cantidad = int(self.entryCantidad.get())

        try:
            if not cantidad:
                self.mensaje_vacios()
                return False
            elif cantidad < 0:
                self.error_cantidad.place(
                    relx=0.2, rely=0.45,
                    relwidth=0.15, relheight=0.05
                )
                return False
            else:
                return True
        except Exception as e:
            print(f'Error {e}')

    def validar_fecha(self):
        try:
            fecha_text = self.entryFechaVencimiento.get()
            fecha = datetime.strptime(fecha_text, "%Y-%m-%d").date()

        except Exception as e:
            print(e)
            return False

        if not fecha:
            self.mensaje_vacios()
            return False
        elif datetime.now().date() <= fecha:
            return True
        else:
            self.error_fecha.place(
                relx=0.1, rely=0.65
            )
            return False
        
    def quitar_errores(self):
        self.error_fecha.place_forget()
        self.error_nivelRiesgo.place_forget()
        self.error_cantidad.place_forget()
        self.error_vacios.place_forget()

    def mensaje_exito(self):
        self.texto_exito.place(
            relx=0.5, rely=0.88,
            anchor=CENTER
        )

    def mensaje_vacios(self):
        self.error_vacios.place(
            relx=0.5, rely=0.88,
            anchor=CENTER
        )

class ModificarSustancia(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        # Título
        self.labelContenido = CTkLabel(
            master=self,
            text="Inventario De Sustancias | Modificar",
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

        # Selector de sustancia (combo cargado desde la tabla 'sustancias')
        self.seleccionar_sustancia_l = CTkLabel(
            master=self,
            text="Seleccionar Sustancia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.seleccionar_sustancia_l.place(
            relx=0.05, rely=0.17,
            relwidth=0.3, relheight=0.05
        )

        self.seleccionar_sustancia = CTkComboBox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            dropdown_font=("Arial", 12, "bold"),
            corner_radius=10,
            values=[],
            hover=True
        )
        self.seleccionar_sustancia.place(
            relx=0.3, rely=0.17,
            relwidth=0.4, relheight=0.06
        )

        # Cargar sustancias desde la BDD y mapear id->datos
        self.sustancias_map = {}  # name -> dict row
        self._cargar_combo_sustancias()
        self.seleccionar_sustancia.configure(command=self.cargar_detalle_seleccion)

        # Campos similares a AgregarSustancia para editar
        self.labelNombre = CTkLabel(
            master=self,
            text="Nombre de Sustancia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelNombre.place(
            relx=0.05, rely=0.25,
            relwidth=0.3, relheight=0.05
        )

        self.entryNombre = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Ej: Ácidos diluidos | Solventes Orgánicos | Neurotóxicos",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryNombre.place(
            relx=0.1, rely=0.3,
            relwidth=0.4, relheight=0.05
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
            relx=0.47, rely=0.25,
            relwidth=0.4, relheight=0.05
        )

        self.entryNivelRiesgo = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="1 | 2 | 3",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryNivelRiesgo.place(
            relx=0.6, rely=0.3,
            relwidth=0.15, relheight=0.05
        )

        self.labelCantidad = CTkLabel(
            master=self,
            text="Cantidad:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelCantidad.place(
            relx=0.1, rely=0.4,
            relwidth=0.1, relheight=0.05
        )

        self.entryCantidad = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Cantidad",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryCantidad.place(
            relx=0.1, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.labelUbicacion = CTkLabel(
            master=self,
            text="Ubicacion:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelUbicacion.place(
            relx=0.47, rely=0.4,
            relwidth=0.4, relheight=0.05
        )

        self.entryUbicacion = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Ej: 294 | 301 | 067",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryUbicacion.place(
            relx=0.6, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.labelFechaVencimiento = CTkLabel(
            master=self,
            text="Fecha de Vencimiento:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaVencimiento.place(
            relx=0.01, rely=0.55,
            relwidth=0.35, relheight=0.05
        )

        self.entryFechaVencimiento = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="AAAA-MM-DD",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryFechaVencimiento.place(
            relx=0.1, rely=0.6,
            relwidth=0.15, relheight=0.05
        )

        self.labelLote = CTkLabel(
            master=self,
            text="Lote:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelLote.place(
            relx=0.53, rely=0.55,
            relwidth=0.2, relheight=0.05
        )

        self.entryLote = CTkEntry(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            placeholder_text="Ej: B2025",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.entryLote.place(
            relx=0.6, rely=0.6,
            relwidth=0.15, relheight=0.05
        )

        self.texto_exito = CTkLabel(
            master=self,
            text="Sustancia modificada con éxito.",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.error_vacios = CTkLabel(
            master=self,
            text="Todos los campos son obligatorios.",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

        # Botón para aplicar modificación
        self.botonModificar = CTkButton(
            master=self,
            text="Guardar Cambios",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.modificar_sustancia
        )
        self.botonModificar.place(
            relx=0.35, rely=0.8,
            relwidth=0.3, relheight=0.07
        )

        # Labels de error reutilizables
        self.error_nivelRiesgo = CTkLabel(
            master=self,
            text="Nivel invalido",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

        self.error_cantidad = CTkLabel(
            master=self,
            text="Cantidad invalida",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

        self.error_fecha = CTkLabel(
            master=self,
            text="Fecha invalida",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def _cargar_combo_sustancias(self):
        rows = self.main.bdd.obtener_sustancias()
        names = []
        self.sustancias_map = {}
        for r in rows:
            names.append(r['name'])
            self.sustancias_map[r['name']] = r
        try:
            self.seleccionar_sustancia.configure(values=names)
        except Exception:
            pass

    def cargar_detalle_seleccion(self, val=None):
        # val may be passed by the combobox; get current selection
        name = self.seleccionar_sustancia.get()
        if not name:
            return
        data = self.sustancias_map.get(name)
        if not data:
            return
        # llenar campos
        self.entryNombre.delete(0, 'end')
        self.entryNombre.insert(0, data.get('name',''))
        self.entryNivelRiesgo.delete(0, 'end')
        self.entryNivelRiesgo.insert(0, str(data.get('nivel_riesgo','')))
        self.entryCantidad.delete(0, 'end')
        self.entryCantidad.insert(0, str(data.get('cantidad','')))
        self.entryUbicacion.delete(0, 'end')
        self.entryUbicacion.insert(0, data.get('ubicacion',''))
        self.entryFechaVencimiento.delete(0, 'end')
        self.entryFechaVencimiento.insert(0, data.get('fecha_vencimiento',''))
        self.entryLote.delete(0, 'end')
        self.entryLote.insert(0, data.get('lote','') or '')

    def modificar_sustancia(self):
        # Validaciones similares a Agregar
        self.error_fecha.place_forget()
        self.error_nivelRiesgo.place_forget()
        self.error_cantidad.place_forget()
        self.error_vacios.place_forget()

        nombre_sustancia = self.entryNombre.get()
        nivel_riesgo = self.entryNivelRiesgo.get()
        cantidad = self.entryCantidad.get()
        ubicacion = self.entryUbicacion.get()
        fecha_vencimiento = self.entryFechaVencimiento.get()
        lote = self.entryLote.get()

        paso = True
        if not nombre_sustancia:
            self.error_vacios.place(relx=0.5, rely=0.88, anchor=CENTER)
            paso = False
        # fecha
        try:
            fecha = datetime.strptime(fecha_vencimiento, "%Y-%m-%d").date()
            if datetime.now().date() > fecha:
                self.error_fecha.place(relx=0.1, rely=0.65)
                paso = False
        except Exception:
            self.error_fecha.place(relx=0.1, rely=0.65)
            paso = False

        # nivel
        try:
            nr = int(nivel_riesgo)
            if nr not in (1,2,3):
                self.error_nivelRiesgo.place(relx=0.6, rely=0.35, relwidth=0.15, relheight=0.05)
                paso = False
        except Exception:
            self.error_nivelRiesgo.place(relx=0.6, rely=0.35, relwidth=0.15, relheight=0.05)
            paso = False

        # cantidad
        try:
            cant = int(cantidad)
            if cant < 0:
                self.error_cantidad.place(relx=0.08, rely=0.5, relwidth=0.15, relheight=0.05)
                paso = False
        except Exception:
            self.error_cantidad.place(relx=0.08, rely=0.5, relwidth=0.15, relheight=0.05)
            paso = False

        if not paso:
            return False

        # obtener id de la seleccion
        selected = self.seleccionar_sustancia.get()
        data = self.sustancias_map.get(selected)
        if not data:
            self.error_vacios.place(relx=0.5, rely=0.88, anchor=CENTER)
            return False
        id_sust = data['id_sustancia']

        success = self.main.bdd.modificar_sustancia(
            id_sust,
            name=nombre_sustancia,
            nivel_riesgo=nr,
            cantidad=cant,
            ubicacion=ubicacion,
            fecha_vencimiento=fecha_vencimiento,
            lote=lote
        )

        if success:
            self.texto_exito.place(relx=0.5, rely=0.88, anchor=CENTER)
            # recargar combobox
            self._cargar_combo_sustancias()
            return True
        return False

class EliminarSustancia(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main

        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        self.labelContenido = CTkLabel(
			master=self,
			text="Inventario De Sustancias | Eliminar",
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

        self.seleccionar_sustancia_l = CTkLabel(
            master=self,
            text="Seleccionar Sustancia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.seleccionar_sustancia_l.place(
            relx=0.05, rely=0.17,
            relwidth=0.3, relheight=0.05
        )

        self.seleccionar_sustancia = CTkComboBox(
            master=self,
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            dropdown_font=("Arial", 12, "bold"),
            corner_radius=10,
            values=[],
            hover=True
        )
        self.seleccionar_sustancia.place(
            relx=0.3, rely=0.17,
            relwidth=0.4, relheight=0.06
        )

        # Cargar y enlazar
        self.sustancias_map = {}
        self._cargar_combo_sustancias_eliminar()
        self.seleccionar_sustancia.configure(command=self._mostrar_detalle_eliminar)

        # Detalles (labels que actúan como campos de solo lectura, ubicados igual que en ModificarSustancia)
        self.labelNombre = CTkLabel(
            master=self,
            text="Nombre de Sustancia:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelNombre.place(
            relx=0.05, rely=0.25,
            relwidth=0.3, relheight=0.05
        )

        self.detalle_nombre = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_nombre.place(
            relx=0.1, rely=0.3,
            relwidth=0.4, relheight=0.05
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
            relx=0.47, rely=0.25,
            relwidth=0.4, relheight=0.05
        )

        self.detalle_nivel = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_nivel.place(
            relx=0.6, rely=0.3,
            relwidth=0.15, relheight=0.05
        )

        self.labelCantidad = CTkLabel(
            master=self,
            text="Cantidad:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelCantidad.place(
            relx=0.1, rely=0.4,
            relwidth=0.1, relheight=0.05
        )

        self.detalle_cantidad = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_cantidad.place(
            relx=0.10, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.labelUbicacion = CTkLabel(
            master=self,
            text="Ubicacion:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelUbicacion.place(
            relx=0.47, rely=0.4,
            relwidth=0.4, relheight=0.05
        )

        self.detalle_ubicacion = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_ubicacion.place(
            relx=0.6, rely=0.45,
            relwidth=0.15, relheight=0.05
        )

        self.labelFechaVencimiento = CTkLabel(
            master=self,
            text="Fecha de Vencimiento:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelFechaVencimiento.place(
            relx=0.01, rely=0.55,
            relwidth=0.35, relheight=0.05
        )

        self.detalle_venc = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_venc.place(
            relx=0.1, rely=0.6,
            relwidth=0.15, relheight=0.05
        )

        self.labelLote = CTkLabel(
            master=self,
            text="Lote:",
            text_color="#ffffff",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
        )
        self.labelLote.place(
            relx=0.53, rely=0.55,
            relwidth=0.2, relheight=0.05
        )

        self.detalle_lote = CTkLabel(
            master=self,
            text="",
            text_color="#ffffff",
            fg_color="#5e5e72",
            font=("Times New Roman", 15),
            corner_radius=10
        )
        self.detalle_lote.place(
            relx=0.6, rely=0.6,
            relwidth=0.15, relheight=0.05
        )

        # Botón eliminar y texto de éxito
        self.botonEliminar = CTkButton(
            master=self,
            text="Eliminar Sustancia",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.eliminar_sustancia_seleccionada
        )
        self.botonEliminar.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.07)

        self.texto_exito_eliminar = CTkLabel(
            master=self,
            text="Sustancia eliminada con éxito.",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold")
        )

    def _cargar_combo_sustancias_eliminar(self):
        rows = self.main.bdd.obtener_sustancias()
        names = []
        self.sustancias_map = {}
        for r in rows:
            names.append(r['name'])
            self.sustancias_map[r['name']] = r
        try:
            self.seleccionar_sustancia.configure(values=names)
        except Exception:
            pass

    def _mostrar_detalle_eliminar(self, val=None):
        name = self.seleccionar_sustancia.get()
        if not name:
            return
        data = self.sustancias_map.get(name)
        if not data:
            return
        self.detalle_nombre.configure(text=data.get('name',''))
        self.detalle_nivel.configure(text=str(data.get('nivel_riesgo','')))
        self.detalle_cantidad.configure(text=str(data.get('cantidad','')))
        self.detalle_ubicacion.configure(text=data.get('ubicacion',''))
        self.detalle_venc.configure(text=data.get('fecha_vencimiento',''))
        self.detalle_lote.configure(text=data.get('lote','') or '')

    def eliminar_sustancia_seleccionada(self):
        selected = self.seleccionar_sustancia.get()
        data = self.sustancias_map.get(selected)
        if not data:
            return False
        id_sust = data['id_sustancia']
        ok = self.main.bdd.eliminar_sustancia(id_sust)
        if ok:
            self.texto_exito_eliminar.place(relx=0.5, rely=0.88, anchor=CENTER)
            # limpiar detalles
            self.detalle_nombre.configure(text="")
            self.detalle_nivel.configure(text="")
            self.detalle_cantidad.configure(text="")
            self.detalle_ubicacion.configure(text="")
            self.detalle_venc.configure(text="")
            self.detalle_lote.configure(text="")
            # recargar combobox
            self._cargar_combo_sustancias_eliminar()
            return True
        return False