# SISTEMA DE SIMULACIÓN PARA LA GESTIÓN DE UN LABORATORIO

from datetime import *

while True:

    # Registro De Usuarios

    class Usuario:
        
        def __init__(self):
            self.nombre = ObtenerNombre()
            self.apellido = ObtenerApellido()
            self.nacimiento = ObtenerNacimiento()
            self.correo_electronico = ObtenerCorreo()
            self.rol

    def __str__(self):
         return f'{self.nombre};{self.apellido};{self.nacimiento}'

    def ObtenerNombre():
        
        while True:
                nombre = input("Ingrese su nombre: ").lower()

                if nombre.isalpha():
                    print('Nombre valido.')
                    return nombre
                else:
                    print('Nombre invalido.\n')
                
                
    def ObtenerApellido(): 
         
         while True:
                apellido = input("Ingrese su apellido: ").lower()

                if apellido.isalpha():
                    print('Apellido valido.')
                    return apellido
                else:
                    print('Apellido invalido.\n')

    def ObtenerNacimiento():
        while True:
            try:
                formato = ("%Y-%m-%d")
                fecha_in = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                fecha = datetime.strptime(fecha_in, formato).date()
                    
                if fecha <= datetime.now():
                    print("Fecha valida")
                    return fecha
                        
            except:
                print("Fecha Invalida")

    def ObtenerCorreo():
        
        correo = input('Ingrese el correo electronico: ')
        return correo