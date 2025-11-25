import sqlite3

# Clase para manejar la base de datos
class BDD:
    def __init__(self):
        self.conn = sqlite3.connect('laboratorio.db')
        self.cursor = self.conn.cursor()
        self.crear_bdd()

    def obtener_usuario(self):
        query = "SELECT username, password FROM usuarios LIMIT 1"
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    ## Crear la base de datos y las tablas necesarias
    def crear_bdd(self):
        self.crear_tabla_usuarios()
        self.crear_tabla_sustancias()

    def crear_tabla_usuarios(self):
        query = '''
                CREATE TABLE IF NOT EXISTS usuarios
                (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                cedula TEXT NOT NULL,
                password TEXT NOT NULL,
                nacimiento TEXT NOT NULL,
                mail TEXT NOT NULL,
                capacitacion TEXT,
                role TEXT NOT NULL,
                nivel_autorizacion INTEGER NOT NULL
                );
                '''
        self.cursor.executescript(query)

        # Use INSERT OR IGNORE so repeated initialization won't raise UNIQUE constraint errors
        insert_q = '''
            INSERT OR IGNORE INTO usuarios (username, cedula, password, nacimiento, mail, role, nivel_autorizacion)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''

        # Crear un usuario administrador por defecto
        self.cursor.execute(insert_q, ('admin', '00000000', '1234', '1970-01-01', 
                                       'admin@example.com', 'Administrador de Cumplimiento', 3))
        self.conn.commit()

    def crear_tabla_sustancias(self):
        query = '''
                CREATE TABLE IF NOT EXISTS sustancias
                (id_sustancia INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nivel_riesgo INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                ubicacion TEXT NOT NULL,
                fecha_vencimiento TEXT NOT NULL
                );
                '''
        self.cursor.executescript(query)
        self.conn.commit()

    def crear_tabla_residuos(self):
        query = '''
                CREATE TABLE IF NOT EXISTS residuos
                (id_residuo INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                tipo_residuo TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                fecha_almacenamiento TEXT NOT NULL,
                fecha_retiro TEXT NOT NULL
                );
                '''
        self.cursor.executescript(query)
        self.conn.commit()

    def crear_tabla_reportes(self):
        query = '''
                CREATE TABLE IF NOT EXISTS reportes
                (id_reporte INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                contenido TEXT NOT NULL,
                tipo_reporte TEXT NOT NULL,
                fecha_creacion TEXT NOT NULL,
                autor TEXT NOT NULL
                );
                '''
        self.cursor.executescript(query)
        self.conn.commit()

    ## Funciones de la base de datos
    def verificarLogin(self, cedula, password):
            query = "SELECT 1 FROM usuarios WHERE cedula = ? AND password = ? LIMIT 1"
            cur = self.cursor.execute(query, (cedula, password))
            row = cur.fetchone()
            return row is not None
    
    def registrarUsuario(self, username, cedula, password, nacimiento, mail, role, nivel_autorizacion):
        query = '''
            INSERT INTO usuarios (username, cedula, password, nacimiento, mail, role, nivel_autorizacion)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (username, cedula, password, nacimiento, mail, role, nivel_autorizacion))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
            return False
    
    def obtenerUsuario(self, cedula):
        # Seleccionar también la contraseña y mantener un orden consistente de columnas
        query = "SELECT username, cedula, password, nacimiento, mail, role, nivel_autorizacion FROM usuarios WHERE cedula = ? LIMIT 1"
        cur = self.cursor.execute(query, (cedula,))
        r = cur.fetchone()
        print(f"DEBUG - Número de columnas: {len(r) if r else 'None'}")
        print(f"DEBUG - Columnas: {r}")

        # Evitar llamar a len() sobre None y mapear directamente las columnas esperadas
        if not r:
            return None

        return {
            'username': r[0],
            'cedula': r[1],
            'password': r[2],
            'nacimiento': r[3],
            'mail': r[4],
            'role': r[5],
            'nivel_autorizacion': r[6]
        }
        