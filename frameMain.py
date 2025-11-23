from customtkinter import *

class frameMain (CTkFrame):
	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		self.configure(
			fg_color = "#ebebeb",
			corner_radius = 0,
		)

		## Labels
		self.labelWelcome = CTkLabel(
			master = self, text = "Bienvenido al sistema",
			text_color = "#ffffff",
			font = ("Arial", 20, "bold"), corner_radius = 15,
			fg_color = "#474aff"
		)
		self.labelWelcome.place(
			relx=0.5, rely=0.1,
			relwidth=0.6, relheight=0.15,
			anchor=CENTER
		)