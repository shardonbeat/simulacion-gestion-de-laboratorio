import sqlite3

# Clase para manejar la base de datos
class BDD:
    def __init__(self):
        self.conn = sqlite3.connect('laboratorio.db')
        self.cursor = self.conn.cursor()
        self.crear_bdd()

    def obtener_usuario(self, cedula):
        query = "SELECT cedula, password FROM usuarios WHERE cedula = ? LIMIT 1"
        self.cursor.execute(query, (cedula,))
        return self.cursor.fetchone()
    
    ## Crear la base de datos y las tablas necesarias
    def crear_bdd(self):
        self.crear_tabla_usuarios()
        self.crear_tabla_sustancias()
        self.crear_tabla_residuos()
        self.crear_tabla_reportes()
        self.crear_tabla_solicitudes_acceso()
        self.crear_tabla_solicitudes_sustancias()
        self.crear_tabla_registros_sustancias_residuos()

    def crear_tabla_usuarios(self):
        try:
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
                    nivel_autorizacion INTEGER NOT NULL,
                    CONSTRAINT user UNIQUE (cedula, password)
                    );
                    '''
            self.cursor.executescript(query)
            self.conn.commit()

            # Verificar si el usuario administrador ya existe y crearlo si no existe
            self.cursor.execute('SELECT id_usuario FROM usuarios WHERE cedula = ?', ('00000000',))
            admin_exists = self.cursor.fetchone()

            if not admin_exists:
                insert_q = '''
                    INSERT OR IGNORE INTO usuarios (username, cedula, password, nacimiento, mail, role, nivel_autorizacion)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    '''

                # Crear un usuario administrador por defecto
                self.cursor.execute(insert_q, ('admin', '00000000', '1234', '1970-01-01', 
                                            'admin@example.com', 'Administrador de Cumplimiento', 3))
                self.conn.commit()
            else:
                print("El usuario administrador ya existe.")

            self.cursor.execute('SELECT id_usuario FROM usuarios WHERE cedula = ?', ('11111111',))
            coordinador_exists = self.cursor.fetchone()

            if not coordinador_exists:
                insert_q = '''
                    INSERT OR IGNORE INTO usuarios (username, cedula, password, nacimiento, mail, role, nivel_autorizacion)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    '''

                # Crear un usuario coordinador por defectos
                self.cursor.execute(insert_q, ('coordinador', '11111111', '1234', '1980-01-01', 
                                            'coordinador@example.com', 'Coordinador de Seguridad', 3))
                self.conn.commit()
            else:
                print("El usuario coordinador ya existe.")
            
        except Exception as e:
            print(f"Error al crear tabla usuarios: {e}")

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

    def crear_tabla_solicitudes_acceso(self):
        query = '''
                CREATE TABLE IF NOT EXISTS solicitudes_acceso
                (id_solicitud_a INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                nivel_solicitado INTEGER NOT NULL,
                motivo TEXT NOT NULL,
                fecha_solicitud TEXT NOT NULL,
                estado TEXT NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
                );
                '''

        self.cursor.executescript(query)
        self.conn.commit()

    def crear_tabla_solicitudes_sustancias(self):
            query = '''
                    CREATE TABLE IF NOT EXISTS solicitudes_sustancias
                    (id_solicitud_s INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    nombre_sustancia TEXT NOT NULL,
                    nivel_riesgo INTEGER NOT NULL,
                    cantidad_solicitada INTEGER NOT NULL,
                    motivo TEXT NOT NULL,
                    fecha_solicitud TEXT NOT NULL,
                    capacitacion TEXT,
                    estado TEXT NOT NULL,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                    FOREIGN KEY (capacitacion) REFERENCES usuarios(capacitacion)
                    );
                    '''
            self.cursor.executescript(query)
            self.conn.commit()

    def obtener_solicitudes_sustancias(self):
        query = '''
            SELECT id_solicitud_s,
                   solicitudes_sustancias.id_solicitud_s,
                   solicitudes_sustancias.id_usuario,
                   solicitudes_sustancias.nombre_sustancia,
                   solicitudes_sustancias.nivel_riesgo,
                   solicitudes_sustancias.cantidad_solicitada,
                   solicitudes_sustancias.motivo,
                   solicitudes_sustancias.fecha_solicitud,
                   solicitudes_sustancias.capacitacion,
                   solicitudes_sustancias.estado
            FROM solicitudes_sustancias
            JOIN usuarios ON solicitudes_sustancias.id_usuario = usuarios.id_usuario;
            '''
        self.cursor.execute(query)
        r = self.cursor.fetchall()
        
        if not r:
            return None
        
        solicitudes = []
        for row in r:
            solicitudes.append({
                'id_solicitud_s': row[0],
                'id_usuario': row[1],
                'nombre_sustancia': row[2],
                'nivel_riesgo': row[3],
                'cantidad_solicitada': row[4],
                'motivo': row[5],
                'fecha_solicitud': row[6],
                'capacitacion': row[7],
                'estado': row[8]
            })
        
        return solicitudes

    def crear_tabla_registros_sustancias_residuos(self):
        query = '''
                CREATE TABLE IF NOT EXISTS registros_sustancias_residuos
                (id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                sustancia TEXT NOT NULL,
                residuo TEXT NOT NULL,
                contenedor TEXT NOT NULL,
                fecha_almacenamiento TEXT NOT NULL,
                fecha_retiro TEXT NOT NULL
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
        query = "SELECT username, cedula, password, nacimiento, mail, capacitacion, role, nivel_autorizacion FROM usuarios WHERE cedula = ? LIMIT 1"
        cur = self.cursor.execute(query, (cedula,))
        r = cur.fetchone()
        if not r:
            return None

        return {
            'username': r[0],
            'cedula': r[1],
            'password': r[2],
            'nacimiento': r[3],
            'mail': r[4],
            'capacitacion': r[5],
            'role': r[6],
            'nivel_autorizacion': r[7]
        }
    
    def obtener_id_usuario(self, cedula):
        query = "SELECT id_usuario FROM usuarios WHERE cedula = ? LIMIT 1"
        self.cursor.execute(query, (cedula,))
        r = self.cursor.fetchone()
        if not r:
            return None
        return r[0]
    
    def crear_solicitud_acceso(self, id_usuario, nivel_solicitado, motivo, fecha_solicitud, estado):
        query = '''
            INSERT INTO solicitudes_acceso (id_usuario, nivel_solicitado, motivo, fecha_solicitud, estado)
            VALUES (?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (id_usuario, nivel_solicitado, motivo, fecha_solicitud, estado))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear solicitud de acceso: {e}")
            return False
        
    def obtener_solicitudes_acceso(self):
        query = '''
            SELECT id_solicitud_a, username, motivo, fecha_solicitud, estado
            FROM solicitudes_acceso
            JOIN usuarios ON solicitudes_acceso.id_usuario = usuarios.id_usuario;
            '''
        self.cursor.execute(query)
        r = self.cursor.fetchall()
        print(r)
        
        if not r:
            return None
        
        solicitudes = []
        for row in r:
            solicitudes.append({
                'id_solicitud_a': row[0],
                'username': row[1],
                'motivo': row[2],
                'fecha_solicitud': row[3],
                'estado': row[4]
            })
        
        return solicitudes
    
    def actualizar_estado_solicitud_acceso(self, id_solicitud, nuevo_estado):
         try:
            query = "UPDATE solicitudes_accesos SET estado = ? WHERE id_solicitud = ?"
            self.cursor.execute(query, (nuevo_estado, id_solicitud))
            self.conn.commit()
            print(f"Estado actualizado: ID {id_solicitud} -> {nuevo_estado}")
            return True
         except Exception as e:
            print(f"Error al actualizar estado de la solicitud: {e}")
            return False
         
    def actualizar_estado_solicitud_sustancias(self, id_sustancia_s, nuevo_estado):
         try:
            query = "UPDATE solicitudes_sustancias SET estado = ? WHERE id_solicitud_s = ?"
            self.cursor.execute(query, (nuevo_estado, id_sustancia_s))
            self.conn.commit()
            print(f"Estado actualizado: ID {id_sustancia_s} -> {nuevo_estado}")
            return True
         except Exception as e:
            print(f"Error al actualizar estado de la solicitud: {e}")
            return False
        
    def guardar_solicitud_sustancias(self, id_usuario, sustancias, nivel_riesgo, cantidades, justificacion, fecha_solicitud, capacitacion, estado):
        query = '''
            INSERT INTO solicitudes_sustancias (id_usuario, nombre_sustancia, nivel_riesgo,
            cantidad_solicitada, motivo, fecha_solicitud, capacitacion, estado)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (id_usuario, sustancias, nivel_riesgo, cantidades, justificacion, fecha_solicitud, capacitacion, estado))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al guardar solicitud de sustancias: {e}")
            return False

    def cerrar_conexion(self):
        self.conn.close()

    def guardar_registro_sustancia_residuo(self, id_usuario, sustancia, residuo, contenedor, fecha_almacenamiento, fecha_retiro):
        query = '''
            INSERT INTO registros_sustancias_residuos (id_usuario, sustancia, residuo, contenedor, fecha_almacenamiento, fecha_retiro)
            VALUES (?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (id_usuario, sustancia, residuo, contenedor, fecha_almacenamiento, fecha_retiro))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al guardar registro de sustancia y residuo: {e}")
            return False
        
    def guardar_reporte_incidente(self, titulo, tipo, descripcion, fecha_creacion, autor):
        query = '''
            INSERT INTO reportes (titulo, tipo_reporte, contenido, fecha_creacion, autor)
            VALUES (?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (titulo, tipo, descripcion, fecha_creacion, autor))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al guardar reporte de incidente: {e}")
            return False
        
    