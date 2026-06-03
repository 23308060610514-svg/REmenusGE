import flet as ft
import asyncio
import re

def RecoverView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    
    txt_email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400,
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
        hint_text="ejemplo@correo.com",
    )
    
    txt_token = ft.TextField(
        label="Código de verificación",
        prefix_icon=ft.Icons.VERIFIED_ROUNDED,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
        hint_text="Ingresa el código que recibiste por correo",
        max_length=32,
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
        hint_text="Mínimo 6 caracteres",
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
        hint_text="Repite tu nueva contraseña",
    )
    
    mensaje_error = ft.Text("", color=ft.Colors.RED_600, size=12, text_align=ft.TextAlign.CENTER)
    mensaje_exito = ft.Text("", color=ft.Colors.GREEN_600, size=12, text_align=ft.TextAlign.CENTER)
    
    loading_indicator = ft.ProgressRing(width=30, height=30, visible=False)
    btn_enviar_text = ft.Text("ENVIAR CÓDIGO", size=14, weight=ft.FontWeight.BOLD)
    btn_cambiar_text = ft.Text("CAMBIAR CONTRASEÑA", size=14, weight=ft.FontWeight.BOLD)
    
    def limpiar_mensajes():
        mensaje_error.value = ""
        mensaje_exito.value = ""
        page.update()
    
    def mostrar_error(mensaje: str):
        mensaje_error.value = mensaje
        mensaje_exito.value = ""
        page.update()
    
    def mostrar_exito(mensaje: str):
        mensaje_exito.value = mensaje
        mensaje_error.value = ""
        page.update()
    
    def validar_email(email: str) -> bool:
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    # ========== FUNCIONES PRINCIPALES ==========
    def volver_login(e):
        page.go("/")
    
    async def enviar_token_async(e):
        limpiar_mensajes()
        
        if not txt_email.value:
            mostrar_error("⚠️ Ingresa tu correo electrónico")
            return
        
        if not validar_email(txt_email.value):
            mostrar_error("⚠️ Ingresa un correo electrónico válido")
            return
        
        # Mostrar loading
        btn_enviar.visible = False
        loading_indicator.visible = True
        page.update()
        
        try:
            # Llamar al método correcto del controlador
            resultado = auth_controller.solicitar_recuperacion(txt_email.value)
            
            if resultado.get("success"):
                mostrar_exito(resultado["message"])
                txt_email.value = ""
                # Cambiar al formulario de restablecimiento
                cambiar_a_formulario_restablecer()
            else:
                mostrar_error(resultado.get("message", "Error al enviar el código"))
        except Exception as ex:
            mostrar_error(f"Error: {str(ex)}")
        finally:
            btn_enviar.visible = True
            loading_indicator.visible = False
            page.update()
    
    def enviar_token(e):
        asyncio.create_task(enviar_token_async(e))
    
    async def cambiar_contraseña_async(e):
        limpiar_mensajes()
        
        if not txt_token.value:
            mostrar_error("⚠️ Ingresa el código de verificación")
            return
        
        if not nueva_password.value:
            mostrar_error("⚠️ Ingresa tu nueva contraseña")
            return
        
        if nueva_password.value != confirmar_password.value:
            mostrar_error("⚠️ Las contraseñas no coinciden")
            return
        
        # Mostrar loading
        btn_cambiar.visible = False
        loading_indicator.visible = True
        page.update()
        
        try:
            resultado = auth_controller.restablecer_contraseña(txt_token.value, nueva_password.value)
            
            if resultado.get("success"):
                mostrar_exito(resultado["message"])
                page.update()
                
                # Redirigir después de 2.5 segundos
                await asyncio.sleep(2.5)
                page.go("/")
            else:
                mostrar_error(resultado.get("message", "Error al cambiar la contraseña"))
        except Exception as ex:
            mostrar_error(f"Error: {str(ex)}")
        finally:
            btn_cambiar.visible = True
            loading_indicator.visible = False
            page.update()
    
    def cambiar_contraseña(e):
        asyncio.create_task(cambiar_contraseña_async(e))
    
    def cambiar_a_formulario_restablecer():
        contenido.controls.clear()
        contenido.controls.append(formulario_restablecer)
        page.update()
    
    def volver_formulario_email(e):
        contenido.controls.clear()
        contenido.controls.append(formulario_email)
        # Limpiar campos del formulario de restablecimiento
        txt_token.value = ""
        nueva_password.value = ""
        confirmar_password.value = ""
        limpiar_mensajes()
        page.update()
    
    btn_enviar = ft.ElevatedButton(
        content=btn_enviar_text,
        width=250,
        height=45,
        on_click=enviar_token,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=3,
        ),
    )
    
    btn_cambiar = ft.ElevatedButton(
        content=btn_cambiar_text,
        width=250,
        height=45,
        on_click=cambiar_contraseña,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=3,
        ),
    )
    
    formulario_email = ft.Column(
        [
            ft.Icon(ft.Icons.LOCK_RESET_ROUNDED, size=60, color=ft.Colors.BLUE_600),
            ft.Text("¿Olvidaste tu contraseña?", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
            ft.Text("Ingresa tu correo y te enviaremos un código de verificación", 
                    size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
            ft.Container(height=30),
            txt_email,
            ft.Container(height=10),
            ft.Row(
                [btn_enviar, loading_indicator],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            ft.Container(height=15),
            mensaje_error,
            mensaje_exito,
            ft.Container(height=20),
            ft.TextButton(
                content=ft.Row(
                    [ft.Icon(ft.Icons.ARROW_BACK, size=16), ft.Text("Volver al inicio de sesión")],
                    spacing=5,
                ),
                on_click=volver_login,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
    )
    
    formulario_restablecer = ft.Column(
        [
            ft.Icon(ft.Icons.VERIFIED_ROUNDED, size=60, color=ft.Colors.GREEN_600),
            ft.Text("Restablecer contraseña", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_800),
            ft.Text("Ingresa el código que recibiste por correo y tu nueva contraseña", 
                    size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
            ft.Container(height=30),
            txt_token,
            ft.Container(height=15),
            nueva_password,
            ft.Container(height=10),
            confirmar_password,
            ft.Container(height=15),
            ft.Row(
                [btn_cambiar, loading_indicator],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            ft.Container(height=15),
            mensaje_error,
            mensaje_exito,
            ft.Container(height=20),
            ft.TextButton(
                content=ft.Row(
                    [ft.Icon(ft.Icons.ARROW_BACK, size=16), ft.Text("¿No recibiste el código? Volver")],
                    spacing=5,
                ),
                on_click=volver_formulario_email,
            ),
            ft.TextButton(
                content=ft.Row(
                    [ft.Icon(ft.Icons.LOGIN, size=16), ft.Text("Volver al inicio de sesión")],
                    spacing=5,
                ),
                on_click=volver_login,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
    )
    
    contenido = ft.Column(
        [formulario_email],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )
    
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
                tooltip="Volver",
            )
        ),
        controls=[contenido],
    )
