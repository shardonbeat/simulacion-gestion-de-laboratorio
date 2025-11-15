from .investigador import Investigdor

class AdminCumplimiento(Investigdor):

    def __init__(self, nombre, apellido, cedula, contraseña, nacimiento, correo_electronico):
        super().__init__(nombre, apellido, cedula, contraseña, nacimiento, correo_electronico,
                         rol = 'Administrador de Cumplimiento',
                         nivel_autorizacion = 3)