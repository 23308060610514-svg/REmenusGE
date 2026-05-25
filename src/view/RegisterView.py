import flet as ft
from pydantic import ValidationError
from models.schemasModel import UsuarioSchema  

def RegisterView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    
    nombre = ft.TextField(
        label="Nombre(s)", 
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        width=400, 
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    apellido = ft.TextField(
        label="Apellidos", 
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        width=400, 
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    telefono = ft.TextField(
        label="Teléfono", 
        prefix_icon=ft.Icons.PHONE_ROUNDED,
        width=400, 
        border_radius=12,
        keyboard_type=ft.KeyboardType.PHONE,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    email = ft.TextField(
        label="Correo electrónico", 
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400, 
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    password = ft.TextField(
        label="Contraseña", 
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True, 
        can_reveal_password=True, 
        width=400, 
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
    )
    
    confirm_password = ft.TextField(
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
    
    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def registrar_click(e):
        # Validar campos obligatorios
        if not all([nombre.value, email.value, password.value]):
            mensaje.value = "⚠️ Nombre, Email y Contraseña son obligatorios"
            mensaje.color = "red"
            page.update()
            return
        
        # Validar contraseñas
        if password.value != confirm_password.value:
            mensaje.value = "⚠️ Las contraseñas no coinciden"
            mensaje.color = "red"
            page.update()
            return
        
        # Validar longitud de contraseña
        if len(password.value) < 4:
            mensaje.value = "⚠️ La contraseña debe tener al menos 4 caracteres"
            mensaje.color = "red"
            page.update()
            return

        # Validar con Pydantic
        try:
            usuario_data = UsuarioSchema(
                nombre=nombre.value,
                apellido=apellido.value if apellido.value else None,
                telefono=telefono.value if telefono.value else None,
                email=email.value,
                password=password.value
            )
        except ValidationError as ex:
            mensaje.value = f"⚠️ {ex.errors()[0]['msg']}"
            mensaje.color = "red"
            page.update()
            return

        # Registrar usuario
        exito, msg = auth_controller.registrar(usuario_data)
        
        if exito:
            mostrar_snackbar("✓ ¡Registro exitoso! Ahora inicia sesión", ft.Colors.GREEN_600)
            # Limpiar campos
            for field in [nombre, apellido, telefono, email, password, confirm_password]:
                field.value = ""
            mensaje.value = ""
            page.update()
            # Redirigir al login
            page.go("/")
        else:
            mensaje.value = f"✗ {msg}"
            mensaje.color = "red"
            page.update()

    btn_registrar = ft.ElevatedButton(
        "REGISTRARSE",
        width=250,
        height=45,
        on_click=registrar_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=3,
            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.BOLD, letter_spacing=1),
        ),
    )
    
    btn_login = ft.TextButton(
        "🔑 ¿Ya tienes cuenta? Inicia sesión",
        on_click=lambda _: page.go("/"),
        style=ft.ButtonStyle(color=ft.Colors.BLUE_600),
    )
    
    # Permitir registro con Enter en el último campo
    confirm_password.on_submit = registrar_click
    
    return ft.View(
        route="/register",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Registro de Usuario", size=20, weight=ft.FontWeight.BOLD),
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
                    ft.Icon(ft.Icons.APP_REGISTRATION_ROUNDED, size=60, color=ft.Colors.GREEN_600),
                    ft.Container(height=5),
                    ft.Text("Crear Nueva Cuenta", size=28, weight="bold", color=ft.Colors.BLUE_800),
                    ft.Text("Completa tus datos para registrarte", size=14, color=ft.Colors.GREY_600),
                    ft.Container(height=20),
                    nombre,
                    ft.Container(height=10),
                    apellido,
                    ft.Container(height=10),
                    telefono,
                    ft.Container(height=10),
                    email,
                    ft.Container(height=10),
                    password,
                    ft.Container(height=10),
                    confirm_password,
                    ft.Container(height=10),
                    mensaje,
                    ft.Container(height=10),
                    btn_registrar,
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                            ft.Text("o", size=12, color=ft.Colors.GREY_500),
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                        ],
                        width=350,
                    ),
                    ft.Container(height=15),
                    btn_login,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=0,
            )
        ]
    )