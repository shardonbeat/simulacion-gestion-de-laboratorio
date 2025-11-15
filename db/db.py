import sqlite3

db = sqlite3.connect('laboratorio.db')
cursor = db.cursor()

def CrearTablaRegistro():
    query = """
            CREATE TABLE IF NOT EXISTS Registro( 
                id_Usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre CHAR(12) NOT NULL,
                Apellido CHAR(12) NOT NULL,
                Cedula CHAR(10) NOT NULL UNIQUE,
                Contraseña CHAR(16) NOT NULL,
                Fecha_nacimiento CHAR(10) NOT NULL,
                Correo CHAR(30) NOT NULL,
                rol CHAR(30) NOT NULL,
                nivel_autorizacion INTEGER NOT NULL
            );
        """  
    cursor.executescript(query)
    print(query)

    db.commit