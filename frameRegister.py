from customtkinter import *
from PIL import Image

class frameRegister (CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color = "#ebebeb",
            corner_radius = 0,
        )

        ## Labels
        self.labelRegister = CTkLabel(
            master = self, text = "Registro de nuevo usuario",
            text_color = "#ffffff",
            font = ("Arial", 20, "bold"), corner_radius = 15,
            fg_color = "#474aff"
        )
        self.labelRegister.place(
            relx=0.5, rely=0.1,
            relwidth=0.6, relheight=0.15,
            anchor=CENTER
        )

        self.input_username = CTkEntry(
			master=self,
			font=('Arial', 25), text_color='black',
			placeholder_text="Nombre de Usuario", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color='white', border_width=5
        )
        self.input_username.place(relx=0.35, rely=0.30,
			relwidth=0.3, relheight=0.1, anchor=CENTER)
        
        self.input_cedula = CTkEntry(
			master=self,
			font=('Arial', 25), text_color='black',
			placeholder_text="Cédula", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color='white', border_width=5
        )
        self.input_cedula.place(relx=0.65, rely=0.30,
			relwidth=0.3, relheight=0.1, anchor=CENTER)
        
        self.input_password = CTkEntry(
			master=self,
			font=('Arial', 25), text_color='black',
			placeholder_text="Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color='white', border_width=5
        )
        self.input_password.place(relx=0.35, rely=0.45,
			relwidth=0.3, relheight=0.1, anchor=CENTER)
        
        self.input_nacimiento = CTkEntry(
            master=self,
            font=('Arial', 25), text_color='black',
            placeholder_text="Fecha de Nacimiento (YYYY-MM-DD)", 
            placeholder_text_color='black',
            justify='center',
            border_color='black', fg_color='white', border_width=5
        )
        self.input_nacimiento.place(relx=0.65, rely=0.45,
			relwidth=0.3, relheight=0.1, anchor=CENTER)
        
        self.mail_input = CTkEntry(
            master=self,
            font=('Arial', 25), text_color='black',
            placeholder_text="Correo Electrónico",
            placeholder_text_color='black',
            justify='center',
            border_color='black', fg_color='white', border_width=5
        )
        self.mail_input.place(relx=0.5, rely=0.60,
            relwidth=0.3, relheight=0.1, anchor=CENTER)
        
        ## Botones

        #@ Botón de registro
        self.register_button = CTkButton(
            master=self,
            text="Enviar Solicitud",
            font=('Arial', 20),
            fg_color="#474aff",
            hover_color="#353edc",
            command=self.registrar_usuario
        )
        self.register_button.place(
            relx=0.5, rely=0.80,
            relwidth=0.4, relheight=0.1,
            anchor=CENTER
        )

        #@ Botón de volver al login
        self.back_image = CTkImage(
            light_image=Image.open(os.path.join(os.path.dirname(__file__), "Img", "back_image.png")),
            dark_image=Image.open(os.path.join(os.path.dirname(__file__), "Img", "back_image.png")),
            size=(30, 30)
        )

        self.back_button = CTkButton(
            master=self,
            text = 'Volver',
            font=('Arial', 25),
            text_color="#4000FF",
            fg_color="#ebebeb",
            image=self.back_image,
            command=self.volver_login
        )
        self.back_button.place(
            relx=0, rely=0,
            relwidth=0.15, relheight=0.1,
            anchor=NW
        )

    def registrar_usuario(self):
        username = self.input_username.get()
        cedula = self.input_cedula.get()
        password = self.input_password.get()
        nacimiento = self.input_nacimiento.get()
        mail = self.mail_input.get()
        role = 'Investigador'  # Default role
        nivel_autorizacion = 1  # Default authorization level

        success = self.main.bdd.registrarUsuario(
            username, cedula, password, nacimiento, mail, role, nivel_autorizacion
        )

        if success:
            print("Usuario registrado exitosamente.")
            # Optionally, clear the input fields after successful registration
            self.input_username.delete(0, 'end')
            self.input_cedula.delete(0, 'end')
            self.input_password.delete(0, 'end')
            self.input_nacimiento.delete(0, 'end')
            self.mail_input.delete(0, 'end')
        else:
            print("Error al registrar el usuario.")

    def volver_login(self):
        self.main.frameRegister.place_forget()
        self.main.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )