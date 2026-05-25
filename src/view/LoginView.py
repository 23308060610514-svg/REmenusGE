import flet as ft

def LoginView(page: ft.Page, auth_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL_ROUNDED,
        width=400,
        border_radius=12,
        keyboard_type=ft.KeyboardType.EMAIL,
        bgcolor=ft.Colors.WHITE,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=12,
        bgcolor=ft.Colors.WHITE,
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

    def login_click(e):
        print(f"🔐 Intentando login con: {correo.value}")  # Debug
        
        if not correo.value or not contraseña.value:
            mensaje.value = "⚠️ Por favor, llene todos los campos"
            mensaje.color = "red"
            page.update()
            return
        
        user, msg = auth_controller.login(correo.value, contraseña.value)
        print(f"📦 Resultado login - User: {user}, Msg: {msg}")  # Debug
        
        if user:
            page.user_data = user
            print(f"✅ user_data guardado: {page.user_data}")  # Debug
            mostrar_snackbar("✓ ¡Bienvenido a REMenus!", ft.Colors.GREEN_600)
            page.go("/dashboard")
        else:
            mensaje.value = f"✗ {msg}"
            mensaje.color = "red"
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "INICIAR SESIÓN",
        width=250,
        height=45,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    btn_registro = ft.TextButton(
        "📝 ¿No tienes cuenta? Regístrate",
        on_click=lambda _: page.go("/register"),
    )
    
    recuperar = ft.TextButton(
        "🔑 Recuperar contraseña",
        on_click=lambda _: page.go("/recover"),
    )
    
    contraseña.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text("REmenus - Inicio de Sesión", size=20, weight=ft.FontWeight.BOLD),
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            center_title=True,
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.RESTAURANT_MENU, size=60, color=ft.Colors.BLUE_600),
                    ft.Container(height=5),
                    ft.Text("Bienvenido a REMenus", size=28, weight="bold", color=ft.Colors.BLUE_800),
                    ft.Text("Ingresa tus datos para continuar", size=14, color=ft.Colors.GREY_600),
                    ft.Container(height=20),
                    correo,
                    ft.Container(height=15),
                    contraseña,
                    ft.Container(height=5),
                    ft.Row([recuperar], alignment=ft.MainAxisAlignment.END, width=400),
                    ft.Container(height=10),
                    mensaje,
                    ft.Container(height=10),
                    iniciar_sesion,
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
                    btn_registro,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=0,
            )
        ],
    )