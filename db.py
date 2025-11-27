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
    
    def obtener_capacitacion(self, id):
        query = "SELECT capacitacion FROM capacitaciones WHERE id_usuario = ? LIMIT 1"
        self.cursor.execute(query, (id,))
        r = self.cursor.fetchone()
        if not r:
            return None
        return r[0]
    
    ## Crear la base de datos y las tablas necesarias
    def crear_bdd(self):
        self.crear_tabla_usuarios()
        self.crear_tabla_sustancias()
        self.crear_tabla_residuos()
        self.crear_tabla_reportes()
        self.crear_tabla_solicitudes_acceso()
        self.crear_tabla_solicitudes_sustancias()
        self.crear_tabla_registros_sustancias_residuos()
        self.crear_tabla_capacitaciones()

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
                    role TEXT NOT NULL,
                    nivel_autorizacion INTEGER NOT NULL,
                    id_capacitacion INTEGER,
                    capacitacion TEXT,
                    CONSTRAINT user UNIQUE (cedula, password),
                    FOREIGN KEY (id_capacitacion) REFERENCES capacitaciones(id_capacitacion),
                    FOREIGN KEY (capacitacion) REFERENCES capacitaciones(capacitacion)
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

    def crear_tabla_capacitaciones(self):
        try:
            query = '''
                    CREATE TABLE IF NOT EXISTS capacitaciones
                    (id_capacitacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    capacitacion TEXT,
                    id_usuario INTEGER NOT NULL,
                    fecha_vigencia TEXT NOT NULL,
                    fecha_caducidad TEXT NOT NULL,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
                    )
                    '''
            self.cursor.executescript(query)
            self.conn.commit()
        except Exception as e:
            print(f'Error: {e}')
        
    def guardar_capacitacion(self, capacitacion, id_usuario, fecha_vigencia, fecha_caducidad):
        query = '''
            INSERT INTO capacitaciones (capacitacion, id_usuario, fecha_vigencia, fecha_caducidad)
            VALUES (?, ?, ?, ?);
            '''
        try:
            # Insertar la capacitación y obtener su id
            self.cursor.execute(query, (capacitacion, id_usuario, fecha_vigencia, fecha_caducidad))
            id_cap = self.cursor.lastrowid

            # Asignar la capacitación al usuario correspondiente
            update_q = 'UPDATE usuarios SET id_capacitacion = ? WHERE id_usuario = ?'
            self.cursor.execute(update_q, (id_cap, id_usuario))

            update_u = 'UPDATE usuarios SET capacitacion = ? WHERE id_usuario = ?'
            self.cursor.execute(update_u, (capacitacion, id_usuario))

            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al guardar la capacitacion: {e}")
            return False
        

    def crear_tabla_sustancias(self):
        query = '''
                CREATE TABLE IF NOT EXISTS sustancias
                (id_sustancia INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nivel_riesgo INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                ubicacion TEXT NOT NULL,
                fecha_vencimiento TEXT NOT NULL,
                lote TEXT
                );
                '''
        self.cursor.executescript(query)
        self.conn.commit()
        # Asegurar columna 'lote' en instalaciones existentes
        self._ensure_column('sustancias', 'lote', 'TEXT')

    # Funciones CRUD para sustancias
    def agregar_sustancia(self, name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote=None):
        """Agrega una nueva sustancia. Devuelve True/False."""
        query = '''
            INSERT INTO sustancias (name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote)
            VALUES (?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al agregar sustancia: {e}")
            return False

    def modificar_sustancia(self, id_sustancia, name=None, nivel_riesgo=None, cantidad=None, ubicacion=None, fecha_vencimiento=None, lote=None):
        """Modifica los campos proporcionados de la sustancia indicada."""
        updates = []
        params = []
        if name is not None:
            updates.append('name = ?')
            params.append(name)
        if nivel_riesgo is not None:
            updates.append('nivel_riesgo = ?')
            params.append(nivel_riesgo)
        if cantidad is not None:
            updates.append('cantidad = ?')
            params.append(cantidad)
        if ubicacion is not None:
            updates.append('ubicacion = ?')
            params.append(ubicacion)
        if fecha_vencimiento is not None:
            updates.append('fecha_vencimiento = ?')
            params.append(fecha_vencimiento)
        if lote is not None:
            updates.append('lote = ?')
            params.append(lote)

        if not updates:
            # nothing to update
            return False

        params.append(id_sustancia)
        query = f"UPDATE sustancias SET {', '.join(updates)} WHERE id_sustancia = ?"
        try:
            self.cursor.execute(query, tuple(params))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al modificar sustancia: {e}")
            return False

    def eliminar_sustancia(self, id_sustancia):
        """Elimina la sustancia indicada por id."""
        try:
            self.cursor.execute('DELETE FROM sustancias WHERE id_sustancia = ?', (id_sustancia,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar sustancia: {e}")
            return False

    def obtener_sustancias(self):
        """Devuelve la lista de sustancias como diccionarios."""
        try:
            self.cursor.execute('SELECT id_sustancia, name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote FROM sustancias')
            rows = self.cursor.fetchall()
            result = []
            for r in rows:
                result.append({
                    'id_sustancia': r[0],
                    'name': r[1],
                    'nivel_riesgo': r[2],
                    'cantidad': r[3],
                    'ubicacion': r[4],
                    'fecha_vencimiento': r[5],
                    'lote': r[6]
                })
            return result
        except Exception as e:
            print(f"Error al obtener sustancias: {e}")
            return []

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
                capacitacion_acc TEXT,
                estado TEXT NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                FOREIGN KEY (capacitacion_acc) REFERENCES usuarios(capacitacion)
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
        query = "SELECT username, cedula, password, nacimiento, mail, role, nivel_autorizacion, capacitacion FROM usuarios WHERE cedula = ? LIMIT 1"
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
            'role': r[5],
            'nivel_autorizacion': r[6],
            'capacitacion': r[7]
        }
    
    def obtener_usuarios(self):
        query = '''
                SELECT id_usuario, username FROM usuarios
                '''
        self.cursor.execute(query)
        try:
            usuarios = self.cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
    
    def obtener_id_usuario(self, cedula):
        query = "SELECT id_usuario FROM usuarios WHERE cedula = ? LIMIT 1"
        self.cursor.execute(query, (cedula,))
        r = self.cursor.fetchone()
        if not r:
            return None
        return r[0]
    
    def crear_solicitud_acceso(self, id_usuario, nivel_solicitado, motivo, fecha_solicitud, capacitacion, estado):
        query = '''
            INSERT INTO solicitudes_acceso (id_usuario, nivel_solicitado, motivo, fecha_solicitud, capacitacion_acc, estado)
            VALUES (?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (id_usuario, nivel_solicitado, motivo, fecha_solicitud, capacitacion, estado))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al crear solicitud de acceso: {e}")
            return False
        
    def obtener_solicitudes_acceso(self):
        query = '''
            SELECT id_solicitud_a, username, nivel_solicitado, motivo, fecha_solicitud, capacitacion_acc, estado
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
                'nivel_solicitado': row[2],
                'motivo': row[3],
                'fecha_solicitud': row[4],
                'capacitacion_acc': row[5],
                'estado': row[6]
            })
        
        return solicitudes
    
    def actualizar_estado_solicitud_acceso(self, id_solicitud, nuevo_estado):
        try:
            query = "UPDATE solicitudes_acceso SET estado = ? WHERE id_solicitud_a = ?"
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
        
    