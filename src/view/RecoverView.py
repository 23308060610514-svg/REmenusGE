import flet as ft
import asyncio

def RecoverView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    
    correo_field = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400,
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
    )
    
    mensaje = ft.Text("", color="red", size=12)
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=3000,
        )
        page.snack_bar.open = True
        page.update()
    
    def enviar_instrucciones(e):
        if not correo_field.value:
            mensaje.value = "⚠️ Por favor, ingrese su correo electrónico"
            mensaje.color = "red"
            page.update()
            return
        
        resultado = auth_controller.solicitar_recuperacion(correo_field.value)
        
        if resultado["success"]:
            mensaje.value = "✓ " + resultado["message"]
            mensaje.color = "green"
            mostrar_snackbar("✓ " + resultado["message"], ft.Colors.GREEN_600)
            correo_field.value = ""
            page.update()
        else:
            mensaje.value = "✗ " + resultado["message"]
            mensaje.color = "red"
            page.update()
    
    btn_enviar = ft.ElevatedButton(
        "ENVIAR INSTRUCCIONES",
        width=250,
        height=45,
        on_click=enviar_instrucciones,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    btn_volver = ft.TextButton(
        "← Volver al inicio de sesión",
        on_click=lambda _: page.go("/"),
    )
    
    correo_field.on_submit = enviar_instrucciones
    
    # ✅ CORRECTO - Sin duplicar controls
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
                on_click=lambda _: page.go("/"),
                icon_color=ft.Colors.WHITE,
            )
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_RESET_ROUNDED, size=60, color=ft.Colors.BLUE_600),
                    ft.Text("¿Olvidaste tu contraseña?", size=28, weight="bold", color=ft.Colors.BLUE_800),
                    ft.Text("Te enviaremos instrucciones a tu correo", size=14, color=ft.Colors.GREY_600),
                    ft.Container(height=30),
                    correo_field,
                    ft.Container(height=20),
                    mensaje,
                    ft.Container(height=10),
                    btn_enviar,
                    ft.Container(height=20),
                    btn_volver,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            )
        ],
    )