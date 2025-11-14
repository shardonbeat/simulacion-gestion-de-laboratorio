from .usuario import Usuario

class AdminCumplimiento(Usuario):

    def __init__(self, nombre, apellido, nacimiento, correo_electronico):
        super().__init__(nombre, apellido, nacimiento, correo_electronico,
                         rol = 'Administrador de Cumplimiento',
                         nivel_autorizacion = 3)