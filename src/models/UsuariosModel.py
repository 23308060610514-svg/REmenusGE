import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
    
    def email_existe(self, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID_usuario FROM usuarios WHERE Email = %s", (email,))
        existe = cursor.fetchone() is not None
        conn.close()
        return existe
        
    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """INSERT INTO usuarios (User, Email, Password, Fecha_Registro) 
                VALUES (%s, %s, %s, CURDATE())""",
                (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
        
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE Email = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['Password'].encode('utf-8')):
            return user
        return None
    
    def actualizar_ultimo_acceso(self, id_usuario):
        # Tu tabla no tiene campo ultimo_acceso, lo omitimos o lo agregamos
        pass
        
    def obtener_por_id(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT ID_usuario, User as nombre, Email as email FROM usuarios WHERE ID_usuario = %s", (id_usuario,))
        user = cursor.fetchone()
        conn.close()
        return user
