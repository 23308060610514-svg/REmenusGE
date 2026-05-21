import flet as ft
import re
from pydantic import ValidationError
from models.schemasModel import UsuarioSchema  

def RegisterView(page: ft.Page, auth_controller):
    
    nombre = ft.TextField(
        label="Nombre(s)", 
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        width=400, 
        border_radius=10
    )
    
    apellido = ft.TextField(
        label="Apellidos", 
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        width=400, 
        border_radius=10
    )
    
    telefono = ft.TextField(
        label="Teléfono", 
        prefix_icon=ft.Icons.PHONE_ROUNDED,
        width=400, 
        border_radius=10, 
        keyboard_type=ft.KeyboardType.PHONE
    )
    
    email = ft.TextField(
        label="Correo electrónico", 
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400, 
        border_radius=10, 
        keyboard_type=ft.KeyboardType.EMAIL
    )
    
    password = ft.TextField(
        label="Contraseña", 
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True, 
        can_reveal_password=True, 
        width=400, 
        border_radius=10
    )
    
    confirm_password = ft.TextField(
        label="Confirmar contraseña", 
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True, 
        can_reveal_password=True, 
        width=400, 
        border_radius=10
    )
    
    mensaje = ft.Text("", color="red", size=12)
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def registrar_click(e):
        if not all([nombre.value, apellido.value, email.value, password.value]):
            mensaje.value = "Nombre, Apellido, Email y Contraseña son obligatorios"
            mensaje.color = "red"
            page.update()
            return
        
        if password.value != confirm_password.value:
            mensaje.value = "Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return

        try:
            usuario_data = UsuarioSchema(
                nombre=nombre.value,
                apellido=apellido.value,
                telefono=telefono.value if telefono.value else None,
                email=email.value,
                password=password.value
            )
        except ValidationError as ex:
            mensaje.value = f"Error: {ex.errors()[0]['msg']}"
            mensaje.color = "red"
            page.update()
            return

        exito, msg = auth_controller.registrar(usuario_data)
        
        if exito:
            mostrar_snackbar("¡Registro exitoso! Ahora inicia sesión", ft.Colors.GREEN)
            for field in [nombre, apellido, telefono, email, password, confirm_password]:
                field.value = ""
            mensaje.value = ""
            page.update()
            page.go("/")
        else:
            mensaje.value = msg or "Error al registrar usuario"
            mensaje.color = "red"
            page.update()

    btn_registrar = ft.ElevatedButton(
        "Registrarse",
        width=250,
        on_click=registrar_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_500,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    btn_login = ft.TextButton("¿Ya tienes cuenta? Inicia sesión", on_click=lambda _: page.go("/"))
    
    return ft.View(
        route="/register",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Registro de Usuario"),  # ✅ CAMBIADO
            bgcolor=ft.Colors.BLUE_800,
            color=ft.Colors.WHITE,
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"))
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Crear Nueva Cuenta", size=20, weight="bold"),
                    ft.Container(height=10),
                    nombre, apellido, telefono, email, password, confirm_password,
                    mensaje,
                    ft.Container(height=5),
                    btn_registrar,
                    btn_login
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=10
            )
        ]
    )