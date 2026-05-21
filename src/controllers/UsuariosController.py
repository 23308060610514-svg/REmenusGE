from models.UsuariosModel import UsuarioModel

class AuthController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def login(self, email, password):
        try:
            user_db = self.usuario_model.validar_login(email, password)

            if not user_db:
                return None, "Correo o contraseña incorrectos"

            self.usuario_model.actualizar_ultimo_acceso(user_db["id_usuario"])
        
            user_db_actualizado = self.usuario_model.obtener_por_id(user_db["id_usuario"])

            user = {
                "id_usuario": user_db_actualizado["id_usuario"],
                "nombre": user_db_actualizado["nombre"],
                "apellido": user_db_actualizado["apellido"],
                "telefono": user_db_actualizado["telefono"],
                "email": user_db_actualizado["email"],
                "fecha_registro": user_db_actualizado["fecha_registro"],
                "ultimo_acceso": user_db_actualizado["ultimo_acceso"],  
            }

            return user, "Login exitoso"
        
        except Exception as e:
            return None, f"Error en login: {str(e)}"
    
    def registrar(self, usuario_data):
        try:
            if self.usuario_model.email_existe(usuario_data.email):
                return False, "El correo electrónico ya está registrado"
            exito = self.usuario_model.registrar(usuario_data)
            
            if exito:
                return True, "Usuario registrado exitosamente"
            else:
                return False, "Error al registrar usuario"
                
        except Exception as e:
            return False, f"Error en registro: {str(e)}"

    # ========== NUEVOS MÉTODOS PARA RECUPERACIÓN DE CONTRASEÑA ==========

    def solicitar_recuperacion(self, email: str) -> dict:
        """
        Solicita recuperación de contraseña para un email
        """
        try:
            # Buscar usuario por email
            usuario = self.usuario_model.obtener_por_email(email)
            
            if not usuario:
                return {
                    "success": False,
                    "message": "No existe una cuenta con este correo electrónico"
                }
            
            # Generar token JWT
            from utils.token_utils import generate_token
            token = generate_token(usuario['id_usuario'], usuario['email'])
            
            # Enviar email de recuperación
            from utils.email_utils import send_reset_email
            email_enviado = send_reset_email(email, token, usuario['nombre'])
            
            if email_enviado:
                return {
                    "success": True,
                    "message": "Se han enviado instrucciones a tu correo electrónico"
                }
            else:
                return {
                    "success": False,
                    "message": "Error al enviar el correo. Intenta más tarde"
                }
                
        except Exception as e:
            print(f"Error en solicitar_recuperacion: {e}")
            return {
                "success": False,
                "message": f"Error al procesar la solicitud: {str(e)}"
            }

    def verificar_token_recuperacion(self, token: str) -> dict:
        """
        Verifica si un token de recuperación es válido
        """
        try:
            from utils.token_utils import verify_token
            
            payload = verify_token(token)
            
            if payload:
                return {
                    "success": True,
                    "user_id": payload.get('user_id'),
                    "email": payload.get('email')
                }
            else:
                return {
                    "success": False,
                    "message": "El enlace ha expirado o es inválido"
                }
        except Exception as e:
            print(f"Error en verificar_token_recuperacion: {e}")
            return {
                "success": False,
                "message": f"Error al verificar el token: {str(e)}"
            }

    def restablecer_contraseña(self, token: str, nueva_password: str) -> dict:
        """
        Restablece la contraseña usando un token válido
        """
        try:
            from utils.token_utils import verify_token, hash_password
            
            # Verificar token
            payload = verify_token(token)
            
            if not payload:
                return {
                    "success": False,
                    "message": "El enlace ha expirado o es inválido"
                }
            
            # Hashear nueva contraseña
            hashed_password = hash_password(nueva_password)
            
            # Actualizar en la base de datos
            usuario_id = payload.get('user_id')
            success = self.usuario_model.actualizar_password(usuario_id, hashed_password)
            
            if success:
                return {
                    "success": True,
                    "message": "Contraseña actualizada correctamente"
                }
            else:
                return {
                    "success": False,
                    "message": "Error al actualizar la contraseña"
                }
                
        except Exception as e:
            print(f"Error en restablecer_contraseña: {e}")
            return {
                "success": False,
                "message": f"Error al procesar la solicitud: {str(e)}"
            }

    def cambiar_contraseña(self, usuario_id: int, password_actual: str, nueva_password: str) -> dict:
        """
        Cambia la contraseña de un usuario (cuando ya está logueado)
        """
        try:
            # Verificar la contraseña actual
            from utils.token_utils import verify_password
            
            usuario = self.usuario_model.obtener_por_id(usuario_id)
            if not usuario:
                return {
                    "success": False,
                    "message": "Usuario no encontrado"
                }
            
            # Verificar contraseña actual
            if not verify_password(password_actual, usuario['password']):
                return {
                    "success": False,
                    "message": "Contraseña actual incorrecta"
                }
            
            # Hashear nueva contraseña
            from utils.token_utils import hash_password
            hashed_password = hash_password(nueva_password)
            
            # Actualizar contraseña
            success = self.usuario_model.actualizar_password(usuario_id, hashed_password)
            
            if success:
                return {
                    "success": True,
                    "message": "Contraseña cambiada correctamente"
                }
            else:
                return {
                    "success": False,
                    "message": "Error al cambiar la contraseña"
                }
                
        except Exception as e:
            print(f"Error en cambiar_contraseña: {e}")
            return {
                "success": False,
                "message": f"Error al procesar la solicitud: {str(e)}"
            }