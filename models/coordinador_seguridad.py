from .usuario import Usuario

class CoordinadorSeguridad(Usuario):

    def __init__(self, nombre, apellido, nacimiento, correo_electronico):
        super.__init__(nombre, apellido, nacimiento, correo_electronico,
                       rol = 'Coordinador de Seguridad',
                       nivel_autorizacion = 2)
