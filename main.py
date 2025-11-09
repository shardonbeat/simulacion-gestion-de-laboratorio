# SISTEMA DE SIMULACIÓN PARA LA GESTIÓN DE UN LABORATORIO

from datetime import *

while True:

    # Registro De Usuarios

    class Usuario:
        
        def __init__(self):
            self.nombre = ObtenerNombre()
            self.apellido = ObtenerApellido()
            self.nacimiento = ObtenerNacimiento()
    
    def ObtenerNombre():
        
        while True:
                opcion = True
                valid = "abcdefghijklmnñopqrstuvwxyzáéíóú"
                nombre = input("Ingrese su nombre: ").lower()

                for x in nombre:
                    if x not in valid:
                        print("Nombre invalido")
                        opcion = False
                        break

                if opcion:
                    print("Nombre valido")
                    return nombre
                
    def ObtenerApellido(): 
         
         while True:
                opcion = True
                valid = "abcdefghijklmnñopqrstuvwxyzáéíóú"
                apellido = input("Ingrese su apellido: ").lower()

                for x in apellido:
                    if x not in valid:
                        print("Apellido invalido")
                        opcion = False
                        break

                if opcion:
                    print("Apellido valido")
                    return apellido

    def ObtenerNacimiento():
            while True:
                try:
                    formato = ("%Y-%m-%d")
                    hoy = datetime.now().date()
                    fecha_in = input("Ingrese la fecha en formato YYYY-MM-DD: ")
                    fecha = datetime.strptime(fecha_in, formato).date()
                    
                    if fecha <= hoy:
                        print("Fecha valida")
                        return fecha
                        
                    
                except:
                     print("Fecha Invalida")