import flet as ft

def LoginView(page: ft.Page, auth_controller):
    
    # Asegurar que la página tenga al menos una vista
    if not page.views:
        # Si no hay vistas, crear una vista temporal
        page.views.append(ft.View("/"))
    
    # Cambiar fondo de la página
    page.bgcolor = ft.Colors.GREY_50
    
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400,
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
        focused_bgcolor=ft.Colors.WHITE,
        content_padding=15,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.BLUE_200,
        focused_border_color=ft.Colors.BLUE_600,
        focused_bgcolor=ft.Colors.WHITE,
        content_padding=15,
    )
    
    mensaje = ft.Container(
        content=ft.Text("", color="red", size=12),
        visible=True,
        height=30,
    )
    
    # Extraer el texto del mensaje para modificarlo fácilmente
    mensaje_text = mensaje.content

    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Row([
                ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color=ft.Colors.WHITE, size=20),
                ft.Text(mensaje_texto, color=ft.Colors.WHITE, weight=ft.FontWeight.W_500),
            ]),
            bgcolor=color,
            duration=2500,
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        page.snack_bar.open = True
        page.update()

    def login_click(e):
        if not correo.value or not contraseña.value:
            mensaje_text.value = "⚠️ Por favor, llene todos los campos"
            mensaje_text.color = "red"
            page.update()
            return
        
        user, msg = auth_controller.login(correo.value, contraseña.value)
        if user:
            page.user_data = user
            mostrar_snackbar("✓ ¡Bienvenido al sistema!", ft.Colors.GREEN_600)
            page.views.clear()
            page.go("/dashboard")
        else:
            mensaje_text.value = f"✗ {msg}"
            mensaje_text.color = "red"
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "INICIAR SESIÓN",
        width=250,
        height=45,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation=3,
            text_style=ft.TextStyle(
                size=14,
                weight=ft.FontWeight.BOLD,
                letter_spacing=1,
            ),
        ),
    )
    
    btn_registro = ft.TextButton(
        "📝 ¿No tienes cuenta? Regístrate",
        on_click=lambda _: page.go("/register"),
        style=ft.ButtonStyle(
            color=ft.Colors.BLUE_600,
            text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500),
        ),
    )
    
    recuperar = ft.TextButton(
        "🔑 Recuperar contraseña",
        on_click=lambda _: page.go("/recover"),
        style=ft.ButtonStyle(
            color=ft.Colors.GREY_600,
            text_style=ft.TextStyle(size=12),
        ),
    )
    
    contraseña.on_submit = login_click

    # Crear la vista de login con diseño mejorado
    login_view = ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text(
                "REmenus - Inicio de Sesión",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            center_title=True,
            elevation=2,
        ),
        controls=[
            ft.Column(
                [
                    # Logo o ícono decorativo
                    ft.Icon(
                        ft.Icons.SECURITY_ROUNDED,
                        size=60,
                        color=ft.Colors.BLUE_600,
                    ),
                    ft.Container(height=5),
                    
                    # Título principal
                    ft.Text(
                        "Acceso a los Menús",
                        size=28,
                        weight="bold",
                        color=ft.Colors.BLUE_800,
                    ),
                    
                    # Subtítulo - ✅ MODIFICADO AQUÍ
                    ft.Text(
                        "Ingrese su información",  # ✅ Cambiado de "Ingrese sus credenciales" a "Ingrese su información"
                        size=14,
                        color=ft.Colors.GREY_600,
                    ),
                    
                    ft.Container(height=20),
                    
                    # Campos del formulario
                    correo,
                    ft.Container(height=15),
                    contraseña,
                    
                    ft.Container(height=5),
                    
                    # Fila para recuperar contraseña (alineado a la derecha)
                    ft.Row(
                        [recuperar],
                        alignment=ft.MainAxisAlignment.END,
                        width=400,
                    ),
                    
                    ft.Container(height=10),
                    
                    # Mensaje de error
                    mensaje,
                    
                    ft.Container(height=10),
                    
                    # Botón de inicio de sesión
                    iniciar_sesion,
                    
                    ft.Container(height=20),
                    
                    # Divisor decorativo
                    ft.Row(
                        [
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                            ft.Text("o", size=12, color=ft.Colors.GREY_500),
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                        ],
                        width=350,
                    ),
                    
                    ft.Container(height=15),
                    
                    # Botón de registro
                    btn_registro,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=0
            )
        ]
    )
    
    return login_view