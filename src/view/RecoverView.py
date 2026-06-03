import flet as ft

def RecoverView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    
    # Campos del primer formulario (solicitar token)
    txt_email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400,
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    # Campos del segundo formulario (restablecer contraseña)
    txt_token = ft.TextField(
        label="Token de recuperación",
        prefix_icon=ft.Icons.VERIFIED_ROUNDED,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    nueva_password = ft.TextField(
        label="Nueva contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    confirmar_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    mensaje = ft.Text("", color="red", size=12)
    mensaje_exito = ft.Text("", color="green", size=12)
    
    def volver_login(e):
        page.go("/")
    
    def enviar_token(e):
        if not txt_email.value:
            mensaje.value = "⚠️ Ingresa tu correo electrónico"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
            return
        
        resultado = auth_controller.solicitar_recuperacion(txt_email.value)
        
        if resultado["success"]:
            mensaje.value = ""
            mensaje_exito.value = resultado["message"]
            txt_email.value = ""
            mostrar_formulario_restablecer()
        else:
            mensaje.value = f"✗ {resultado['message']}"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
    
    def cambiar_contraseña(e):
        if not txt_token.value:
            mensaje.value = "⚠️ Ingresa el token de recuperación"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
            return
        
        if not nueva_password.value or not confirmar_password.value:
            mensaje.value = "⚠️ Ingresa tu nueva contraseña"
            mensaje.color = "red"
            page.update()
            return
        
        if nueva_password.value != confirmar_password.value:
            mensaje.value = "⚠️ Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return
        
        if len(nueva_password.value) < 6:
            mensaje.value = "⚠️ La contraseña debe tener al menos 6 caracteres"
            mensaje.color = "red"
            page.update()
            return
        
        resultado = auth_controller.restablecer_contraseña(txt_token.value, nueva_password.value)
        
        if resultado["success"]:
            mensaje.value = ""
            mensaje_exito.value = resultado["message"]
            page.update()
            
            # Redirigir al login después de 2 segundos
            import asyncio
            async def redirigir():
                await asyncio.sleep(2)
                page.go("/")
            asyncio.create_task(redirigir())
        else:
            mensaje.value = f"✗ {resultado['message']}"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
    
    def mostrar_formulario_restablecer():
        contenido.controls.clear()
        contenido.controls.append(formulario_restablecer)
        page.update()
    
    # Formulario 1: Solicitar token por email
    formulario_email = ft.Column(
        [
            ft.Icon(ft.Icons.LOCK_RESET_ROUNDED, size=60, color=ft.Colors.BLUE_600),
            ft.Text("¿Olvidaste tu contraseña?", size=28, weight="bold", color=ft.Colors.BLUE_800),
            ft.Text("Ingresa tu correo y te enviaremos un token", 
                    size=14, color=ft.Colors.GREY_600),
            ft.Container(height=20),
            txt_email,
            mensaje,
            mensaje_exito,
            ft.Container(height=10),
            ft.ElevatedButton(
                "ENVIAR TOKEN",
                width=250,
                height=45,
                on_click=enviar_token,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_600,
                    color=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=3,
                    text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD, letter_spacing=1),
                ),
            ),
            ft.TextButton("← Volver al inicio de sesión", on_click=volver_login)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Formulario 2: Restablecer contraseña con token
    formulario_restablecer = ft.Column(
        [
            ft.Icon(ft.Icons.VERIFIED_ROUNDED, size=60, color=ft.Colors.GREEN_600),
            ft.Text("Restablecer contraseña", size=28, weight="bold", color=ft.Colors.BLUE_800),
            ft.Text("Ingresa el token y tu nueva contraseña", 
                    size=14, color=ft.Colors.GREY_600),
            ft.Container(height=20),
            txt_token,
            ft.Container(height=10),
            ft.Text("Nueva contraseña", size=14, weight="bold", color=ft.Colors.BLUE_800),
            nueva_password,
            confirmar_password,
            mensaje,
            mensaje_exito,
            ft.Container(height=10),
            ft.ElevatedButton(
                "CAMBIAR CONTRASEÑA",
                width=250,
                height=45,
                on_click=cambiar_contraseña,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.GREEN_600,
                    color=ft.Colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=3,
                    text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD, letter_spacing=1),
                ),
            ),
            ft.TextButton("← Volver al inicio de sesión", on_click=volver_login)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Contenedor principal
    contenido = ft.Column([formulario_email], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # También necesitas agregar el método restablecer_contraseña a tu AuthController
    # Si no lo tienes, agrégalo:
    """
    def restablecer_contraseña(self, token, nueva_password):
        # Verificar token y actualizar contraseña
        # Este método debe implementarse en UsuariosController.py
        pass
    """
    
    return ft.View(
        route="/recover",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Recuperar Contraseña", size=20, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            center_title=True,
            elevation=2,
            leading=ft.IconButton(
                ft.Icons.ARROW_BACK_ROUNDED, 
                on_click=volver_login,
                icon_color=ft.Colors.WHITE,
            )
        ),
        controls=[contenido]
    )
