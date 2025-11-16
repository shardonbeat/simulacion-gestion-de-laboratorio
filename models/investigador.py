# CLASE ABUELA USUARIO

from datetime import *

# Registro De Usuarios

class Investigdor:
    
    def __init__(self):
        self.nombre = ObtenerNombre()
        self.apellido = ObtenerApellido()
        self.cedula = ObtenerCédula()
        self.contraseña = ObtenerContraseña()
        self.nacimiento = ObtenerNacimiento()
        self.correo_electronico = ObtenerCorreo()
        self.rol = 'No asignada.'
        self.nivel_autorizacion = 0

def ObtenerDatosParaDB(self):
    return (self.nombre, self.apellido, self.cedula, self.contraseña, self.nacimiento, self.correo_electronico, self.rol, self.nivel_autorizacion)

def ObtenerNombre():
    while True:
        nombre = input("Ingrese su nombre: ").lower()

        if nombre.isalpha():
            print('Nombre valido.')
            return nombre
        else:
            print('Nombre Invalido.\n')
                
                
def ObtenerApellido(): 
    while True:
        apellido = input("Ingrese su apellido: ").lower()

        if apellido.isalpha():
            print('Apellido valido.')
            return apellido
        else:
            print('Apellido Invalido.\n')

def ObtenerCédula():
    while True:
        CI = input("Ingrese su Dni: ")

        if CI.isdigit:
            print("CI valido.")
            return CI
        else:
            print("CI Invalido.\n")

def ObtenerContraseña():
    while True:
        passw = input("Ingrese una contraseña: ")

        if not passw.isspace:
            print("Contraseña valida.")
            return passw
        else:
            print("Contraseña Invalida.\n") 

def ObtenerNacimiento():
    while True:
        try:
            fecha_in = input("Ingrese la fecha en formato YYYY-MM-DD: ")
            fecha = datetime.strptime(fecha_in, '%Y-%m-%d').date()
                    
            if fecha <= datetime.now():
                print("Fecha valida.")
                return fecha
                        
        except:
            print("Fecha Invalida.\n")

def ObtenerCorreo():
    while True:   
        correo = input('Ingrese el correo electronico: ')
        
        if '@' in correo and '.' in correo:
            print('Correo valido.')
            return correo
        else:
            print('Correo Invalido.\n')