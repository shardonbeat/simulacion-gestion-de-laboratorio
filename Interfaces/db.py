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
    
    def crear_bdd(self):
        query = '''
                CREATE TABLE IF NOT EXISTS usuarios
                (id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                cedula TEXT NOT NULL,
                password TEXT NOT NULL,
                nacimiento TEXT NOT NULL,
                mail TEXT NOT NULL,
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

        # Crear un usuario administrador por defecto (idempotent)
        self.cursor.execute(insert_q, ('admin', '00000000', '1234', '1970-01-01', 'admin@example.com', 'admin', 3))
        self.conn.commit()

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
        query = "SELECT username, cedula, nacimiento, mail, role, nivel_autorizacion FROM usuarios WHERE cedula = ? LIMIT 1"
        cur = self.cursor.execute(query, (cedula,))
        r = cur.fetchone()

        if r:
            return {
                'username': r[0],
                'cedula': r[1],
                'nacimiento': r[2],
                'mail': r[3],
                'role': r[4],
                'nivel_autorizacion': r[5]
            }
        else:
            return None
        