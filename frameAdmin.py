from customtkinter import *

class frameAdmin (CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color = "#ebebeb",
            corner_radius = 0,
        )

        ## Labels
        self.labelAdmin = CTkLabel(
            master = self, text = "Panel de Administración",
            text_color = "#ffffff",
            font = ("Arial", 20, "bold"), corner_radius = 15,
            fg_color = "#474aff"
        )
        self.labelAdmin.place(
            relx=0.5, rely=0.1,
            relwidth=0.6, relheight=0.15,
            anchor=CENTER
        )