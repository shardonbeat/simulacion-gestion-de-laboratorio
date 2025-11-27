from customtkinter import *

class funcionesUsuario (CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
			fg_color = "#A79D8A",
			corner_radius = 0
		)