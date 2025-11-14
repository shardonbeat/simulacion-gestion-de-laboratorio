from .usuario import Usuario

class Investigador(Usuario):

    def __init__(self, nombre, apellido, nacimiento, correo_electronico):
        super().__init__(nombre, apellido, nacimiento, correo_electronico, 
                         rol = 'Investigador',
                         nivel_autorizacion = 1)
