import flet as ft

def MenuView(page: ft.Page, auth_controller, menu_controller):
    
    page.bgcolor = ft.Colors.GREY_50
    page.title = "REmenus - Menús"
    
    def mostrar_snackbar(mensaje, color=ft.Colors.GREEN_600):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()
    
    def ver_platillos(tipo):
        """Navega a la vista de platillos por tipo"""
        page.go(f"/menus/{tipo}")
    
    def cerrar_sesion(e):
        page.user_data = None
        page.go("/")
        mostrar_snackbar("Sesión cerrada correctamente", ft.Colors.BLUE_600)
    
    # Datos de las categorías
    categorias = [
        {"tipo": "mexicana", "nombre": "Comida Mexicana", "icono": ft.Icons.RESTAURANT, "color": ft.Colors.RED_600, "descripcion": "Platillos tradicionales de México"},
        {"tipo": "china", "nombre": "Comida China", "icono": ft.Icons.RICE_BOWL, "color": ft.Colors.AMBER_700, "descripcion": "Sabores auténticos de la cocina china"},
        {"tipo": "mariscos", "nombre": "Mariscos", "icono": ft.Icons.SET_MEAL, "color": ft.Colors.BLUE_600, "descripcion": "Los mejores mariscos del puerto"}
    ]
    
    # Crear tarjetas para cada categoría
    tarjetas_menu = []
    
    for cat in categorias:
        tarjeta = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(cat["icono"], size=60, color=cat["color"]),
                    ft.Container(height=10),
                    ft.Text(
                        cat["nombre"],
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=cat["color"],
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=5),
                    ft.Text(
                        cat["descripcion"],
                        size=12,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=15),
                    ft.ElevatedButton(
                        "Ver Menú",
                        on_click=lambda e, t=cat["tipo"]: ver_platillos(t),
                        style=ft.ButtonStyle(
                            bgcolor=cat["color"],
                            color=ft.Colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=10),
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
            width=300,
            height=300,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            padding=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.GREY_300,
                offset=ft.Offset(0, 4),
            ),
        )
        tarjetas_menu.append(tarjeta)
    
    # Botón de cerrar sesión
    btn_cerrar_sesion = ft.IconButton(
        icon=ft.Icons.LOGOUT_ROUNDED,
        icon_color=ft.Colors.WHITE,
        tooltip="Cerrar sesión",
        on_click=cerrar_sesion,
    )
    
    # Obtener nombre del usuario
    nombre_usuario = page.user_data.get('nombre', 'Usuario') if page.user_data else "Usuario"
    
    return ft.View(
        route="/dashboard",
        bgcolor=ft.Colors.GREY_50,
        appbar=ft.AppBar(
            title=ft.Text(
                "REmenus - Sistema de Menús",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            bgcolor=ft.Colors.BLUE_700,
            center_title=True,
            actions=[btn_cerrar_sesion],
            elevation=2,
        ),
        controls=[
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Row(
                        [
                            ft.Text(
                                f"¡Bienvenido, {nombre_usuario}!",
                                size=20,
                                color=ft.Colors.BLUE_800,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        [
                            ft.Text(
                                "Selecciona una categoría",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLUE_800,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        [
                            ft.Text(
                                "Explora nuestros deliciosos platillos",
                                size=16,
                                color=ft.Colors.GREY_600,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Container(height=30),
                    ft.Row(
                        tarjetas_menu,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=30,
                        wrap=True,
                    ),
                    ft.Container(height=30),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            )
        ],
    )
