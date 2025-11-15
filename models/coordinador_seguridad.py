from .investigador import Investigdor

class CoordinadorSeguridad(Investigdor):

    def __init__(self, nombre, apellido, cedula, contraseña, nacimiento, correo_electronico):
        super().__init__(nombre, apellido, cedula, contraseña, nacimiento, correo_electronico,
                         rol = 'Coordinador de Seguridad',
                         nivel_autorizacion = 2)
