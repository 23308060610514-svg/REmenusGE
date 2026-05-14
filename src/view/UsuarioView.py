import flet as ft

def UserView(page, auth_controller):
    page.title = "Perfil"
    user = getattr(page, "user_data", None)
    
    def formatear_fecha(fecha):
        if not fecha:
            return "No disponible"
        if isinstance(fecha, str) and ' ' in fecha:
            fecha_parte = fecha.split(' ')[0]  
            hora_parte = fecha.split(' ')[1]  
            año, mes, dia = fecha_parte.split('-')
            return f"{dia}/{mes}/{año} {hora_parte}"
        elif isinstance(fecha, str):
            año, mes, dia = fecha.split('-')
            return f"{dia}/{mes}/{año}"
        return str(fecha)
    
    nombre = ft.Text(f"Nombre: {user['nombre'] if user else 'Usuario'}", size=20)
    apellido = ft.Text(f"Apellido: {user['apellido'] if user else 'Usuario'}", size=20)
    telefono = ft.Text(f"Teléfono: {user['telefono'] if user else 'Usuario'}", size=20)
    email = ft.Text(f"Email: {user['email'] if user else 'Usuario'}", size=20)
    fecha_registro = ft.Text(f"Fecha de creación de la cuenta: {formatear_fecha(user['fecha_registro']) if user else 'Usuario'}", size=20)
    ultimo_acceso = ft.Text(f"Último acceso: {formatear_fecha(user['ultimo_acceso']) if user else 'Usuario'}", size=20)

    return ft.View(
        route="/perfil",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Perfil de Usuario", size=30),
                actions=[
                    ft.IconButton(ft.Icons.BOOK, on_click=lambda _: page.go("/dashboard")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Container(
                ft.Column([
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([nombre]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([apellido]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([telefono]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Row([email]),
                    ft.Divider(thickness=6, color=ft.Colors.BLUE),
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([fecha_registro]),
                    ft.Divider(thickness=8, color=ft.Colors.BLUE),
                    ft.Row([ultimo_acceso]),
                ], expand=True),
                padding=20, expand=True,
            ),
        ]
    )