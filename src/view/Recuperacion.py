import flet as ft

def ForgotPasswordView(page: ft.Page, auth_controller):
    txt_email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        width=400,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    txt_token = ft.TextField(
        label="Token de recuperación",
        prefix_icon=ft.Icons.VERIFIED,
        width=400,
        border_radius=10
    )
    
    nueva_password = ft.TextField(
        label="Nueva contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10
    )
    
    confirmar_password = ft.TextField(
        label="Confirmar contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10
    )
    
    mensaje = ft.Text("", color="red", size=12)
    mensaje_exito = ft.Text("", color="green", size=12)

    def volver_login(e):
        page.go("/")
    
    def enviar_token(e):
        if not txt_email.value:
            mensaje.value = "Ingresa tu correo electrónico"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
            return
        
        exito, msg = auth_controller.solicitar_recuperacion(txt_email.value)
        
        if exito:
            mensaje.value = ""
            mensaje_exito.value = msg
            txt_email.value = ""
            mostrar_formulario_restablecer()
        else:
            mensaje.value = msg
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
    
    def cambiar_contraseña(e):
        if not txt_token.value:
            mensaje.value = "Ingresa el token"
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()
            return
        
        if not nueva_password.value or not confirmar_password.value:
            mensaje.value = "Ingresa tu nueva contraseña"
            mensaje.color = "red"
            page.update()
            return
        
        if nueva_password.value != confirmar_password.value:
            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return
        
        if len(nueva_password.value) < 6:
            mensaje.value = "La contraseña debe tener al menos 6 caracteres"
            mensaje.color = "red"
            page.update()
            return
        
        exito, msg = auth_controller.reset_password(txt_token.value, nueva_password.value)
        
        if exito:
            mensaje.value = ""
            mensaje_exito.value = msg
            page.update()
                        
            def redirigir_login():
                page.go("/")
                page.after(2000, redirigir_login)
        else:
            mensaje.value = msg
            mensaje.color = "red"
            mensaje_exito.value = ""
            page.update()

    def mostrar_formulario_restablecer():
        contenido.controls.clear()
        contenido.controls.append(formulario_restablecer)
        page.update()

    formulario_email = ft.Column(
        [
            ft.Icon(ft.Icons.LOCK_RESET, size=60, color=ft.Colors.BLUE_500),
            ft.Text("¿Olvidaste tu contraseña?", size=24, weight="bold"),
            ft.Text("Ingresa tu correo y te enviaremos un token", 
                size=14, color=ft.Colors.GREY_600),
            ft.Container(height=20),
            txt_email,
            mensaje,
            mensaje_exito,
            ft.Container(height=10),
            ft.ElevatedButton(
                "Enviar token",
                width=250,
                on_click=enviar_token,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.BLUE_500,
                    color=ft.Colors.WHITE,
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
            ),
            ft.TextButton("Volver al inicio de sesión", on_click=volver_login)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True,
        spacing=10
    )

    formulario_restablecer = ft.Column(
        [
            ft.Icon(ft.Icons.VERIFIED, size=60, color=ft.Colors.BLUE_500),
            ft.Text("Restablecer contraseña", size=24, weight="bold"),
            ft.Text("Ingresa el token y tu nueva contraseña", 
                size=14, color=ft.Colors.BLACK),
            ft.Container(height=20),
            txt_token,
            ft.Container(height=10),
            ft.Text("Nueva contraseña", size=16, weight="bold"),
            nueva_password,
            confirmar_password,
            mensaje,
            mensaje_exito,
            ft.Container(height=10),
            ft.ElevatedButton(
                "Cambiar contraseña",
                width=250,
                on_click=cambiar_contraseña,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.GREEN_500,
                    color=ft.Colors.WHITE,
                    padding=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
            ),
            ft.TextButton("Volver al inicio de sesión", on_click=volver_login)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        tight=True,
        spacing=10
    )

    contenido = ft.Column([formulario_email], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    return ft.View(
        route="/forgot-password",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("CoinControl - Recuperar Contraseña"),
            bgcolor=ft.Colors.GREEN_500,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=volver_login)
        ),
        controls=[contenido]
    )