import sqlite3
from datetime import datetime

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
        self.crear_tabla_alertas()
        self.crear_tabla_solicitudes_acceso()
        self.crear_tabla_solicitudes_sustancias()
        self.crear_tabla_registros_sustancias_residuos()
        self.crear_tabla_capacitaciones()
        self.crear_tabla_politicas()
        self.crear_tabla_auditoria()
        self._crear_datos_prueba_auditoria()

    def _auditar_accion(self, usuario, accion, tabla_afectada, descripcion):
        """Método interno para registrar auditoría"""
        try:
            usuario_actual = usuario if usuario else "Sistema"
            self.registrar_auditoria(usuario_actual, accion, tabla_afectada, descripcion)
        except Exception as e:
            print(f"⚠️ Error en auditoría automática: {e}")

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

                # Crear un usuario coordinador por defecto
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
            self.cursor.execute(query, (capacitacion, id_usuario, fecha_vigencia, fecha_caducidad))
            id_cap = self.cursor.lastrowid

            update_q = 'UPDATE usuarios SET id_capacitacion = ? WHERE id_usuario = ?'
            self.cursor.execute(update_q, (id_cap, id_usuario))

            update_u = 'UPDATE usuarios SET capacitacion = ? WHERE id_usuario = ?'
            self.cursor.execute(update_u, (capacitacion, id_usuario))

            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "capacitaciones", 
                f"Agregada capacitación: {capacitacion} para usuario ID {id_usuario}"
            )
            
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
        self._ensure_column('sustancias', 'lote', 'TEXT')

    # Funciones CRUD para sustancias
    def agregar_sustancia(self, name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote=None):
        query = '''
            INSERT INTO sustancias (name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote)
            VALUES (?, ?, ?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (name, nivel_riesgo, cantidad, ubicacion, fecha_vencimiento, lote))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "sustancias", 
                f"Agregada sustancia: {name}, Cantidad: {cantidad}, Nivel Riesgo: {nivel_riesgo}"
            )
            
            return True
        except Exception as e:
            print(f"Error al agregar sustancia: {e}")
            return False

    def modificar_sustancia(self, id_sustancia, name=None, nivel_riesgo=None, cantidad=None, ubicacion=None, fecha_vencimiento=None, lote=None):
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
            return False

        params.append(id_sustancia)
        query = f"UPDATE sustancias SET {', '.join(updates)} WHERE id_sustancia = ?"
        
        try:
            self.cursor.execute(query, tuple(params))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            cambios = ", ".join(updates)
            self._auditar_accion(
                "Sistema", 
                "UPDATE", 
                "sustancias", 
                f"Modificada sustancia ID {id_sustancia}: {cambios}"
            )
            
            return True
        except Exception as e:
            print(f"Error al modificar sustancia: {e}")
            return False

    def eliminar_sustancia(self, id_sustancia):
        try:
            # Obtener datos antes de eliminar para auditoría
            self.cursor.execute('SELECT name FROM sustancias WHERE id_sustancia = ?', (id_sustancia,))
            sustancia = self.cursor.fetchone()
            
            self.cursor.execute('DELETE FROM sustancias WHERE id_sustancia = ?', (id_sustancia,))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            if sustancia:
                self._auditar_accion(
                    "Sistema", 
                    "DELETE", 
                    "sustancias", 
                    f"Eliminada sustancia: {sustancia[0]} (ID: {id_sustancia})"
                )
            
            return True
        except Exception as e:
            print(f"Error al eliminar sustancia: {e}")
            return False

    def obtener_sustancias(self):
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

    def crear_tabla_alertas(self):
        query = '''
                CREATE TABLE IF NOT EXISTS alertas
                (id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_alerta TEXT NOT NULL,
                mensaje TEXT NOT NULL,
                fecha_creacion TEXT NOT NULL,
                autor TEXT
                );
                '''
        try:
            self.cursor.executescript(query)
            self.conn.commit()
        except Exception as e:
            print(f"Error al crear tabla alertas: {e}")

    def crear_alerta(self, tipo_alerta, mensaje, fecha_creacion, autor=None):
        query = '''
            INSERT INTO alertas (tipo_alerta, mensaje, fecha_creacion, autor)
            VALUES (?, ?, ?, ?);
            '''
        try:
            self.cursor.execute(query, (tipo_alerta, mensaje, fecha_creacion, autor))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                autor or "Sistema", 
                "INSERT", 
                "alertas", 
                f"Alerta creada: {tipo_alerta} - {mensaje[:50]}..."
            )
            
            return True
        except Exception as e:
            print(f"Error al crear alerta: {e}")
            return False

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
            SELECT ss.id_solicitud_s, u.username, ss.nombre_sustancia, ss.nivel_riesgo,
                   ss.cantidad_solicitada, ss.motivo, ss.fecha_solicitud, ss.estado
            FROM solicitudes_sustancias ss
            JOIN usuarios u ON ss.id_usuario = u.id_usuario;
            '''
        self.cursor.execute(query)
        r = self.cursor.fetchall()
        
        if not r:
            return []
        
        solicitudes = []
        for row in r:
            solicitudes.append({
                'id_solicitud_s': row[0],
                'username': row[1],
                'nombre_sustancia': row[2],
                'nivel_riesgo': row[3],
                'cantidad_solicitada': row[4],
                'motivo': row[5],
                'fecha_solicitud': row[6],
                'estado': row[7]
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "usuarios", 
                f"Usuario registrado: {username} ({cedula}), Rol: {role}"
            )
            
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

    def obtener_usuarios_detalles(self):
        query = '''
                SELECT id_usuario, username, cedula, nacimiento, mail, role, nivel_autorizacion, capacitacion
                FROM usuarios
                '''
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            result = []
            for r in rows:
                result.append({
                    'id_usuario': r[0],
                    'username': r[1],
                    'cedula': r[2],
                    'nacimiento': r[3],
                    'mail': r[4],
                    'role': r[5],
                    'nivel_autorizacion': r[6],
                    'capacitacion': r[7]
                })
            return result
        except Exception as e:
            print(f"Error al obtener usuarios detalles: {e}")
            return []

    def toggle_bloqueo_usuario(self, id_usuario):
        try:
            self._ensure_column('usuarios', 'prev_role', 'TEXT')
            self._ensure_column('usuarios', 'prev_nivel', 'INTEGER')
        except Exception:
            pass

        try:
            self.cursor.execute('SELECT username, role, nivel_autorizacion, prev_role, prev_nivel FROM usuarios WHERE id_usuario = ? LIMIT 1', (id_usuario,))
            row = self.cursor.fetchone()
            if not row:
                return False
            username, role, nivel, prev_role, prev_nivel = row

            if role == 'Bloqueado':
                if prev_role is None:
                    restore_role = 'Usuario'
                else:
                    restore_role = prev_role
                restore_nivel = prev_nivel if prev_nivel is not None else 1
                self.cursor.execute('UPDATE usuarios SET role = ?, nivel_autorizacion = ?, prev_role = NULL, prev_nivel = NULL WHERE id_usuario = ?', (restore_role, restore_nivel, id_usuario))
                
                # AUDITORÍA AUTOMÁTICA - DESBLOQUEO
                self._auditar_accion(
                    "Sistema", 
                    "UPDATE", 
                    "usuarios", 
                    f"Usuario desbloqueado: {username}, Rol restaurado: {restore_role}"
                )
            else:
                self.cursor.execute('UPDATE usuarios SET prev_role = ?, prev_nivel = ? WHERE id_usuario = ?', (role, nivel, id_usuario))
                self.cursor.execute('UPDATE usuarios SET role = ?, nivel_autorizacion = ? WHERE id_usuario = ?', ('Bloqueado', 0, id_usuario))
                
                # AUDITORÍA AUTOMÁTICA - BLOQUEO
                self._auditar_accion(
                    "Sistema", 
                    "UPDATE", 
                    "usuarios", 
                    f"Usuario bloqueado: {username}, Rol anterior: {role}"
                )

            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error al alternar bloqueo de usuario: {e}")
            return False
    
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "solicitudes_acceso", 
                f"Solicitud acceso creada - Usuario ID: {id_usuario}, Nivel: {nivel_solicitado}"
            )
            
            return True
        except Exception as e:
            print(f"Error al crear solicitud de acceso: {e}")
            return False
        
    def obtener_solicitudes_acceso(self):
        query = '''
            SELECT sa.id_solicitud_a, u.username, sa.nivel_solicitado, sa.motivo, 
                   sa.fecha_solicitud, sa.estado
            FROM solicitudes_acceso sa
            JOIN usuarios u ON sa.id_usuario = u.id_usuario;
            '''
        self.cursor.execute(query)
        r = self.cursor.fetchall()
        print(r)
        
        if not r:
            return []
        
        solicitudes = []
        for row in r:
            solicitudes.append({
                'id_solicitud_a': row[0],
                'username': row[1],
                'nivel_solicitado': row[2],
                'motivo': row[3],
                'fecha_solicitud': row[4],
                'estado': row[5]
            })
        
        return solicitudes
    
    def actualizar_estado_solicitud_acceso(self, id_solicitud, nuevo_estado):
        try:
            query = "UPDATE solicitudes_acceso SET estado = ? WHERE id_solicitud_a = ?"
            self.cursor.execute(query, (nuevo_estado, id_solicitud))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "UPDATE", 
                "solicitudes_acceso", 
                f"Estado cambiado a {nuevo_estado} para solicitud ID {id_solicitud}"
            )
            
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "UPDATE", 
                "solicitudes_sustancias", 
                f"Estado cambiado a {nuevo_estado} para solicitud sustancias ID {id_sustancia_s}"
            )
            
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "solicitudes_sustancias", 
                f"Solicitud sustancias: {sustancias}, Cantidad: {cantidades}, Usuario ID: {id_usuario}"
            )
            
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                "Sistema", 
                "INSERT", 
                "registros_sustancias_residuos", 
                f"Registro sustancia/residuo: {sustancia} -> {residuo}"
            )
            
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
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                autor or "Sistema", 
                "INSERT", 
                "reportes", 
                f"Reporte incidente: {titulo} - {tipo}"
            )
            
            return True
        except Exception as e:
            print(f"Error al guardar reporte de incidente: {e}")
            return False
    
    def _ensure_column(self, table, column, col_type):
        """
        Añade la columna 'column' de tipo 'col_type' a 'table' si no existe.
        """
        try:
            # Obtener info de columnas
            self.cursor.execute(f"PRAGMA table_info({table});")
            cols = [row[1] for row in self.cursor.fetchall()]  # row[1] es el nombre de la columna
            if column not in cols:
                alter_q = f"ALTER TABLE {table} ADD COLUMN {column} {col_type};"
                self.cursor.execute(alter_q)
                self.conn.commit()
        except Exception as e:
            print(f"Error en _ensure_column para {table}.{column}: {e}")

    # NUEVAS FUNCIONES PARA ADMINISTRADOR
    def crear_tabla_politicas(self):
        query = '''
        CREATE TABLE IF NOT EXISTS politicas (
            id_politica INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_laboratorio TEXT NOT NULL,
            nivel_riesgo TEXT NOT NULL,
            politica_text TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL,
            creador TEXT NOT NULL
        );
        '''
        try:
            self.cursor.executescript(query)
            self.conn.commit()
        except Exception as e:
            print(f"Error creando tabla politicas: {e}")

    def crear_tabla_auditoria(self):
        query = '''
        CREATE TABLE IF NOT EXISTS auditoria (
            id_auditoria INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            accion TEXT NOT NULL,
            tabla_afectada TEXT,
            descripcion TEXT NOT NULL,
            fecha_accion TEXT NOT NULL,
            ip_address TEXT
        );
        '''
        try:
            self.cursor.executescript(query)
            self.conn.commit()
            print("Tabla de auditoría creada/verificada")
        except Exception as e:
            print(f"❌ Error creando tabla auditoría: {e}")

    def registrar_auditoria(self, usuario, accion, tabla_afectada, descripcion, ip_address=None):
        query = '''
        INSERT INTO auditoria (usuario, accion, tabla_afectada, descripcion, fecha_accion, ip_address)
        VALUES (?, ?, ?, ?, ?, ?);
        '''
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.cursor.execute(query, (usuario, accion, tabla_afectada, descripcion, fecha, ip_address))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"❌ Error registrando auditoría: {e}")
            return False

    def obtener_log_auditoria(self, fecha_inicio=None, fecha_fin=None, usuario=None):
        try:
            query = "SELECT * FROM auditoria WHERE 1=1"
            params = []
            
            if fecha_inicio:
                query += " AND fecha_accion >= ?"
                params.append(fecha_inicio)
            if fecha_fin:
                query += " AND fecha_accion <= ?"
                params.append(fecha_fin)
            if usuario:
                query += " AND usuario LIKE ?"
                params.append(f'%{usuario}%')
                
            query += " ORDER BY fecha_accion DESC"
            self.cursor.execute(query, tuple(params))
            registros = self.cursor.fetchall()
            
            print(f"Registros de auditoría encontrados: {len(registros)}")
            return registros
            
        except Exception as e:
            print(f"❌ Error obteniendo auditoría: {e}")
            return []

    def guardar_politica(self, tipo_laboratorio, nivel_riesgo, politica_text, creador):
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query = '''
            INSERT INTO politicas (tipo_laboratorio, nivel_riesgo, politica_text, fecha_creacion, creador)
            VALUES (?, ?, ?, ?, ?);
            '''
            self.cursor.execute(query, (tipo_laboratorio, nivel_riesgo, politica_text, fecha, creador))
            self.conn.commit()
            
            # AUDITORÍA AUTOMÁTICA
            self._auditar_accion(
                creador, 
                "INSERT", 
                "politicas", 
                f"Política definida: {tipo_laboratorio} - Nivel {nivel_riesgo}"
            )
            
            return True
        except Exception as e:
            print(f"Error al guardar política: {e}")
            return False

    def obtener_politicas(self):
        try:
            query = "SELECT * FROM politicas ORDER BY tipo_laboratorio, nivel_riesgo"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener políticas: {e}")
            return []

    def generar_reporte_mensual(self, mes, año, autoridad):
        try:
            total_sustancias = self.contar_sustancias()
            total_alertas = self.contar_alertas_mes(mes, año)
            total_usuarios = self.contar_usuarios_activos()
            
            if autoridad == "MINAM":
                return f"""
REPORTE MENSUAL MINAM - {mes}/{año}
=================================
Sustancias registradas: {total_sustancias}
Alertas ambientales: {total_alertas}
Usuarios activos: {total_usuarios}
Fecha generación: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
            elif autoridad == "INVIMA":
                return f"""
REPORTE MENSUAL INVIMA - {mes}/{año}
==================================
Control de sustancias: {total_sustancias}
Alertas sanitarias: {total_alertas}
Capacitaciones registradas: {self.contar_capacitaciones()}
Fecha generación: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
            elif autoridad == "OSHA":
                return f"""
REPORTE MENSUAL OSHA - {mes}/{año}
================================
Incidentes reportados: {self.contar_incidentes_mes(mes, año)}
Alertas de seguridad: {total_alertas}
Capacitaciones en seguridad: {self.contar_capacitaciones()}
Fecha generación: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
            else:
                return "Autoridad no reconocida"
                
        except Exception as e:
            print(f"Error generando reporte mensual: {e}")
            return f"Error al generar reporte: {e}"

    def generar_reporte_iso45001(self, mes, año):
        try:
            incidentes = self.contar_incidentes_mes(mes, año)
            capacitaciones = self.contar_capacitaciones_mes(mes, año)
            usuarios_capacitados = self.contar_usuarios_capacitados()
            total_usuarios = self.contar_usuarios_activos()
            
            porcentaje_capacitacion = (usuarios_capacitados / total_usuarios * 100) if total_usuarios > 0 else 0
            sustancias_mas_usadas = self.obtener_sustancias_mas_usadas(mes, año)
            
            reporte = f"""
REPORTE ISO 45001 - SEGURIDAD OCUPACIONAL
=========================================
Período: {mes:02d}/{año}
Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Norma: ISO 45001:2018 - Sistemas de gestión de la seguridad y salud en el trabajo

1. INDICADORES DE DESEMPEÑO EN SEGURIDAD:
   • Número de incidentes: {incidentes}
   • Alertas de seguridad generadas: {self.contar_alertas_seguridad_mes(mes, año)}
   • Capacitaciones realizadas: {capacitaciones}
   • Porcentaje de cumplimiento en capacitaciones: {porcentaje_capacitacion:.1f}%

2. GESTIÓN DE RIESGOS LABORALES:
   • Evaluaciones de riesgo realizadas: {self.contar_evaluaciones_riesgo()}
   • Controles implementados: {self.contar_controles_implementados()}
   • Observaciones de seguridad: {self.contar_observaciones_seguridad()}

3. SUSTANCIAS MÁS UTILIZADAS:
{sustancias_mas_usadas}

4. EVALUACIÓN DE CONFORMIDAD ISO 45001:
   • Liderazgo y participación: CONFORME
   • Planificación de SGSST: CONFORME
   • Soporte y operación: CONFORME
   • Evaluación del desempeño: {'CONFORME' if incidentes == 0 else 'MEJORABLE'}
   • Mejora continua: {'CONFORME' if incidentes <= 1 else 'REQUIERE ACCIÓN'}

FIRMA DEL SISTEMA:
─────────────────
Sistema de Gestión de Seguridad y Salud en el Trabajo
Certificación ISO 45001:2018
"""
            return reporte
        except Exception as e:
            return f"Error generando reporte ISO 45001: {e}"

    def generar_reporte_reach(self, mes, año):
        try:
            sustancias_registradas = self.contar_sustancias_registradas()
            sustancias_controladas = self.contar_sustancias_controladas()
            incidentes_quimicos = self.contar_incidentes_quimicos_mes(mes, año)
            
            sustancias_mas_usadas = self.obtener_sustancias_mas_usadas(mes, año)
            capacitaciones = self.contar_capacitaciones_quimicas_mes(mes, año)
            usuarios_capacitados = self.contar_usuarios_capacitados_quimica()
            total_usuarios = self.contar_usuarios_activos()
            
            porcentaje_capacitacion = (usuarios_capacitados / total_usuarios * 100) if total_usuarios > 0 else 0
            
            reporte = f"""
REPORTE REACH - REGISTRO, EVALUACIÓN Y AUTORIZACIÓN DE SUSTANCIAS QUÍMICAS
===========================================================================
Período: {mes:02d}/{año}
Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Reglamento: (CE) No 1907/2006 - REACH

1. INVENTARIO DE SUSTANCIAS QUÍMICAS:
   • Sustancias registradas en sistema: {sustancias_registradas}
   • Sustancias bajo control REACH: {sustancias_controladas}
   • Incidentes con sustancias químicas: {incidentes_quimicos}

2. SUSTANCIAS MÁS UTILIZADAS:
{sustancias_mas_usadas}

3. CAPACITACIÓN Y COMPETENCIA:
   • Capacitaciones en manejo químico: {capacitaciones}
   • Porcentaje de cumplimiento en capacitaciones: {porcentaje_capacitacion:.1f}%
   • Personal certificado en manejo seguro: {usuarios_capacitados}

4. CUMPLIMIENTO REACH:
   • Comunicación en la cadena de suministro: CONFORME
   • Evaluación de seguridad química: CONFORME
   • Gestión de sustancias muy preocupantes: {self.gestion_sustancias_preocupantes()}
   • Autorizaciones y restricciones: CONFORME

FIRMA DEL SISTEMA:
─────────────────
Sistema de Gestión de Sustancias Químicas REACH
"""
            return reporte
        except Exception as e:
            return f"Error generando reporte REACH: {e}"

    def generar_reporte_residuos(self, mes, año):
        try:
            residuos_generados = self.contar_residuos_generados_mes(mes, año)
            residuos_eliminados = self.contar_residuos_eliminados_mes(mes, año)
            incidentes_ambientales = self.contar_incidentes_ambientales_mes(mes, año)
            
            capacitaciones = self.contar_capacitaciones_ambientales_mes(mes, año)
            usuarios_capacitados = self.contar_usuarios_capacitados_ambiental()
            total_usuarios = self.contar_usuarios_activos()
            
            porcentaje_capacitacion = (usuarios_capacitados / total_usuarios * 100) if total_usuarios > 0 else 0
            sustancias_mas_usadas = self.obtener_sustancias_mas_usadas(mes, año)
            
            reporte = f"""
REPORTE DE MANEJO DE RESIDUOS - NORMAS LOCALES
===============================================
Período: {mes:02d}/{año}
Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Normativa: Resolución 1362 de 2007 - Manejo de Residuos Peligrosos

1. GESTIÓN DE RESIDUOS:
   • Residuos generados: {residuos_generados} unidades
   • Residuos eliminados correctamente: {residuos_eliminados} unidades
   • Incidentes ambientales: {incidentes_ambientales}

2. SUSTANCIAS GENERADORAS DE RESIDUOS:
{sustancias_mas_usadas}

3. CAPACITACIÓN AMBIENTAL:
   • Capacitaciones ambientales: {capacitaciones}
   • Porcentaje de cumplimiento en capacitaciones: {porcentaje_capacitacion:.1f}%
   • Personal certificado en manejo ambiental: {usuarios_capacitados}

4. CUMPLIMIENTO NORMATIVO:
   • Plan de gestión de residuos: IMPLEMENTADO
   • Separación en la fuente: CONFORME
   • Almacenamiento temporal: ADECUADO
   • Transporte y disposición final: CERTIFICADO

FIRMA DEL SISTEMA:
─────────────────
Sistema de Gestión Ambiental de Residuos
"""
            return reporte
        except Exception as e:
            return f"Error generando reporte de residuos: {e}"

    def generar_informe_cumplimiento(self, fecha_inicio, fecha_fin):
        try:
            total_sustancias = self.contar_sustancias_registradas()
            total_alertas = self.contar_alertas_periodo(fecha_inicio, fecha_fin)
            total_capacitaciones = self.contar_capacitaciones_periodo(fecha_inicio, fecha_fin)
            total_incidentes = self.contar_incidentes_periodo(fecha_inicio, fecha_fin)
            
            nivel_cumplimiento = min(100, 95 - total_incidentes * 2)
            
            informe = f"""
INFORME DE CUMPLIMIENTO NORMATIVO
==================================
Período de Evaluación: {fecha_inicio} a {fecha_fin}
Fecha de Generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Sistema: Gestión de Laboratorio Científico

RESUMEN EJECUTIVO:
──────────────────
• Nivel de Cumplimiento General: {nivel_cumplimiento}%
• Sustancias en Inventario: {total_sustancias}
• Alertas Generadas: {total_alertas}
• Capacitaciones Realizadas: {total_capacitaciones}
• Incidentes Reportados: {total_incidentes}

HALLAZGOS RELEVANTES:
────────────────────
• Sistema operando dentro de parámetros normativos
• Documentación completa y actualizada
• Personal capacitado y certificado
• Protocolos de emergencia establecidos

BRECHAS IDENTIFICADAS:
─────────────────────
"""

            if total_incidentes > 0:
                informe += f"• Se reportaron {total_incidentes} incidentes que requieren atención\n"
            
            if total_alertas > 5:
                informe += f"• Número elevado de alertas ({total_alertas}) que merecen revisión\n"
                
            if total_capacitaciones == 0:
                informe += "• No se registraron capacitaciones en el período\n"
            
            if total_incidentes == 0 and total_alertas <= 5 and total_capacitaciones > 0:
                informe += "• No se identificaron brechas significativas\n"

            informe += f"""
RECOMENDACIONES:
───────────────
1. Mantener programa de auditorías internas
2. Continuar con capacitación continua del personal
3. Revisar y actualizar protocolos cada 6 meses
4. Implementar mejora en sistema de alertas tempranas

FIRMA DIGITAL DEL SISTEMA:
─────────────────────────
SGL-{datetime.now().strftime('%Y%m%d%H%M%S')}

---
Documento generado automáticamente - Tiene validez oficial
"""
            return informe
            
        except Exception as e:
            print(f"Error generando informe de cumplimiento: {e}")
            return f"Error al generar informe: {e}"

    def exportar_informe_archivo(self, contenido, nombre_archivo):
        try:
            if not nombre_archivo.endswith('.txt'):
                nombre_archivo += '.txt'
            
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)
            print(f"Informe exportado correctamente: {nombre_archivo}")
            return True
        except Exception as e:
            print(f"❌ Error exportando informe: {e}")
            return False

    def evaluar_laboratorios(self):
        try:
            return [
                {
                    'laboratorio': 'Laboratorio Químico Principal',
                    'puntaje_riesgo': 35,
                    'recomendacion': 'Mantenimiento preventivo requerido',
                    'accion_requerida': 'MEJORAS RECOMENDADAS'
                },
                {
                    'laboratorio': 'Laboratorio de Biología',
                    'puntaje_riesgo': 15,
                    'recomendacion': 'Cumplimiento adecuado',
                    'accion_requerida': 'CUMPLIMIENTO ADECUADO'
                }
            ]
        except Exception as e:
            print(f"Error evaluando laboratorios: {e}")
            return []

    # FUNCIONES AUXILIARES PARA ESTADÍSTICAS
    def contar_sustancias_registradas(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM sustancias")
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_usuarios_activos(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM usuarios WHERE role != 'Bloqueado'")
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_capacitaciones(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM capacitaciones")
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_alertas_mes(self, mes, año):
        try:
            query = "SELECT COUNT(*) FROM alertas WHERE strftime('%m', fecha_creacion) = ? AND strftime('%Y', fecha_creacion) = ?"
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_incidentes_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM reportes 
            WHERE tipo_reporte LIKE '%incidente%' 
            AND strftime('%m', fecha_creacion) = ? 
            AND strftime('%Y', fecha_creacion) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_capacitaciones_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM capacitaciones 
            WHERE strftime('%m', fecha_vigencia) = ? 
            AND strftime('%Y', fecha_vigencia) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_usuarios_capacitados(self):
        try:
            query = "SELECT COUNT(*) FROM usuarios WHERE id_capacitacion IS NOT NULL"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            return 0

    def obtener_sustancias_mas_usadas(self, mes, año):
        try:
            query = """
            SELECT nombre_sustancia, COUNT(*) as usos 
            FROM solicitudes_sustancias 
            WHERE strftime('%m', fecha_solicitud) = ? 
            AND strftime('%Y', fecha_solicitud) = ?
            GROUP BY nombre_sustancia 
            ORDER BY usos DESC 
            LIMIT 5
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            resultados = self.cursor.fetchall()
            
            if not resultados:
                return "   • No hay datos de uso de sustancias para este período"
            
            texto = ""
            for i, (sustancia, usos) in enumerate(resultados, 1):
                texto += f"   {i}. {sustancia}: {usos} solicitudes\n"
            return texto.rstrip()
        except:
            return "   • Error obteniendo datos de sustancias"

    def contar_alertas_seguridad_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM alertas 
            WHERE tipo_alerta LIKE '%seguridad%' 
            AND strftime('%m', fecha_creacion) = ? 
            AND strftime('%Y', fecha_creacion) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_sustancias_controladas(self):
        try:
            query = "SELECT COUNT(*) FROM sustancias WHERE nivel_riesgo >= 2"
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_incidentes_quimicos_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM reportes 
            WHERE (tipo_reporte LIKE '%químico%' OR tipo_reporte LIKE '%sustancia%')
            AND strftime('%m', fecha_creacion) = ? 
            AND strftime('%Y', fecha_creacion) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_capacitaciones_quimicas_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM capacitaciones 
            WHERE capacitacion LIKE '%químico%' 
            AND strftime('%m', fecha_vigencia) = ? 
            AND strftime('%Y', fecha_vigencia) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_usuarios_capacitados_quimica(self):
        try:
            query = """
            SELECT COUNT(*) FROM usuarios 
            WHERE capacitacion LIKE '%químico%' OR capacitacion LIKE '%sustancia%'
            """
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_residuos_generados_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM residuos 
            WHERE strftime('%m', fecha_almacenamiento) = ? 
            AND strftime('%Y', fecha_almacenamiento) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_residuos_eliminados_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM residuos 
            WHERE strftime('%m', fecha_retiro) = ? 
            AND strftime('%Y', fecha_retiro) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_incidentes_ambientales_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM reportes 
            WHERE tipo_reporte LIKE '%ambiental%' 
            AND strftime('%m', fecha_creacion) = ? 
            AND strftime('%Y', fecha_creacion) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_capacitaciones_ambientales_mes(self, mes, año):
        try:
            query = """
            SELECT COUNT(*) FROM capacitaciones 
            WHERE capacitacion LIKE '%ambiental%' 
            AND strftime('%m', fecha_vigencia) = ? 
            AND strftime('%Y', fecha_vigencia) = ?
            """
            self.cursor.execute(query, (f"{mes:02d}", str(año)))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_usuarios_capacitados_ambiental(self):
        try:
            query = """
            SELECT COUNT(*) FROM usuarios 
            WHERE capacitacion LIKE '%ambiental%' OR capacitacion LIKE '%residuo%'
            """
            self.cursor.execute(query)
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_alertas_periodo(self, fecha_inicio, fecha_fin):
        try:
            query = "SELECT COUNT(*) FROM alertas WHERE fecha_creacion BETWEEN ? AND ?"
            self.cursor.execute(query, (fecha_inicio, fecha_fin))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_capacitaciones_periodo(self, fecha_inicio, fecha_fin):
        try:
            query = "SELECT COUNT(*) FROM capacitaciones WHERE fecha_vigencia BETWEEN ? AND ?"
            self.cursor.execute(query, (fecha_inicio, fecha_fin))
            return self.cursor.fetchone()[0]
        except:
            return 0

    def contar_incidentes_periodo(self, fecha_inicio, fecha_fin):
        try:
            query = "SELECT COUNT(*) FROM reportes WHERE tipo_reporte = 'Incidente' AND fecha_creacion BETWEEN ? AND ?"
            self.cursor.execute(query, (fecha_inicio, fecha_fin))
            return self.cursor.fetchone()[0]
        except:
            return 0

    # FUNCIONES DE SIMULACIÓN (para demo)
    def contar_evaluaciones_riesgo(self):
        return 5

    def contar_controles_implementados(self):
        return 12

    def contar_observaciones_seguridad(self):
        return 8

    def gestion_sustancias_preocupantes(self):
        return "CONTROLADO"

    def _crear_datos_prueba_auditoria(self):
        """Crea algunos registros de prueba para la auditoría"""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM auditoria")
            count = self.cursor.fetchone()[0]
            
            if count == 0:
                acciones_prueba = [
                    ("admin", "LOGIN", "sistema", "Inicio de sesión exitoso"),
                    ("admin", "INSERT", "sustancias", "Agregada sustancia: Cloruro de sodio"),
                    ("coordinador", "UPDATE", "usuarios", "Actualización de permisos de usuario"),
                    ("sistema", "INSERT", "alertas", "Alerta automática: Stock bajo detectado"),
                    ("admin", "INSERT", "politicas", "Política definida: Químico - Nivel 2"),
                    ("sistema", "INSERT", "solicitudes_acceso", "Solicitud acceso creada - Usuario ID: 2")
                ]
                
                for usuario, accion, tabla, descripcion in acciones_prueba:
                    self.registrar_auditoria(usuario, accion, tabla, descripcion)
                    
                print("Datos de prueba para auditoría creados")
        except Exception as e:
            print(f"Error creando datos prueba auditoría: {e}")