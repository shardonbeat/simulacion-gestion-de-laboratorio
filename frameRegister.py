from customtkinter import *
from PIL import Image

class frameRegister (CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color = "#A79D8A",
            corner_radius = 0,
        )

        ## Labels

        self.labelFondo = CTkLabel(
			master = self,
			text = "",
			fg_color = "#2b2b39",
			corner_radius=15
		)
        self.labelFondo.place(
			relx=0.5, rely=0.5,
			relwidth=0.35, relheight=0.7,
			anchor=CENTER
		)


        self.labelRegister = CTkLabel(
            master = self, text = "Registro de nuevo usuario",
            text_color = "#ffffff",
            font = ("Times New Roman", 15, "bold"), corner_radius = 15,
            fg_color = "#8b8b9f",
            bg_color= "#2b2b39"
        )
        self.labelRegister.place(
            relx=0.5, rely=0.2,
            relwidth=0.3, relheight=0.05,
            anchor=CENTER
        )

        self.input_username = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
			placeholder_text="Nombre de Usuario", placeholder_text_color='black',
			border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.input_username.place(relx=0.35, rely=0.30,
			relwidth=0.12, relheight=0.05)
        
        self.input_cedula = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
			placeholder_text="Cédula", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.input_cedula.place(relx=0.53, rely=0.30,
			relwidth=0.12, relheight=0.05)
        
        self.input_password = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
            show='*',
			placeholder_text="Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.input_password.place(relx=0.35, rely=0.45,
			relwidth=0.12, relheight=0.05)
        
        self.input_password2 = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
            show='*',
			placeholder_text="Confirmar Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.input_password2.place(relx=0.53, rely=0.45,
			relwidth=0.13, relheight=0.05)
        
        self.input_nacimiento = CTkEntry(
            master=self,
            font=('Arial', 15), text_color='black',
            placeholder_text="Fecha de Nacimiento (YYYY-MM-DD)", 
            placeholder_text_color='black',
            justify='center',
            border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.input_nacimiento.place(relx=0.53, rely=0.60,
			relwidth=0.12, relheight=0.05)
        
        self.mail_input = CTkEntry(
            master=self,
            font=('Arial', 15), text_color='black',
            placeholder_text="Correo Electrónico",
            placeholder_text_color='black',
            justify='center',
            border_color='black', fg_color="#948D8D", bg_color="#2b2b39"
        )
        self.mail_input.place(relx=0.35, rely=0.60,
            relwidth=0.12, relheight=0.05,)
        
        ## Botones

        #@ Botón de registro
        self.register_button = CTkButton(
            master=self,
            text="Registrarse",
            font=('Arial', 15),
            hover_color="#898995",
            bg_color="#2b2b39",
            fg_color="#72737f",
            command=self.registrar_usuario
        )
        self.register_button.place(
            relx=0.5, rely=0.80,
            relwidth=0.12, relheight=0.05,
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
            text_color="#000000",
            fg_color="#A79D8A",
            hover_color="#BAAF9B",
            image=self.back_image,
            command=self.volver_login
        )
        self.back_button.place(
            relx=0, rely=0,
            relwidth=0.10, relheight=0.05,
            anchor=NW
        )

    def registrar_usuario(self):
        username = self.input_username.get()
        cedula = self.input_cedula.get()
        password = self.input_password.get()
        password2 = self.input_password2.get()
        nacimiento = self.input_nacimiento.get()
        mail = self.mail_input.get()
        role = 'Investigador'  # Default role
        nivel_autorizacion = 1  # Default authorization level

        success = self.main.bdd.registrarUsuario(
            username, cedula, password, nacimiento, mail, role, nivel_autorizacion
        )

        if success and password == password2:
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