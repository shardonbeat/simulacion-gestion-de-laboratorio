from customtkinter import *
from datetime import datetime

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
			text="Alertas De Seguridad",
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

        # Combobox con tipos de alerta predefinidos
        self.comboTipoAlerta = CTkComboBox(
            master=self,
            values=[
                "Vencimiento de sustancia",
                "Stock crítico", 
                "Riesgo de exposición",
                "Capacitación vencida",
                "Residuos sin registrar",
                "Alerta personalizada"
            ],
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            dropdown_fg_color="#5e5e72",
            dropdown_font=("Arial", 12),
            corner_radius=10,
            state="readonly"
        )
        self.comboTipoAlerta.place(
            relx=0.35, rely=0.3,
            relwidth=0.6, relheight=0.05
        )
        self.comboTipoAlerta.set("Seleccione tipo de alerta")

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
            corner_radius=10,
            command=self.emitir_alerta
        )
        self.botonRegistrar.place(
            relx=0.35, rely=0.8,
            relwidth=0.3, relheight=0.07
        )

        # Botón para alertas automáticas
        self.botonAlertasAutomaticas = CTkButton(
            master=self,
            text="Generar Alertas Auto",
            hover_color="#4a4a5e",
            text_color="#ffffff",
            fg_color="#3a3a4a",
            bg_color="#2b2b39",
            font=("Times New Roman", 12, "bold"),
            corner_radius=10,
            command=self.generar_alertas_automaticas
        )
        self.botonAlertasAutomaticas.place(
            relx=0.7, rely=0.8,
            relwidth=0.25, relheight=0.07
        )

        # Labels de éxito / error
        self.mensaje_exito_label = CTkLabel(
            master=self,
            text="Alerta emitida correctamente.",
            text_color="#00ff00",
            font=("Times New Roman", 12, "bold"),
        )

        self.mensaje_error_label = CTkLabel(
            master=self,
            text="",
            text_color="#ff0000",
            font=("Times New Roman", 12, "bold"),
        )

    def emitir_alerta(self):
        try:
            tipo = self.comboTipoAlerta.get().strip()
        except Exception:
            tipo = ""

        try:
            mensaje = self.entryMensaje.get("1.0", "end-1c").strip()
        except Exception:
            try:
                mensaje = self.entryMensaje.get().strip()
            except Exception:
                mensaje = ""

        if not tipo or tipo == "Seleccione tipo de alerta":
            self.mensaje_error_label.configure(text="Seleccione el tipo de alerta.")
            self.mensaje_error_label.place(relx=0.5, rely=0.93, anchor=CENTER)
            return

        if not mensaje:
            # Generar mensaje automático basado en el tipo
            mensaje = self.generar_mensaje_automatico(tipo)
            if not mensaje:
                self.mensaje_error_label.configure(text="Complete el mensaje de la alerta.")
                self.mensaje_error_label.place(relx=0.5, rely=0.93, anchor=CENTER)
                return

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            autor = self.main.usuario_actual.get('username', '')
        except Exception:
            autor = ''

        ok = False
        try:
            ok = self.main.bdd.crear_alerta(tipo, mensaje, fecha, autor)
        except Exception as e:
            print(f"Error al llamar crear_alerta: {e}")

        if ok:
            self.limpiar_campos()
            self.mensaje_error_label.configure(text="")
            self.mensaje_exito_label.place(relx=0.5, rely=0.93, anchor=CENTER)
        else:
            self.mensaje_error_label.configure(text="No se pudo emitir la alerta.")
            self.mensaje_error_label.place(relx=0.5, rely=0.93, anchor=CENTER)

    def generar_mensaje_automatico(self, tipo):
        """Genera mensajes automáticos para los tipos predefinidos"""
        if tipo == "Vencimiento de sustancia":
            return "¡La sustancia 'Benceno' del lote B2024 vence en 5 días!"
        elif tipo == "Stock crítico":
            return "¡Stock crítico detectado en el inventario de sustancias!"
        elif tipo == "Riesgo de exposición":
            return "¡Riesgo de exposición detectado en el laboratorio!"
        elif tipo == "Capacitación vencida":
            return "¡El investigador X no ha actualizado su capacitación desde hace 11 meses!"
        elif tipo == "Residuos sin registrar":
            return "¡Se generaron 8 residuos sin registrar en el laboratorio 301!"
        else:
            return ""

    def generar_alertas_automaticas(self):
        """Genera alertas automáticas basadas en datos reales de la BD"""
        alertas_generadas = 0
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            # Alertas de vencimiento de sustancias
            sustancias = self.main.bdd.obtener_sustancias()
            hoy = datetime.now().date()
            
            for sustancia in sustancias:
                if sustancia.get('fecha_vencimiento'):
                    try:
                        fecha_vencimiento = datetime.strptime(sustancia['fecha_vencimiento'], "%Y-%m-%d").date()
                        dias_restantes = (fecha_vencimiento - hoy).days
                        
                        if 0 <= dias_restantes <= 7:
                            mensaje = f"¡La sustancia '{sustancia['name']}' del lote {sustancia.get('lote', 'N/A')} vence en {dias_restantes} días!"
                            self.main.bdd.crear_alerta("Vencimiento de sustancia", mensaje, fecha, "Sistema")
                            alertas_generadas += 1
                    except Exception as e:
                        print(f"Error procesando sustancia {sustancia['name']}: {e}")
            
            # Alertas de stock crítico
            for sustancia in sustancias:
                if sustancia.get('cantidad', 0) <= 10:
                    mensaje = f"¡Stock crítico de {sustancia['name']}! Solo quedan {sustancia['cantidad']} unidades."
                    self.main.bdd.crear_alerta("Stock crítico", mensaje, fecha, "Sistema")
                    alertas_generadas += 1
                    
        except Exception as e:
            print(f"Error generando alertas automáticas: {e}")

        if alertas_generadas > 0:
            self.mensaje_exito_label.configure(text=f"Se generaron {alertas_generadas} alertas automáticas")
            self.mensaje_exito_label.place(relx=0.5, rely=0.93, anchor=CENTER)
            self.mensaje_error_label.place_forget()
        else:
            self.mensaje_exito_label.configure(text="No se encontraron situaciones que requieran alertas")
            self.mensaje_exito_label.place(relx=0.5, rely=0.93, anchor=CENTER)
            self.mensaje_error_label.place_forget()

    def limpiar_campos(self):
        try:
            self.entryMensaje.delete("1.0", "end")
        except Exception:
            try:
                self.entryMensaje.delete(0, 'end')
            except Exception:
                pass
        self.comboTipoAlerta.set("Seleccione tipo de alerta")